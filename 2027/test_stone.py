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
pd = PupDevices()

ADJUST = 20
ANGLE1 = 270
SLEEP = 270 # 340
ANGLE2 = 70
SPEED2 = 1800
DRIVE = 80

async def rotate(pd):
    await wait(SLEEP)
    await pd.action_left.run_angle(SPEED2, -ANGLE2)

async def drive(pd, distance):
    await pd.straight(distance)

async def activate_stone(pd):
    await pd.straight(ADJUST)
    await pd.straight(-10)
    await pd.action_left.run_angle(400, -ANGLE1)
    await multitask(drive(pd, -DRIVE), rotate(pd))

async def reset(pd):
    await pd.action_left.run_angle(1000, ANGLE1 + ANGLE2)
    await pd.straight(DRIVE)

async def main(pd):
    await activate_stone(pd)
    await reset(pd)
    await activate_stone(pd)
    await pd.action_left.run_angle(1000, ANGLE1 + ANGLE2)
    await pd.straight(-300)

run_task(main(pd))




# pd.db
# multit
