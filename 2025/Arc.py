from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from umath import sin, cos, pi

hub = PrimeHub()

def action_arc(radius: int, angle: int, velocity: int):

    """
    Moves any forklift like structure in an arc like motion

    :param radius: The radius of the arc in mm
    :param angle: The final angle of the arc
    :param velocity: Degrees of the arc per second
    """

    ma = Motor(Port.A, direction=Direction.COUNTERCLOCKWISE)
    mleft = Motor(Port.B)
    mright = Motor(Port.F, direction=Direction.COUNTERCLOCKWISE)
    db = DriveBase(mleft, mright, 56, 113)
    
    velocity_cm = (phi * 2 * radius * pi) / 360

    velocity_forklift = (3 * velocity_cm) / 360
    velocity_movement = (56 * pi * velocity_cm) / 360

    t_max = angle / velocity

    s = StopWatch()
    while (t:=s.time()) < t_final:
        phi = t * (angle / t_max)
        vertical_ratio, horizontal_ratio = velocity * cos(phi), velocity * sin(phi)
        ma.start(vertical_ratio * velocity_forklift)
        db.start(horizontal_ratio * velocity_movement)

    db.stop()
    ma.stop()

        
if __name__ == "__main__":
    action_arc(10, 90, 10)
        


