# ======= Straight Driving with Persistent Trim (Pybricks / PrimeHub) =======

import umath as math
from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.tools import multitask, run_task, wait

# Optional helper you already had (not required by this file)
try:
    from yaw import Yaw
except ImportError:
    Yaw = None

# Use ujson on hub for speed; fall back to json if needed.
try:
    import ujson as json
except ImportError:
    import json


class PID:
    def __init__(
        self,
        ml,
        mr,
        wheel_diameter: int = 56,
        acceleration: int = 100,
        min_speed: int = 100,
        max_speed: int = 900,
    ):
        self.hub = PrimeHub()
        self.imu = self.hub.imu
        self.ml = ml
        self.mr = mr

        # Geometry (mm)
        self.wheel_diameter = abs(int(wheel_diameter))
        self.wheel_circumference = math.pi * self.wheel_diameter

        # Motion params (deg/s)
        self.acceleration = abs(int(acceleration))
        self.min_speed = abs(int(min_speed))
        self.max_speed = abs(int(max_speed))

        # PI tuning
        self.Kp = 0.04
        self.Tn = 2400  # integral time constant
        self.tuning_speed = 800
        self.speed_multiplier = 1

        # Controller state
        self._i_acc = 0.0
        self._prev_p = 0.0
        self.running = False

        # Persistent left/right trim ratio
        self.trim_ratio = (1.0, 1.0)
        self._load_trim()

    # ---------- Persistence ---------- #

    def _load_trim(self):
        try:
            with open("trim.json", "r") as f:
                data = json.load(f)
                print(data)
                t = data.get("trim_ratio", [1.0, 1.0])
                self.trim_ratio = (float(t[0]), float(t[1]))
        except OSError:
            # First run or no file yet
            self.trim_ratio = (1.0, 1.0)
            print("File emtpy!")

    def _save_trim(self):
        try:
            with open("trim.json", "w") as f:
                json.dump({"trim_ratio": [self.trim_ratio[0], self.trim_ratio[1]]}, f)
        except OSError:
            # Ignore if storage isn’t available right now
            pass

    # ---------- Math helpers ---------- #

    @staticmethod
    def _clamp(x, lo, hi):
        return hi if x > hi else lo if x < lo else x

    @staticmethod
    def _angle_error(target, current):
        """Shortest signed angle error (degrees). Negative keeps original sign convention."""
        e = (target - current + 180) % 360 - 180
        return -e

    @staticmethod
    def _sigmoid(x):
        return 1.0 / (1.0 + math.exp(-x))

    # ---------- Controller ---------- #

    def calc_pid_speed(self, base_speed: tuple, target_angle: int, debug: bool = False):
        """
        base_speed: (left_base, right_base) in deg/s
        returns: (vl, vr) motor commands in deg/s
        """
        # Apply persistent trim so it’s straight immediately
        base_speed = (
            base_speed[0] * self.trim_ratio[0],
            base_speed[1] * self.trim_ratio[1],
        )

        heading = self.imu.heading()

        # PI terms
        p = self._angle_error(target_angle, heading)
        i = self._i_acc + p
        # Derivative is disabled for gyro-noise simplicity. Add filtered D if desired.

        # Anti-windup clamp and save state
        i = self._clamp(i, -2000, 2000)
        self._i_acc = i
        self._prev_p = p

        # Scale terms
        p *= self.Kp
        i *= self.Kp / self.Tn
        u = p + i  # PI output

        # Smoothly split speeds using a ratio in (0, 2)
        avg_base = (
            (base_speed[0] + base_speed[1]) / 2.0
            if (base_speed[0] + base_speed[1]) != 0
            else 1.0
        )
        gain = (self.tuning_speed / avg_base) * self.speed_multiplier
        correction_ratio = 2.0 * self._sigmoid(u * gain)

        # Apply split, keep order (vl, vr)
        vl = base_speed[0] * (2.0 - correction_ratio)
        vr = base_speed[1] * correction_ratio

        # Enforce motor limits
        vl = self._clamp(vl, -self.max_speed, self.max_speed)
        vr = self._clamp(vr, -self.max_speed, self.max_speed)

        # Keep near minimum if commanded forward
        if base_speed[0] > 0 and base_speed[1] > 0:
            vl = self._clamp(vl, self.min_speed, self.max_speed)
            vr = self._clamp(vr, self.min_speed, self.max_speed)

        if debug:
            print(
                "Heading:",
                heading,
                "P:",
                p,
                "I:",
                i,
                "Trim:",
                self.trim_ratio,
                "vl/vr:",
                vl,
                vr,
            )

        return vl, vr

    def _adapt_trim(self, vl, vr, lr=0.02):
        """
        Gentle online adaptation so both sides do similar work.
        Call at ~10–20 Hz while moving forward.
        """
        avl = abs(vl)
        avr = abs(vr)
        if avl == 0 or avr == 0:
            return
        ratio = avr / avl
        # Update inversely so product stays roughly around 1
        self.trim_ratio = (
            self.trim_ratio[0] * (1.0 / (ratio**lr)),
            self.trim_ratio[1] * (ratio**lr),
        )

    # ---------- Driving ---------- #

    async def _soft_start_and_lock_heading(self, settle_ms=200, nudge_ms=120):
        """
        Average heading briefly (reduce noise), zero PI, and give a tiny open-loop nudge.
        Returns the locked target heading.
        """
        # Average IMU heading for a short settle
        samples = max(1, settle_ms // 10)
        h_sum = 0.0
        for _ in range(samples):
            h_sum += self.imu.heading()
            await wait(10)
        target = h_sum / samples

        # Reset controller state
        self._i_acc = 0.0
        self._prev_p = 0.0

        # Small nudge to overcome static friction
        self.ml.run(self.min_speed)
        self.mr.run(self.min_speed)
        await wait(nudge_ms)

        return target

    async def straight(self, speed: int, distance_mm: int, debug: bool = False):
        """Drive straight for a linear distance (mm) at approx. 'speed' (deg/s per wheel)."""
        self.running = True

        # Record starting angles (deg)
        left_start = self.ml.angle()
        right_start = self.mr.angle()
        distance = 0.0

        # Lock heading & soft start
        target = await self._soft_start_and_lock_heading()

        # Controller period ~10 ms
        while distance < distance_mm:
            vl, vr = self.calc_pid_speed((speed, speed), target, debug=debug)
            self.ml.run(vl)
            self.mr.run(vr)

            # Online trim adaptation when going forward
            if vl > 0 and vr > 0:
                self._adapt_trim(vl, vr, lr=0.02)

            await wait(10)

            # Angle deltas (deg): subtract first, then abs
            left_delta = abs(self.ml.angle() - left_start)
            right_delta = abs(self.mr.angle() - right_start)

            # Convert to mm (avg of the two wheels)
            distance = ((left_delta + right_delta) * self.wheel_circumference) / (
                2.0 * 360.0
            )

        self.ml.stop()
        self.mr.stop()
        self.running = False

        # Save any improved trim for next run
        self._save_trim()

        # Reset controller state for next action
        self._i_acc = 0.0
        self._prev_p = 0.0

    async def straight_ratio(
        self, speed: int, distance_mm: int, ratios: tuple, debug: bool = False
    ):
        """Drive straight with base left/right scaling (bias compensation)."""
        self.running = True
        left_start = self.ml.angle()
        right_start = self.mr.angle()
        distance = 0.0
        target = await self._soft_start_and_lock_heading()

        while distance < distance_mm:
            base = (speed * ratios[0], speed * ratios[1])
            vl, vr = self.calc_pid_speed(base, target, debug=debug)
            self.ml.run(vl)
            self.mr.run(vr)

            if vl > 0 and vr > 0:
                self._adapt_trim(vl, vr, lr=0.02)

            await wait(10)

            left_delta = abs(self.ml.angle() - left_start)
            right_delta = abs(self.mr.angle() - right_start)
            distance = ((left_delta + right_delta) * self.wheel_circumference) / (
                2.0 * 360.0
            )

        self.ml.stop()
        self.mr.stop()
        self.running = False
        self._save_trim()
        self._i_acc = 0.0
        self._prev_p = 0.0

    async def start(self, speed: int, debug: bool = False):
        """Keep current heading and drive until stop() is called."""
        self.running = True
        target = await self._soft_start_and_lock_heading()

        while self.running:
            vl, vr = self.calc_pid_speed((speed, speed), target, debug=debug)
            self.ml.run(vl)
            self.mr.run(vr)

            if vl > 0 and vr > 0:
                self._adapt_trim(vl, vr, lr=0.02)

            await wait(10)

        self.ml.stop()
        self.mr.stop()
        self._save_trim()
        self._i_acc = 0.0
        self._prev_p = 0.0

    async def stop(self):
        self.running = False

    # ---------- One-shot calibration (optional) ---------- #

    async def auto_trim(self, speed=400, ms=1200, debug: bool = False):
        """
        Run once to measure and store a good static trim quickly.
        After this, every run starts straight immediately.
        """
        await wait(300)
        target = self.imu.heading()
        self._i_acc = 0.0
        self._prev_p = 0.0

        samples = 0
        sum_vl = 0.0
        sum_vr = 0.0
        t = 0
        while t < ms:
            vl, vr = self.calc_pid_speed((speed, speed), target, debug=debug)
            self.ml.run(vl)
            self.mr.run(vr)
            await wait(10)
            t += 10
            sum_vl += abs(vl)
            sum_vr += abs(vr)
            samples += 1

        self.ml.stop()
        self.mr.stop()

        if samples > 0:
            avg_l = sum_vl / samples
            avg_r = sum_vr / samples
            m = max(avg_l, avg_r)
            if m > 0:
                k_l = avg_r / m
                k_r = avg_l / m
                self.trim_ratio = (k_l, k_r)
                if debug:
                    print("Auto-trim set to:", self.trim_ratio)
                self._save_trim()

        self._i_acc = 0.0
        self._prev_p = 0.0


# ---------- Parallel demo coroutines ---------- #


async def stop_after(pid: PID, ms=5000):
    """Example: stop the continuous driver after some time."""
    await wait(ms)
    await pid.stop()


async def spin_motor_after(motor: Motor, delay_ms=2000, speed=360, angle=10 * 360):
    """Spin a third motor after a delay (blocking run_angle is fine; don't 'await' it)."""
    await wait(delay_ms)
    motor.run_angle(speed, angle)


# ---------- Main ---------- #

if __name__ == "__main__":
    hub = PrimeHub()

    # Drive motors: left on B, right on F (invert right so forward matches left)
    ml = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)  # left
    mr = Motor(Port.D)  # right

    # Optional yaw helper (unused by PI controller)
    if Yaw is not None:
        yaw = Yaw(hub, ml, mr, max_velocity=400, positive_direction=1)

    # Wheel diameter: set to your tire (e.g., LEGO 56x26 is ~56–57 mm)
    pid = PID(ml, mr, wheel_diameter=57, min_speed=100, max_speed=900)

    # ---- Example A: continuous driving with a parallel task ----
    """
    run_task(
        multitask(
            pid.start(800),  # hold heading at ~800 deg/s per wheel
            spin_motor_after(Motor(Port.E), 2000),  # spin motor A after 2 s
            # stop_after(pid, 5000),                 # optionally stop after 5 s
        )
    )
    """
    # ---- Example B: one-shot distance drive (uncomment to use) ----
    run_task(pid.straight(800, 1000))  # drive ~1000 mm then stop

    # ---- Example C: one-time calibration (uncomment and run once) ----
    # run_task(pid.auto_trim(speed=400, ms=1200, debug=True))
