from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import (ColorSensor, ForceSensor, Motor,
                                 UltrasonicSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, run_task, wait

from pupdevices import PupDevices
from yaw import Yaw

hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")
print(hub.system.name())

watch = StopWatch

hub.speaker.beep()


def straight(pd):
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(320, 200, 250, 250)
    yaw = Yaw(hub, pd.left_motor, pd.right_motor, positive_direction=-1)
    yield True

    pd.drive_base.straight(1000)


if __name__ == "__main__":
    for element in straight(PupDevices()):
        pass
