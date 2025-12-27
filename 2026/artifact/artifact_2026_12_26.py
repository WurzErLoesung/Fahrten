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


def artifact(pd):
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

    pd.straight(300)
    yaw(25)
    pd.straight(440)

    run_task(prepare(pd, yaw))
    pd.action_right.run_angle(800, 1400)
    pd.action_left.run_angle(-400, 600)
    pd.action_left.run_angle(400, 200)
    pd.action_right.run_angle(-800, 1400)

    pd.straight(-150)
    yaw(20)
    pd.drive_base.arc(1500, angle=-30)


    yield False
    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    watch.reset()

async def prepare(pd, yaw):
    await multitask(prepare1(pd), prepare2(pd, yaw))

async def prepare1(pd):
    await pd.action_left.run_angle(800, 500)
    
async def prepare2(pd, yaw):
    yaw(0)
    await pd.straight(170)
    await pd.straight(-15)

if __name__ == "__main__":
   # PupDevices().action_left.run_angle(-400, 500)
    for element in artifact(PupDevices()):
        pass

