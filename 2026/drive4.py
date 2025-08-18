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


def drive4(pd):
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(500, 500)
    yaw = Yaw(hub, pd.left_motor, pd.right_motor, positive_direction=-1)
    yield True

    pd.action_left.run_angle(200, 50)

    pd.action_right.run_until_stalled(-300, then=Stop.COAST, duty_limit=35)
    pd.drive_base.straight(400)


    for i in range(3):
        pd.action_right.run_angle(600, 150)
        wait(500)
        pd.action_right.run_angle(300, -160)
        wait(250)
    yield True
    pd.action_right.run_until_stalled(-300, then=Stop.COAST, duty_limit=50)
    pd.action_left.run_angle(200, -50)

    pd.drive_base.straight(-100)
    yaw(-30)
    pd.drive_base.straight(460)
    yaw(60)
    pd.drive_base.straight(110)
    pd.action_left.run_angle(200, 50)
    pd.action_right.run_angle(100, 120)
    yaw(20)
    pd.drive_base.straight(-25)
    yaw(-12)
    pd.drive_base.straight(-50)
    pd.action_right.run_angle(100, -90)
    pd.action_left.run_angle(200, -50)
    yaw(90)
    pd.drive_base.straight(220)
    pd.action_left.run_angle(200, 50)
    pd.drive_base.straight(200)
    pd.drive_base.straight(-58)
    pd.action_right.run_angle(100, 40)
    pd.drive_base.straight(200)
    pd.action_right.run_angle(100, 30)


if __name__ == "__main__":
    for element in drive4(PupDevices()):
        pass