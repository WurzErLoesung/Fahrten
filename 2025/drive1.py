from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task


hub = PrimeHub()
# Motoren initialisieren
left_motor = Motor(Port.E, positive_direction=Direction.CLOCKWISE)
right_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)

action_front = Motor(Port.D)

#DriveBase initialisieren
wheel_diameter = 56 
axle_track = 113 
drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
drive_base.use_gyro(True) 
drive_base.settings(straight_speed=900, straight_acceleration=500)

hub.speaker.beep()

drive_base.settings(900)

#zu unbekanntem Wesen
drive_base.straight(195)
drive_base.turn(-47)
drive_base.settings(300)

#unbekanntes Wesen auslösen
drive_base.straight(400)
drive_base.settings(900)
drive_base.straight(-300)

#3 Schrimps + 1 Alge einsammeln
drive_base.turn(18)
#1. Schrimps
drive_base.straight(130)
drive_base.turn(40)
#Alge
drive_base.straight(110)
drive_base.turn(-25)
#2. Schrimps
drive_base.straight(140)
drive_base.settings(turn_rate=40)
drive_base.turn(40)
drive_base.settings(900)
#3. Schrimps
drive_base.straight(120)
drive_base.turn(-145)
#Algenprobe
drive_base.straight(70)
action_front.run_angle(80, 200)
drive_base.straight(-140)
action_front.run_angle(80, -100)
drive_base.straight(70)
action_front.run_angle(80, -150)
drive_base.turn(10)
drive_base.straight(60)
drive_base.turn(45)
#zu Anglerfich
drive_base.turn(-10)
drive_base.straight(500)
drive_base.turn(-55)
drive_base.curve(200, 40)
#zu Wasserprobe
drive_base.straight(300)
drive_base.turn(-10)
drive_base.straight(70)
#zu Meeresbodenprobe
drive_base.straight(200)
drive_base.turn(-30)
action_front.run_angle(80, 75)
drive_base.straight(-300)
action_front.run_angle(80, -150)