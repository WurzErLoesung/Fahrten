from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.pupdevices import ColorSensor, Motor, UltrasonicSensor
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, wait

# Aus calibrate.py ermittelte Werte hier eintragen.
WHEEL_DIAMETER = 61.98
AXLE_TRACK = 159.7


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
        self.hub = PrimeHub()
        self.left_motor = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.B)
        self.drive_base = DriveBase(
            self.left_motor, self.right_motor, WHEEL_DIAMETER, AXLE_TRACK
        )
        self.action_left = Motor(Port.E)
        self.action_right = Motor(Port.A)
        self.imu = self.hub.imu
        self.color = ColorSensor(Port.C)
        self.timer = StopWatch()
        self.straight = self.drive_base.straight


if __name__ == "__main__":
    hub = PrimeHub()
    print(hub.system.name())
    p = PupDevices()
    p2 = PupDevices()
    print(p == p2)
