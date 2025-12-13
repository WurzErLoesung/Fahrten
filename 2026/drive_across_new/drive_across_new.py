from pupdevices import PupDevices
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import (ColorSensor, ForceSensor, Motor,
                                 UltrasonicSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, run_task, wait
from yaw import Yaw

hub = PrimeHub()
print(f"{hub.battery.voltage()/1000} Volt")
watch = StopWatch()
hub.speaker.beep()


def drive_across_new(pd):
    # DriveBase initialisieren
    pd.drive_base.use_gyro(True)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(500, 400)
    yaw = Yaw(
        hub,
        pd.right_motor,
        pd.left_motor,
        min_velocity=100,
        max_velocity=600,
        acceleration=400,
    )
    yield True
    # drive to market
    pd.drive_base.straight(160)
    yield True
    yaw(90)
    yield True
    pd.drive_base.straight(1170)
    yield True
    yaw(0)
    yield True

    # solve scale
    pd.drive_base.straight(110)
    yield True
    yaw(0)
    yield True
    pd.drive_base.straight(-200)
    yield True
    yaw(4)
    yield True
    # turn gear
    pd.action_left.run_angle(700, -1500)
    yield True
    # drive to homebase
    pd.action_left.run_angle(700, 130, wait=False)
    yield True
    yaw(8)
    yield True
    pd.drive_base.straight(50)
    yield True
    # pd.drive_base.straight(-20)
    yaw(105)
    yield True
    pd.drive_base.settings(977, 700)
    yield True
    pd.drive_base.straight(800)
    yield True
    yield False
    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()


if __name__ == "__main__":
    for element in drive_across_new(PupDevices()):
        pass
