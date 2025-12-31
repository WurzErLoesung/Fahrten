from pupdevices import PupDevices
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import (ColorSensor, ForceSensor, Motor,
                                 UltrasonicSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, multitask, run_task, wait
from yaw import Yaw

hub = PrimeHub()
print(f"{hub.system.name()}: {hub.battery.voltage()} mV")
print(f"{hub.system.name()}: {hub.battery.current()} mA")
watch = StopWatch()
hub.speaker.beep()


def brush_new(pd):
    # DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(950, 700)
    yaw = Yaw(
        hub,
        pd.right_motor,
        pd.left_motor,
        min_velocity=50,
        max_velocity=500,
        acceleration=800,
    )

    pd.drive_base.straight(100)
    yield True
    yaw(14.5)
    yield True
    print(pd.hub.imu.heading())
    pd.drive_base.straight(520)
    yield True
    yaw(-90)
    yield True
    pd.drive_base.straight(150)
    yield True

    run_task(multitask(do_brush(pd), do_rest(pd)))
    yield True

    pd.drive_base.straight(-110)
    yield True
    yaw(20)
    yield True
    pd.drive_base.straight(-620)
    yield True

    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()
    yield False


async def do_brush(pd):
    await pd.action_left.run_angle(1000, -350)
    yield True
    await pd.action_left.run_angle(800, 300)
    yield True


async def do_rest(pd):
    await pd.action_right.run_angle(300, 260)
    yield True
    await pd.action_right.run_angle(600, -970)
    yield True
    await pd.action_right.run_angle(800, 450)
    yield True


def test(pd):
    # DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(200, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)


if __name__ == "__main__":
    brush_new(PupDevices())
    # for element in brush_new(PupDevices()): pass
