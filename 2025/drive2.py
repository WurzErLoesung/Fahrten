from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from action_arc import action_arc
from yaw import Yaw

hub = PrimeHub()
# Motoren initialisieren
left_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE) 
right_motor = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)

action_front = Motor(Port.C)
action_back = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)

ultra = UltrasonicSensor(Port.E)
color = ColorSensor(Port.D)

yaw = Yaw(hub, left_motor, right_motor)

watch = StopWatch()

#DriveBase initialisieren
wheel_diameter = 56
axle_track = 113
drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
drive_base.use_gyro(False)
drive_base.settings(straight_speed=900, straight_acceleration=500)
StopWatch = watch
hub.speaker.beep()

#Korallenbaum
drive_base.straight(192)
action_back.run_angle(500, 250)
#action_arc(drive_base, -1, action_back, 27, 200, 90, 30, 15)
action_arc(drive_base, -1, action_back, 20, 182, 90, 30, 20)
action_back.run_angle(500, -430)
drive_base.straight(-95)

#zu Schiffwrack
yaw(-135)
drive_base.straight(-302)
#drive_base.turn(-57)
yaw(-90)
drive_base.settings(100)
drive_base.straight(-193)
action_front.run_angle(1000, 70)
drive_base.straight(-55)
action_front.run_angle(1000, -90)
drive_base.straight(150)
drive_base.settings(900)

#Korallenbaum Teil 2
drive_base.turn(-7)
drive_base.straight(125)
drive_base.straight(-80)
yaw(0)

#Hai und Taucherin
drive_base.straight(170)
yaw(-73)
action_back.run_angle(1250, -160)
drive_base.straight(200)

print("Fahrt 2 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
watch.reset()

