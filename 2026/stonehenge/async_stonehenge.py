from pupdevices import PupDevices
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import (ColorSensor, ForceSensor, Motor,
                                 UltrasonicSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, run_task, multitask, wait
from yaw import Yaw

hub = PrimeHub()
print(f"{hub.system.name()}: {hub.battery.voltage()} mV")
print(f"{hub.system.name()}: {hub.battery.current()} mA")
watch = StopWatch()

async def stonehenge(pd):
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(straight_speed=777, straight_acceleration=700)
    yaw = Yaw(
        hub,
        pd.right_motor,
        pd.left_motor,
        min_velocity=100,
        max_velocity=400,
        acceleration=300,
    )

    # driving to stonehenge
    await pd.drive_base.straight(40) # BEFORE: 50
    yaw(-13)  # -18
    await pd.drive_base.straight(590)  # BEFORE: 555 # 550 553
    yaw(45)  # 43 45 42
    await pd.drive_base.straight(430) # 300 (20.12.)

    # solving everything
    await multitask(solve1(pd), solve2(pd))

    await pd.drive_base.arc(370, angle=-145) # 450

    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()
    return True

async def solve1(pd):
    await pd.action_right.run_angle(-1200, 7500)

async def solve2(pd):
    await pd.action_left.run_angle(590, -1250) # -610 -690 -820 -850 (20.12.)
    await pd.action_left.run_angle(600, 1480)  # 1470
    await wait(1500)
    await pd.action_left.run_angle(600, -250)  # -200


if __name__ == "__main__":
    run_task(stonehenge(PupDevices()))
