from pupdevices import PupDevices
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import (ColorSensor, ForceSensor, Motor, UltrasonicSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, run_task, wait, multitask
from yaw import Yaw

hub = PrimeHub()
print(f"{hub.system.name()}: {hub.battery.voltage()} mV")
print(f"{hub.system.name()}: {hub.battery.current()} mA")
watch = StopWatch()
hub.speaker.beep()


async def artifact(pd):
    # DriveBase initialisieren
    pd.drive_base.use_gyro(True)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(700, 500)  # 700, 500
    yaw = Yaw(
        hub,
        pd.right_motor,
        pd.left_motor,
        min_velocity=100,
        max_velocity=500,
        acceleration=300,
    )  # 100, 500, 600

    
    # Drive goes here

    await pd.straight(300)
    await yaw(25)
    await pd.straight(470)

    await multitask(prepare1(pd), prepare2(pd, yaw))
    await pd.action_right.run_angle(800, 1700)
    await pd.action_left.run_angle(400, 1100)
    await pd.action_left.run_angle(-400, 200)
    await pd.action_right.run_angle(-800, 1700)

    await pd.straight(-150)
    await yaw(21)
    await pd.drive_base.arc(1500, angle=-30)


    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    watch.reset()
    return True

async def prepare1(pd):
    await pd.action_left.run_angle(-800, 800)
    
async def prepare2(pd, yaw):
    await yaw(0)
    await pd.straight(220) #170
    await pd.straight(-20)

if __name__ == "__main__":
    run_task(artifact(PupDevices()))
   
    # PupDevices().action_left.run_angle(-400, 500)
    # for element in artifact(PupDevices()):
        # pass

