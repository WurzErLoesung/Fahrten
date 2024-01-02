from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import *
from math import *

#Ausrichtung 1 (Am Anfang von der Fahrt)
#Rote Base
#Gabelstapler unten
#L eingehängt
#Maxerl mit Kopf nach Süden und Vorderteil nach Westen laden
#x-Achse West-Ost, y-Achse Süd-Nord
#Räder nach Norden
#mitte vom linken Rad: x=2, y=10,5


#Ausrichtung 2 (In der Mitte von der Fahrt)
#Rote Base
#Gabelstapler unten
#L eingehängt
#Maxerl mit Kopf nach Süden und Vorderteil nach Westen laden
#x-Achse West-Ost, y-Achse Süd-Nord
#Räder nach Norden
#Mitte des rechten Rades: x = 14, y = 10,5

def yaw(target_yaw: int = 0):
    direction = min(1, max(-1, gyro.get_yaw_angle() - target_yaw))
    steering = 100*direction
    drive.start(steering, speed=8)
    wait_until(gyro.get_yaw_angle, equal_to, target_yaw + 4*direction)
    drive.stop()

def relative_yaw(yaw_step: int):
    yaw(gyro.get_yaw_angle() + yaw_step)

def drop_figure():
    action_front.run_for_rotations(-0.7, speed=80)
    wait_for_seconds(0.3)


#Initalizing
hub = PrimeHub()

drive_right = Motor ("A")
drive_left = Motor ("E")
action_front = Motor ("D")
action_back = Motor ("B")
drive = MotorPair("E", "A")
gyro = hub.motion_sensor
color = ColorSensor ("C")

gyro.reset_yaw_angle()

drive.set_stop_action("hold")
drive.set_default_speed(75) #Standard Schnelligkeit 75%

# 3d Kino
# drop_figure_time = 1.3
# drive.move(24,steering=36, speed=100) #Fährt zum Drachen
# drive.move(9, steering=-100, speed=80) #Löst den Drachen aus
# drive.move(-15, speed=100)


# wait_for_seconds(5) #neu Ausrichten für 2. Teil


drive.move(38, steering = -8, speed=70)#Fährt zu Popcorn
yaw()
drop_figure()
drive.move(17)
yaw(-45)
drive.move(15, speed=40)
drop_figure()
drive.move(-5.5)
wait_for_seconds(2.5)
drive.move(15, speed=40)
drive.move(-8)
yaw()
drive.move(-13, speed=70)
yaw(45)
drive.move(38, steering=-2)
drop_figure()
drive.move(-18)
yaw(90)
drive.move(45)
yaw(45)
drive.move(24)
yaw(90)
action_back.run_for_rotations(8)
drive.move(-3)
action_back.run_for_rotations(-9)
yaw()
drive.move(15)