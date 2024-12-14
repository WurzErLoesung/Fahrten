from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from arc import action_arc


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
drive_base.settings(straight_speed=900, straight_acceleration=500)
StopWatch = watch
hub.speaker.beep()

drive_base.settings(150)

drive_base.straight(230)
action_back.run_angle(1250, -1000)
drive_base.straight(90)
action_back.run_angle(1250, -650)
drive_base.straight(45)
action_back.run_angle(1250, -515)
drive_base.turn(-5)
drive_base.straight(60)
action_back.run_angle(1250, 500)
drive_base.straight(-200)
action_back.run_angle(1250, 1750)

print("Fahrt 1 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
watch.reset()
