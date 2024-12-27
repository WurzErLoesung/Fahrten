from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


class PupDevices(object):
     def __new__(cls, *args, **kw):
         if not hasattr(cls, '_instance'):
             orig = super(PupDevices, cls)
             cls._instance = orig.__new__(cls, *args, **kw)
         return cls._instance

     def __init__(self):
         self.left_motor = Motor(Port.B)
         self.right_motor = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
         self.action_front = Motor(Port.C)
         self.action_back = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
         self.hub = PrimeHub()
         self.imu = self.hub.imu
         self.ultra = UltrasonicSensor(Port.E)
         self.color = ColorSensor(Port.D)

