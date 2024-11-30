from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask


hub = PrimeHub()
# Motoren initialisieren 
left_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE) 
right_motor = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)

action_front = Motor(Port.C)
action_back = Motor(Port.A)

ultra = UltrasonicSensor(Port.E)
color = ColorSensor(Port.D)



#DriveBase initialisieren
wheel_diameter = 56 
axle_track = 113 
drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
drive_base.use_gyro(False) 
drive_base.settings(straight_speed=900, straight_acceleration=500)

#hub.speaker.beep()

drive_base.settings(190)

async def drive_forward(n):
    await drive_base.straight(n)

async def action(speed,degree):
    await wait(1040)
    await action_back.run_angle(speed, degree)
    
async def main1():
    await multitask(drive_forward(440), action(1250, -5000), race=False)
run_task(main1())


drive_base.straight(-200)
