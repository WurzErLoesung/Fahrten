from pupdevices import PupDevices
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import (ColorSensor, ForceSensor, Motor,
                                 UltrasonicSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, run_task, wait
from yaw import Yaw

hub = PrimeHub()
print(f"{hub.system.name()}: {hub.battery.voltage()} mV")
print(f"{hub.system.name()}: {hub.battery.current()} mA")
watch = StopWatch()
hub.speaker.beep()


def forum(pd):
    # DriveBase initialisieren
    pd.drive_base.use_gyro(True)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(700, 500)  # 700, 500
    yaw = Yaw(
        hub,
        pd.right_motor,
        pd.left_motor,
        min_velocity=100,
        max_velocity=500,
        acceleration=600,
    )  # 100, 500, 600

    # Zu Trolley fahren und aufheben
    pd.drive_base.straight(20)
    yield True
    yaw(-19)
    yield True
    pd.drive_base.straight(700)
    yield True
    yaw(-63)
    yield True
    pd.drive_base.straight(145)
    yield True
    yaw(-90)
    yield True
    pd.drive_base.straight(110)
    yield True
    # yaw(-30)
    # pd.drive_base.straight(-20)
    # yaw(-50)
    # pd.drive_base.straight(-90, wait=False)
    # start = watch.time()
    # while not pd.drive_base.done():
    # if watch.time() - start > 1000:
    # pd.drive_base.stop()
    # yaw(-55)
    # pd.drive_base.straight(110)
    # yaw(0)
    yaw(0)
    yield True
    pd.drive_base.straight(120)
    yield True
    pd.action_right.run_angle(800, -1200)
    yield True
    # Zu Forum fahren und abladen
    pd.drive_base.straight(-120)
    yield True
    yaw(-90)
    yield True
    pd.drive_base.straight(465)
    yield True

    yaw(-104)
    yield True
    pd.drive_base.straight(260)
    yield True
    yaw(180)
    yield True
    pd.drive_base.straight(60)
    yield True

    pd.action_left.run_angle(100, -50)
    yield True
    pd.drive_base.straight(-50)
    yield True
    pd.action_right.run_angle(800, 2850)
    yield True
    pd.drive_base.straight(80)
    yield True
    pd.drive_base.straight(-60)
    yield True
    pd.action_right.run_angle(800, -3000, wait=False)
    yield True

    yaw(-90)
    yield True
    pd.drive_base.straight(145)  # 150
    yield True
    yaw(-180)
    yield True
    pd.drive_base.straight(30)
    yield True

    yield False
    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    watch.reset()


def test(pd):
    # DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(200, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    yield True


if __name__ == "__main__":
    for element in forum(PupDevices()):
        pass
