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
    await db.straight(668)
    await yaw(-47) #vorher 48
    #await db.turn(1440) #für den flex
    #await yaw(-46) # 2. teil des flex (funktiert aber nicht)
    db.settings(200,200)
    await db.straight(270)
    await yaw(-95)
    await pd.action_right.run_angle(500, 45) #55 + 45 sagt Simon + 40 sagt Tkeo + Kompromiss 45
    await db.straight(-42) #47
    await pd.action_right.run_angle(500, 200)
    await yaw(178) #-182
    db.settings(*DRIVE)
    await db.straight(825)
    #await yaw(-80) #sicherheitsfahrt premium, falls er zu weit rechts ist (muss man nicht machen)
    #await db.straight(200) 
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
