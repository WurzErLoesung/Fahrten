from pupdevices import PupDevices
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import (ColorSensor, ForceSensor, Motor,
                                 UltrasonicSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, run_task, wait
from yaw import Yaw

hub = PrimeHub()
print(f"{hub.battery.voltage()/1000} Volt")
watch = StopWatch()
hub.speaker.beep()


async def ship(pd):
    # DriveBase initialisieren
    pd.drive_base.use_gyro(True)
    pd.imu.reset_heading(90)
    pd.drive_base.settings(500, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)

    await pd.drive_base.arc(4200, distance=550, wait=True)
    pd.action_left.run_angle(700, -70)
    pd.action_left.run_angle(700, 50, wait=True)
    pd.drive_base.settings(977, 977)
    await wait(50)
    await pd.drive_base.straight(-600)

    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    # print(pd.timer.time())
    watch.reset()
    return True


if __name__ == "__main__":
    run_task(ship(PupDevices()))
