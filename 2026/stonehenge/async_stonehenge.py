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
    pd.drive_base.settings(straight_speed=400, straight_acceleration=300)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)

    # driving to stonehenge
    await pd.drive_base.straight(50) # BEFORE: 50
    await yaw(-14)  # -18
    await pd.drive_base.straight(570)  # BEFORE: 555 # 550 553
    await yaw(43)  # 43 45 42
    await pd.drive_base.straight(270) # 300 (20.12.)

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
    await pd.action_left.run_angle(400, -500) # -610 -690 -820 -850 (20.12.)
    await pd.action_left.run_angle(600, 800)  # 1470
    await wait(1500)
    await pd.action_left.run_angle(600, -20)  # -200


if __name__ == "__main__":
    run_task(stonehenge(PupDevices()))
