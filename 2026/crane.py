from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import (ColorSensor, ForceSensor, Motor,
                                 UltrasonicSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, run_task, wait

from pupdevices import PupDevices
from yaw import Yaw

hub = PrimeHub()

print(f"Name: {hub.system.name()}, {hub.battery.voltage()/1000} Volt")

watch = StopWatch()

hub.speaker.beep()


def crane(pd):
    # DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(-90)
    pd.drive_base.settings(400, 500)
    yaw = Yaw(
        hub,
        pd.right_motor,
        pd.left_motor,
        min_velocity=40,
        max_velocity=600,
        acceleration=700,
    )
    yield True

    pd.action_right.run(200)

    pd.drive_base.straight(630)
    yield True




    yaw(-110)
    yield True


    pd.drive_base.straight(160)

    yaw(-91.5)
    yield True


    pd.action_left.run_time(-1000, 1100)
    yield True

    yaw(-170)
    pd.drive_base.settings(300, 300)
    pd.drive_base.straight(-105)
    yield True

    pd.drive_base.straight(150)
    yield True

    pd.drive_base.settings(400, 500)

    yaw(-120)
    pd.drive_base.straight(-330)
    yield True

    pd.drive_base.straight(150)
    yaw(-74)
    yield True
    pd.drive_base.settings(700, 700)
    pd.drive_base.straight(-570)

    yield False
    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()


if __name__ == "__main__":
    for element in crane(PupDevices()):
        pass
