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

hub.speaker.beep()

drive_base.settings(250)

# zu der/die/das Kaktus
drive_base.straight(590)
drive_base.settings(950)
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

#zu Karotte
drive_base.turn(-120)
drive_base.straight(120)
action_back.run_angle(200, 190)
drive_base.straight(-55)
action_back.run_angle(200, -70)
drive_base.straight(200)
action_back.run_angle(200, -100)

#zu Anglerfisch
drive_base.turn(-11)
drive_base.straight(445)

# eingesammelte Sachen abstellen
drive_base.turn(15)
drive_base.straight(300)
drive_base.turn(-15)
drive_base.straight(210)

#zu Bodenprobe
drive_base.turn(-25)

action_back.run_angle(300, 83)

drive_base.straight(-210)
action_back.run_angle(200, -90)
drive_base.straight(310)
drive_base.turn(-32)

#zurück in rote Base
drive_base.straight(510)
drive_base.turn(23)
drive_base.straight(300)
hub.speaker.beep()


