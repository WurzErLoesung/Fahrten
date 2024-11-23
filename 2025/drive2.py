from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask


hub = PrimeHub()
# Motoren initialisieren 
left_motor = Motor(Port.E, positive_direction=Direction.CLOCKWISE) 
right_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)

action_front = Motor(Port.D)
action_back = Motor(Port.A)

ultra = UltrasonicSensor(Port.E)
color = ColorSensor(Port.D)



#DriveBase initialisieren
wheel_diameter = 56 
axle_track = 113 
drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
drive_base.use_gyro(True) 
drive_base.settings(straight_speed=900, straight_acceleration=500)

hub.speaker.beep()

drive_base.settings(900)

async def drive_forward():
    await drive_base.straight(250)

async def action(degree, speed):
    await action_back.run_angle(speed, degree)

# async def main1():
#     await multitask( drive_forward(), action(360, 500))
# run_task(main1())
#


multitask( drive_forward(), action(360, 500))

