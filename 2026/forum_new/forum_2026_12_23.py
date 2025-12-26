from pupdevices import PupDevices
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import (ColorSensor, ForceSensor, Motor, UltrasonicSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, run_task, wait, multitask
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

    # Drive to cart
    pd.drive_base.straight(200)
    yield True
    yaw(-21)
    yield True
    pd.drive_base.straight(550)
    yield True
    yaw(-80)
    yield True
    pd.drive_base.straight(275)
    yield True
    yaw(0)
    yield True

    # Pick up cart
    pd.drive_base.straight(90)
    yield True
    pd.action_right.run_angle(800, -1200)
    yield True
    pd.drive_base.straight(-70)
    yield True

    # Drive to forum (using 2 "edges")
    yaw(-80)
    yield True
    pd.drive_base.straight(350)
    yield True
    yaw(-115)
    yield True
    pd.drive_base.straight(400)
    yield True
    yaw(-180)
    yield True

    # Drop contents into forum
    pd.drive_base.straight(50)
    yield True
    run_task(task(pd))
    yield True
    pd.drive_base.straight(-20)
    yield True

    # Reset module and place flag
    pd.drive_base.straight(-60)
    # pd.action_right.run_angle(800, -1650)

    yaw(-240)
    pd.drive_base.straight(-110)

    # yaw(-80)
    # pd.drive_base.straight(175)
    # yaw(-180)
    # pd.drive_base.straight(120)

    yield False
    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    watch.reset()

async def task(pd):
    await multitask(task1(pd), task2(pd))

async def task1(pd):
    await pd.action_left.run_angle(100, -50)
    await pd.action_left.run_angle(100, 50)

async def task2(pd):
    await pd.action_right.run_angle(800, 2900)



if __name__ == "__main__":
    for element in forum(PupDevices()):
        pass

