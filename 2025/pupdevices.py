from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


class PupDevices(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = super(PupDevices, cls).__new__(cls)

            cls._instance.left_motor = Motor(Port.B)
            cls._instance.right_motor = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
            cls._instance.action_front = Motor(Port.C)
            cls._instance.action_back = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
            cls._instance.hub = PrimeHub()
            cls._instance.imu = cls._instance.hub.imu
            cls._instance.ultra = UltrasonicSensor(Port.E)
            cls._instance.color = ColorSensor(Port.D)
        return cls._instance
