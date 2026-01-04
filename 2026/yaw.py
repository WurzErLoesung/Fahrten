from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
import umath as math

class Yaw:
    def __init__(self, hub, left_motor, right_motor, positive_direction=1, min_velocity: int = 20, max_velocity: int = 300, acceleration: int = 500):
        self.hub = hub
        self.ml = left_motor
        self.mr = right_motor
        self.direction = positive_direction
        self.min_velocity = min_velocity
        self.max_velocity = max_velocity
        self.acceleration = acceleration

    async def __call__(self, deg, min_velocity: int = None, max_velocity: int = None, acceleration: int = None):
        min_velocity = min_velocity if min_velocity is not None else self.min_velocity
        max_velocity = max_velocity if max_velocity is not None else self.max_velocity
        
        deg = deg % 360
        time_limit = 3000
        s = StopWatch()
        start = s.time()
        while True:
            current_yaw = (self.hub.imu.heading()) % 360
            if current_yaw < 0: current_yaw = 360 - current_yaw
            difference = deg - current_yaw
    
    
            if abs(difference) < 0.1:
                self.ml.stop()
                self.mr.stop()
                break
    
            if s.time() - start > time_limit:
                print("Timeout")
                break
    
    
            if abs(difference) > 180:
                difference = (360 - abs(difference)) * -1 * (difference/abs(difference))
            
            direction = 1 if difference >= 0 else -1
    
            # higher values = higher average speed
            speed_potency = 3

            acceleration = acceleration if acceleration is not None else self.acceleration
            velocity = round(min_velocity + (max_velocity - min_velocity) * (abs(difference) / 180) ** (1 / speed_potency))
            accelerated_velocity = min((s.time() / 1000) * acceleration, velocity)

            self.ml.run(-self.direction * accelerated_velocity * direction)
            self.mr.run(self.direction * accelerated_velocity * direction)
            
            await wait(0)
    
        self.ml.stop()
        self.mr.stop()

    def reset(self, angle):
        self.hub.imu.reset_heading(angle)

if __name__ == "__main__":
    hub =  PrimeHub()

    ml = Motor(Port.C)
    mr = Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
    yaw = Yaw(hub, ml, mr)
    run_task(yaw(90))
    run_task(yaw(-90))
