from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Stop
from pybricks.tools import wait, StopWatch, run_task


class Yaw:
    """Dreht den Roboter auf eine absolute Gyro-Ausrichtung.

    Der Zielwinkel ist absolut (0-359), nicht relativ: yaw(90) dreht auf
    Kurs 90, egal wo der Roboter gerade steht. yaw(-90) entspricht 270.
    """

    def __init__(self, hub, left_motor, right_motor, positive_direction=1,
                 min_velocity: int = 20, max_velocity: int = 300,
                 acceleration: int = 500, stop_action=Stop.BRAKE,
                 tolerance: float = 0.1, time_limit: int = 3000):
        self.hub = hub
        self.ml = left_motor
        self.mr = right_motor
        self.direction = positive_direction
        self.min_velocity = min_velocity
        self.max_velocity = max_velocity
        self.acceleration = acceleration
        self.stop_action = stop_action
        self.tolerance = tolerance
        self.time_limit = time_limit

    def _stop(self):
        """Einziger Ausgang der Drehung. Coast waere hier nicht reproduzierbar,
        weil der Ausrollweg von Reibung und Temperatur abhaengt."""
        if self.stop_action == Stop.HOLD:
            self.ml.hold()
            self.mr.hold()
        elif self.stop_action == Stop.COAST:
            self.ml.stop()
            self.mr.stop()
        else:
            self.ml.brake()
            self.mr.brake()

    async def __call__(self, deg, min_velocity: int = None, max_velocity: int = None,
                       acceleration: int = None, stop_action=None,
                       tolerance: float = None, time_limit: int = None):
        # Parameter einmal vorab aufloesen, nicht in der Schleife.
        min_velocity = min_velocity if min_velocity is not None else self.min_velocity
        max_velocity = max_velocity if max_velocity is not None else self.max_velocity
        acceleration = acceleration if acceleration is not None else self.acceleration
        tolerance = tolerance if tolerance is not None else self.tolerance
        time_limit = time_limit if time_limit is not None else self.time_limit

        previous_stop_action = self.stop_action
        if stop_action is not None:
            self.stop_action = stop_action

        # Hoehere Werte = hoehere Durchschnittsgeschwindigkeit, aber schneller
        # in Zielnaehe und damit groesseres Ueberschwingen.
        speed_potency = 3

        deg = deg % 360
        s = StopWatch()
        timed_out = False

        try:
            while True:
                # heading() % 360 liegt in Python immer in [0, 360).
                current_yaw = self.hub.imu.heading() % 360
                difference = deg - current_yaw

                if abs(difference) < tolerance:
                    break

                elapsed = s.time()
                if elapsed > time_limit:
                    print("Timeout, Restfehler:", round(difference, 2))
                    timed_out = True
                    break

                # Immer den kuerzeren Weg nehmen.
                if abs(difference) > 180:
                    difference = (360 - abs(difference)) * -1 * (difference / abs(difference))

                sign = 1 if difference >= 0 else -1

                velocity = round(
                    min_velocity
                    + (max_velocity - min_velocity) * (abs(difference) / 180) ** (1 / speed_potency)
                )
                # Anfahrrampe, relativ zum Start dieser Drehung.
                accelerated_velocity = min(elapsed / 1000 * acceleration, velocity)

                self.ml.run(-self.direction * accelerated_velocity * sign)
                self.mr.run(self.direction * accelerated_velocity * sign)

                await wait(0)

            self._stop()
        finally:
            self.stop_action = previous_stop_action

        # Restfehler in Grad zurueckgeben, damit ihr die Streuung messen koennt.
        error = (self.hub.imu.heading() - deg) % 360
        if error > 180:
            error -= 360
        return error, timed_out

    def reset(self, angle):
        self.hub.imu.reset_heading(angle)


if __name__ == "__main__":
    hub = PrimeHub()

    # Portbelegung wie in pupdevices.py: links = F (CCW), rechts = B.
    ml = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
    mr = Motor(Port.B)
    yaw = Yaw(hub, ml, mr, min_velocity=50, max_velocity=500, acceleration=800)

    async def demo():
        for ziel in (90, 270, 0):
            w = StopWatch()
            error, timed_out = await yaw(ziel)
            print(ziel, "->", w.time(), "ms   Restfehler:", round(error, 2))
            await wait(1500)  # Gyro Zeit zur Rekalibrierung geben

    run_task(demo())