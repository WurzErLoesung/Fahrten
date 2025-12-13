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


def trolley(pd):
    # DriveBase initialisieren
    pd.drive_base.use_gyro(True)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(700, 500)
    yaw = Yaw(
        hub,
        pd.right_motor,
        pd.left_motor,
        min_velocity=50,
        max_velocity=650,
        acceleration=500,
    )
    yield True

    # Drive to trolley
    pd.drive_base.straight(415)
    yield True
    yaw(65)
    yield True
    pd.drive_base.straight(410)  # 420
    yield True

    # Activate trolley
    yaw(12)  # 20
    yield True
    pd.drive_base.straight(-10)
    yield True
    pd.action_left.run_angle(-1000, 1450)
    yield True

    # Pick up artefact
    # yaw(10) #15
    pd.drive_base.straight(165)  # 155
    yield True
    pd.action_right.run_angle(2000, 1000)
    yield True
    pd.action_right.run_angle(-2000, 1000)
    yield True

    # Activate statue
    pd.drive_base.straight(-15)
    yield True
    pd.action_left.run_angle(500, 300)
    yield True
    pd.drive_base.straight(-110)
    yield True
    yaw(-45)
    yield True
    pd.drive_base.straight(25)
    yield True
    pd.action_left.run_angle(-500, 300)
    yield True
    pd.drive_base.straight(-40)
    yield True
    pd.action_left.run_angle(1050, 450)
    yield True
    yaw(-65)
    yield True
    pd.action_left.run_angle(1050, 450)
    yield True

    # Drive home
    pd.drive_base.settings(900, 500)
    yield True
    pd.drive_base.straight(30)
    yield True
    yaw(255)
    yield True
    pd.drive_base.straight(290)
    yield True
    yaw(200)
    yield True
    pd.drive_base.straight(720)
    yield True

    yield False
    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()


def test(pd):
    # DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(200, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    yield True

    yield False


if __name__ == "__main__":
    for element in trolley(PupDevices()):
        pass
    # for element in test(PupDevices()): pass
