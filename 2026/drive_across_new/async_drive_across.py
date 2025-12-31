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


async def drive_across_new(pd):
    # DriveBase initialisieren
    pd.drive_base.use_gyro(True)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(600, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    
    # bring 3 items to forum
    await pd.drive_base.straight(190)
    yaw(51)
    await pd.drive_base.straight(330) #335
    await pd.drive_base.straight(-250)
    yaw(90)
    await pd.drive_base.straight(750)
    pd.action_right.run_angle(700, 455) # wait=False
    yaw(141)
    await pd.drive_base.straight(-90) #-85
    await pd.action_right.run_angle(600, -500)
    yaw(45)
    await pd.drive_base.straight(200) #220
    await pd.drive_base.straight(-280) #-300
    yaw(112)
    pd.drive_base.settings(900, 900)
    await pd.drive_base.straight(1050)

    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()
    return True


if __name__ == "__main__":
    run_task(drive_across_new(PupDevices()))
