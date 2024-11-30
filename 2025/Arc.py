from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

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

    t_max = angle / velocity

    s = StopWatch()
    t = 0
    while s.time() < t_final:
        phi = t * (angle / t_max)
        
        dt = s.time() - t
        t = s.time()