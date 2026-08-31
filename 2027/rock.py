from pybricks.hubs import PrimeHub
from pybricks.tools import StopWatch, multitask, run_task, wait

from pupdevices import PupDevices

MAX_VOLTAGE = 7000
USE_GYRO = True
DRIVE = (700, (500, 400), 400, (700, 500))   # speed, accel, turn_rate, turn_accel


async def delayed(ms, second_thing):
    """Start second_thing() only after ms milliseconds. Pass a lambda, not a call."""
    await wait(ms)
    await second_thing()


async def rock(pd):
    db, arm = pd.drive_base, pd.action_left
    watch = StopWatch()

    db.settings(*DRIVE)

    # ---------
    await multitask(
        db.straight(500),
        delayed(500, lambda: arm.run_angle(170, -300)),
    )

    db.settings(977, 977)
    await db.straight(-100)

    await multitask(
        arm.run_angle(400, 200),
        delayed(200, lambda: db.straight(110)),
    )
    await pd.action_left.run_angle(400, -200)
    await db.straight(-500)
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

    try:
        run_task(rock(pd))
    finally:
        pd.drive_base.stop()
        #hub.speaker.beep(1000, 100)


if __name__ == "__main__":
    main()
