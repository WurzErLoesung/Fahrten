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
watch = StopWatch()


#DriveBase initialisieren
wheel_diameter = 56 
axle_track = 113 
drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
drive_base.use_gyro(False) 
drive_base.settings(straight_speed=400, straight_acceleration=500)
StopWatch = watch
hub.speaker.beep()

drive_base.straight(130)
drive_base.straight(-105)

