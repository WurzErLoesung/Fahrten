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


async def drive_across(pd):
    # DriveBase initialisieren
    pd.drive_base.use_gyro(True)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(500, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    
    # bring 3 items to forum
    await pd.drive_base.straight(190)
    await yaw(51)
    await pd.drive_base.straight(345) #330
    await pd.drive_base.straight(-250)
    await yaw(90) 
    await pd.drive_base.straight(765)
    """
    pd.drive_base.drive(500, 0)
    while True:
        reflection = await pd.color_bottom.reflection()  # <<< wichtig
        if reflection < 20:
            pd.drive_base.stop()
            break
        await wait(10)
    """
    #await pd.drive_base.straight(-20)
    pd.action_right.run_angle(600, 455) # wait=False
    await yaw(139) #141
    await pd.drive_base.straight(-135) #-90 #110
    yaw(153.5)
    await pd.action_right.run_angle(450, -700)
    await pd.drive_base.straight(30)
    await yaw(45) #45
    await pd.drive_base.straight(230) #220
    await pd.drive_base.straight(-280) #-300
    await yaw(102) #112
    pd.drive_base.settings(900, 900)
    await pd.drive_base.straight(1050)

    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()
    return True


if __name__ == "__main__":
    run_task(drive_across(PupDevices()))
