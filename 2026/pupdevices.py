from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class PupDevices:
    def __init__(self):
        self.left_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.D)
        self.drive_base = DriveBase(self.left_motor, self.right_motor, 56, 145)
        self.action_left = Motor(Port.E)
        self.action_right = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
        self.hub = PrimeHub()
        self.imu = self.hub.imu
        self.color = ColorSensor(Port.B)
        self.color_top = ColorSensor(Port.A)
        self.timer = StopWatch()

if __name__ == "__main__":
    hub = PrimeHub()
    print(hub.system.name())
    p = PupDevices()
    p2 = PupDevices()
    print(p == p2)
