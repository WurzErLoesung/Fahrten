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
pd=PupDevices()
db = pd.drive_base

async def rock(pd):
    db = pd.drive_base
    db.use_gyro(True)
    hub.imu.reset_heading(0)
    db.settings(700, (500, 400), 400, (700, 500))
    watch.reset()

    async def arm():
        await wait(500)
        await pd.action_left.run_angle(170, -300)

    await multitask(db.straight(500), arm())    
    db.settings(977,977)
    await db.straight(-100)
    async def arm2():
        await wait(200)
        db.straight(110)

    await multitask(pd.action_left.run_angle(400, 200), arm2())
    #await pd.action_left.(300, -300)
    await db.straight(-100)

    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    return True


if __name__ == "__main__":
    pd = PupDevices()
    pd.left_motor.settings(max_voltage=7000)
    pd.right_motor.settings(max_voltage=7000)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor, min_velocity=50,
              max_velocity=500, acceleration=800, stop_action=Stop.BRAKE)
    run_task(rock(pd))
