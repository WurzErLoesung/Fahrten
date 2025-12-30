from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.pupdevices import ColorSensor, Motor, UltrasonicSensor
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, wait


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
        color_top_port = Port.A
        color_bottom_port = Port.B
        if self.hub.system.name() == "ROOTBOTS 2":
            color_top_port, color_bottom_port = color_bottom_port, color_top_port
        self.left_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.D)
        self.drive_base = DriveBase(self.left_motor, self.right_motor, 56, 145)
        self.action_left = Motor(Port.E)
        self.action_right = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
        self.imu = self.hub.imu
        self.color_bottom = ColorSensor(color_bottom_port)
        self.color = ColorSensor(color_top_port)
        self.timer = StopWatch()
        self.straight = self.drive_base.straight


if __name__ == "__main__":
    hub = PrimeHub()
    print(hub.system.name())
    p = PupDevices()
    p2 = PupDevices()
    print(p == p2)
