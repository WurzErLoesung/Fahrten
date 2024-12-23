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
action_back = Motor(Port.A)

ultra = UltrasonicSensor(Port.E)
color = ColorSensor(Port.D)
watch = StopWatch()
yaw = Yaw(hub, left_motor, right_motor)

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

wait(10000)

#Boot hinschieben
drive_base.settings(100)
drive_base.straight(200)
drive_base.settings(300)
drive_base.straight(700)

#Krabben aufstellen
drive_base.straight(-225)
action_back.run_angle(360, 360)
drive_base.straight(-100)
drive_base.settings(900)

#zu blauer Base
yaw(-30)
drive_base.straight(-50)
action_front.run_angle(1250, 850) #Schieber abwerfen
drive_base.straight(350)
yaw(5)
drive_base.straight(900)

print("Fahrt 2 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
watch.reset()
