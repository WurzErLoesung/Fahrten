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


async def forum(pd):
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
    await pd.drive_base.straight(200)
    await yaw(-21)
    await pd.drive_base.straight(550)
    await yaw(-80)
    await pd.drive_base.straight(275)
    await yaw(0)

    # Pick up cart
    await pd.drive_base.straight(90)
    await pd.action_right.run_angle(800, -1200)
    await pd.drive_base.straight(-70)

    # Drive to forum (using 2 "edges")
    await yaw(-80)
    await pd.drive_base.straight(350)
    await yaw(-115)
    await pd.drive_base.straight(400)
    await yaw(-180)

    # Drop contents into forum
    await pd.drive_base.straight(50)
    await multitask(task1(pd), task2(pd))
    await pd.drive_base.straight(-20)

    # Reset module and place flag
    await pd.drive_base.straight(-60)

    await yaw(-240)
    await pd.drive_base.straight(-110)

    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    watch.reset()
    return True

async def task1(pd):
    await pd.action_left.run_angle(100, -50)
    await pd.action_left.run_angle(100, 50)

async def task2(pd):
    await pd.action_right.run_angle(800, 2900)

if __name__ == "__main__":
    run_task(forum(PupDevices()))
