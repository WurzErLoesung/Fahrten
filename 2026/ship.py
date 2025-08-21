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

watch = StopWatch()

hub.speaker.beep()


def ship(pd):
    # DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(-90)
    pd.drive_base.settings(900, 500)
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)
    yield True

    pd.action_right.run_angle(5000, 900)
    pd.action_right.run_until_stalled(-5000, duty_limit=50)
    pd.drive_base.arc(2000, distance=-595)
    pd.action_left.run_angle(1500, 60)
    pd.drive_base.arc(2000, distance=595)

    yield False
    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()


if __name__ == "__main__":
    for element in ship(PupDevices()):
        pass
