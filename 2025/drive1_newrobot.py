from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task


hub = PrimeHub()
# Motoren initialisieren
left_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, positive_direction=Direction.CLOCKWISE)

action_front = Motor(Port.C)
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

drive_base.settings(270)

# zu unbekanntem Wesen
drive_base.straight(590)
drive_base.settings(900)
action_back.run_angle(200, -170)

#zu 1. Schrimm & Koralle
drive_base.straight(-200)
drive_base.turn(75)
drive_base.straight(200)

#2. Schrims
drive_base.turn(-30)
drive_base.straight(180)
drive_base.turn(35)
drive_base.straight(70)

#zu Algenprobe
drive_base.turn(-120)
drive_base.straight(120)
action_back.run_angle(200, 190)
drive_base.straight(-55)
action_back.run_angle(200, -70)
drive_base.straight(200)
action_back.run_angle(200, -100)

#zu Anglerfisch
drive_base.turn(-10)
drive_base.straight(435)

# eingesammelte Sachen abstellen
drive_base.turn(15)
drive_base.straight(300)
drive_base.turn(-15)
drive_base.straight(210)
drive_base.turn(-28)
action_back.run_angle(300, 80)
drive_base.straight(-210)
action_back.run_angle(200, -90)
drive_base.straight(300)
drive_base.turn(-30)

drive_base.straight(500)
drive_base.turn(20)
drive_base.straight(300)
