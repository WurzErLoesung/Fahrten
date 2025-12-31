from pupdevices import PupDevices
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import (ColorSensor, ForceSensor, Motor,
                                 UltrasonicSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, run_task, wait
from yaw import Yaw

hub = PrimeHub()
print(f"{hub.system.name()}: {hub.battery.voltage()} mV")
print(f"{hub.system.name()}: {hub.battery.current()} mA")
watch = StopWatch()
hub.speaker.beep()

async def crane(pd):
    # DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(-90)
    pd.drive_base.settings(400, 500)

    yaw = Yaw(
        hub,
        pd.right_motor,
        pd.left_motor,
        min_velocity=40,
        max_velocity=600,
        acceleration=700,
    )

    await pd.drive_base.straight(630)
    yaw(-110)
    await pd.drive_base.straight(160)
    yaw(-91.5)
    await pd.action_left.run_time(-1000, 1100)
    yaw(-170)
    await pd.drive_base.straight(-105)
    await pd.drive_base.straight(150)
    yaw(-120)
    await pd.drive_base.straight(-330)
    await pd.drive_base.straight(150)
    yaw(-74)
    pd.drive_base.settings(700, 700)
    await pd.drive_base.straight(-570)
    
    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()
    return True


if __name__ == "__main__":
    run_task(crane(PupDevices()))
