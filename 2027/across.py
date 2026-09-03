"""Mission template."""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Stop
from pybricks.tools import StopWatch, multitask, run_task, wait

from pupdevices import PupDevices
from yaw import Yaw

MAX_VOLTAGE = 7000
USE_GYRO = True
DRIVE = (500, (400, 400), 300, (500, 500))   # speed, accel, turn_rate, turn_accel
FAST = (977, 977)
YAW = dict(
    min_velocity=50,
    max_velocity=500,
    acceleration=800,
    stop_action=Stop.BRAKE,
)


async def delayed(ms, make_coro):
    """Start make_coro() only after ms milliseconds. Pass a lambda, not a call."""
    await wait(ms)
    await make_coro()


async def mission(pd, yaw):
    db, arm = pd.drive_base, pd.action_left
    watch = StopWatch()

    db.settings(*DRIVE)

    # ---------
    await db.straight(350)
    await yaw(50)
    await db.straight(350)
    await yaw(100)
    await db.straight(200)
    await yaw(110)
    await db.straight(130)
    await yaw(90)
    db.settings(*FAST)
    await db.straight(150)
    db.settings(*DRIVE)
    await multitask(pd.action_left.run_angle(500, 250), pd.action_right.run_angle(-200, 110))
    await multitask(pd.action_left.run_angle(-300, 250), pd.action_right.run_angle(300, 110))
    await multitask(db.straight(-110), delayed(200, lambda: pd.action_right.run_angle(-300, 150)))
    await yaw(30)
    await multitask(db.straight(305), pd.action_right.run_angle(300, 150))
    await yaw(90)
    await db.straight(425)
    await yaw(45)
    db.settings(320, 270)
    await db.straight(200) # 165 #scheiß ameise
    await db.straight(-80)
    db.settings(250, 250)
    await db.straight(220)
    db.settings(*DRIVE)
    await db.straight(-150)
    await yaw(98)
    await db.straight(165)
    await yaw(0)
    await pd.action_right.run_angle(-300, 55)
    await db.straight(-110)
    await pd.action_right.run_angle(300, 55)
    await db.straight(50)
    await pd.action_right.run_angle(300, 55)
    await db.straight(-150)
    await yaw(-30)
    await db.straight(-680)
    # ---------

    print("Run took " + str(watch.time() / 1000) + " seconds.")


def main():
    hub = PrimeHub()
    print(f"{hub.system.name()}: {hub.battery.voltage()} mV")
    hub.speaker.beep()

    pd = PupDevices()
    pd.left_motor.settings(max_voltage=MAX_VOLTAGE)
    pd.right_motor.settings(max_voltage=MAX_VOLTAGE)

    hub.imu.reset_heading(0)
    pd.drive_base.use_gyro(USE_GYRO)

    yaw = Yaw(hub, pd.right_motor, pd.left_motor, **YAW)

    try:
        run_task(mission(pd, yaw))
    finally:
        pd.drive_base.stop()
        #hub.speaker.beep(1000, 100)


if __name__ == "__main__":
    main()
