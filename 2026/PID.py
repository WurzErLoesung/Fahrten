from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from yaw import Yaw
import umath as math


class PID:
    def __init__(self, ml, mr, wheel_diameter: int = None, acceleration: int = None, min_speed: int = None, max_speed: int = None):
        self.imu = PrimeHub().imu
        self.ml = ml
        self.mr = mr
        self.wheel_diameter = abs(wheel_diameter) if wheel_diameter is not None else 0
        self.wheel_circumference = math.pi * self.wheel_diameter
        self.acceleration = abs(acceleration) if acceleration is not None else 100
        self.min_speed = abs(min_speed) if min_speed is not None else 100
        self.max_speed = abs(max_speed) if max_speed is not None else 900
        self.debug = []

        self.Kp = 0.04
        self.Tn = 2400
        self.Tv = 250
        self.tuning_speed = 800
        self.speed_multiplier = 1

        self.error = 0
        self.previous = 0

        self.running = False


# ----- CALCULATIONS ----- #

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def calc_acceleration(self, acceleration: int, current_distance: int, target_distance: int, min_speed: int = None, max_speed: int = None):
        self.min_speed = min_speed if min_speed is not None else self.min_speed
        self.max_speed = max_speed if max_speed is not None else self.max_speed
        distance_ratio = current_distance / target_distance
        speed_increment = acceleration * min(current_distance, 0.5 * target_distance)
        speed_reduction = acceleration * min(0, current_distance - 0.5*target_distance)
        return min(max_speed, max(min_speed, min_speed + speed_increment - speed_reduction))

    def calc_pid_speed(self, speed: tuple, target_angle: int, debug: Bool = False):
        heading = self.imu.heading()
        p = -(target_angle - heading)
        i = self.error + p
        d = p - self.previous

        self.previous = p
        self.error = i

        p *= self.Kp
        i *= self.Kp / self.Tn
        #d *= self.Tv * self.Kp
        d = 0
        if debug: 
            print("P:" , p)
            print("Gyro:" , heading)
            self.debug.append(heading)  
            print("Avg:", sum(self.debug) / len(self.debug))

        correction_ratio = 2 * self.sigmoid((p + i + d) * self.speed_multiplier * (self.tuning_speed / (sum(speed) / len(speed)))) 
        return speed[0] * correction_ratio, speed[1] * (2 - correction_ratio)

# ----- DRIVING ----- #

    async def straight(self, speed: int, distance: int, acceleration: int = None, min_speed: int = None, debug: bool = False):
        # acceleration = acceleration if acceleration is not None else self.acceleration
        min_speed = min_speed if min_speed is not None else self.min_speed
        self.running = True
        left_starting_angle = self.ml.angle()
        right_starting_angle = self.mr.angle()
        current_distance = 0
        heading = self.imu.heading()
        while current_distance < distance:
            vr, vl = self.calc_pid_speed((speed, speed), heading)
            self.ml.run(vl)
            self.mr.run(vr)
            await wait(1)
            left_angle = abs(self.ml.angle()) - left_starting_angle
            right_angle = abs(self.mr.angle()) - right_starting_angle
            current_distance = ((left_angle + right_angle) * self.wheel_circumference) / (2 * 360)
        self.ml.stop()
        self.mr.stop()

    async def straight_ratio(self, speed: int, distance: int, ratios: tuple, acceleration: int = None, min_speed: int = None, debug: bool = False):
        # acceleration = acceleration if acceleration is not None else self.acceleration
        min_speed = min_speed if min_speed is not None else self.min_speed
        self.running = True
        left_starting_angle = self.ml.angle()
        right_starting_angle = self.mr.angle()
        current_distance = 0
        heading = self.imu.heading()
        while current_distance < distance:
            vr, vl = self.calc_pid_speed((speed * ratios[0], speed * ratios[1]), heading)
            self.ml.run(vl)
            self.mr.run(vr)
            await wait(1)
            left_angle = abs(self.ml.angle()) - left_starting_angle
            right_angle = abs(self.mr.angle()) - right_starting_angle
            current_distance = ((left_angle + right_angle) * self.wheel_circumference) / (2 * 360)
        self.ml.stop()
        self.mr.stop()

    async def start(self, speed: int, debug: bool = False):
        self.running = True
        heading = self.imu.heading()
        while self.running:
            vl, vr = self.calc_pid_speed((speed, speed), heading)
            self.ml.run(vl)
            self.mr.run(vr)
            await wait(1)
        self.ml.stop()
        self.mr.stop()

    async def stop(self):
        self.running = False



async def main(pid):
    await wait(5000)
    pid.stop()
    #await pid.straight(800, 1000)

async def motor(action):
    await wait(2000)
    await action.run_angle(360, 10*360)


if __name__ == "__main__":
    hub = PrimeHub()
    ma, me = Motor(Port.B), Motor(Port.F, positive_direction = Direction.COUNTERCLOCKWISE)
    yaw = Yaw(hub, ma, me, max_velocity=400, positive_direction=1)
    pid = PID(ma, me, 57)
    
    # yaw(90)
    # yaw(-90)
    # yaw(0)
    run_task(multitask(pid.start(800), motor(Motor(Port.A))))
