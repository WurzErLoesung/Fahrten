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
    await multitask(db.straight(450), delayed(500, lambda: pd.action_left.run_angle(170, -200)))
    await multitask(db.straight(-160), pd.action_left.run_angle(250, -100))
    await pd.action_left.run_angle(500, 300)
    await yaw(-1)
    await wait(50)
    await multitask(db.straight(167), pd.action_left.run_angle(200, -200))
    await multitask(db.straight(-550), pd.action_left.run_angle(300, -105))
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
