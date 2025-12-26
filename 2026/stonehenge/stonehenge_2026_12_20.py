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

hub.speaker.beep()


def stonehenge(pd):
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(straight_speed=777, straight_acceleration=700)
    yaw = Yaw(
        hub,
        pd.right_motor,
        pd.left_motor,
        min_velocity=100,
        max_velocity=400,
        acceleration=500,
    )
    yield True

    # driving to stonehenge
    pd.drive_base.straight(40) # BEFORE: 50
    yield True
    yaw(-15)  # -18
    yield True
    pd.drive_base.straight(590)  # BEFORE: 555 # 550 553
    yield True

    # yaw(0)
    # yield True
    # pd.drive_base.straight(40)
    # yield True

    yaw(43)  # 45 42
    yield True
    pd.drive_base.straight(400) # 300 (20.12.)
    yield True
    

    # solving everything
    run_task(solve(pd))
    yield True

    pd.drive_base.arc(450, angle=-140)
    yield end(pd)
    return


    # driving back to homebase
    pd.drive_base.straight(-240)
    yield True

    # yaw(10)
    # yield True
    # pd.drive_base.straight(-40)
    # yield True

    yaw(0)
    yield True
    pd.drive_base.straight(-330) # -400
    yield True
    yaw(-45)
    yield True
    pd.drive_base.straight(-400)
    yield True

    yield False
    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()

def end(pd):
    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()
    yield False

async def solve(pd):
    await multitask(solve1(pd), solve2(pd))

async def solve1(pd):
    await pd.action_right.run_angle(-1200, 7500)

async def solve2(pd):
    await pd.action_left.run_angle(590, -1250) # -610 -690 -820 -850 (20.12.)
    await pd.action_left.run_angle(600, 1480)  # 1470
    await wait(1500)
    await pd.action_left.run_angle(600, -250)  # -200


if __name__ == "__main__":
    #run_task(solve1(PupDevices()))
    for element in stonehenge(PupDevices()): pass

