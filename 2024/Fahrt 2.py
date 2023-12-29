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

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import *
from math import *

def yaw(target_yaw: int = 0):
    direction = min(1, max(-1, gyro.get_yaw_angle() - target_yaw))
    steering = 100*direction
    drive.start(steering, speed=10)
    wait_until(gyro.get_yaw_angle, equal_to, target_yaw)
    drive.stop()

def relative_yaw(yaw_step: int):
    yaw(gyro.get_yaw_angle() + yaw_step)





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

drive.set_stop_action("brake")
drive.set_default_speed(75) #Standard Schnelligkeit 50%

# 3d Kino
# drop_figure_time = 1.3
# drive.move(24,steering=36, speed=100)
# drive.move(9, steering=-100, speed=80)
# yaw(0)
# drive.move(-15, speed=100)


# wait_for_seconds(5)


drive.move(37, steering = -9, speed=70)#Fährt zu Popcorn
drive_left.run_for_rotations(-0.1)
action_front.run_for_rotations(-0.7)
drive.move(30, steering=36, speed=70)
drive.move(-5)
wait_for_seconds(0.5)
drive.move(9)
drive.move(-5)
drive.move(-10, steering=70)
drive.move(10, steering=-20, speed=60)
relative_yaw(45)
drive.move(20, steering=-30)
action_front.run_for_rotations(-0.6)
drive.move(10, steering=-30, speed=50)
drive.move(15, steering=-35, speed=70)
drive.move(22, steering=-40)
action_front.run_for_rotations(-0.6)
action_front.run_for_rotations(2.5)
action_front.run_for_rotations(-1.1)
action_front.run_for_rotations(1.1)
action_back.run_for_rotations(7)


# drive.move(20, steering=-50, speed=70)


# drive.move(5, steering=-100, speed=50)
# drive.move(30, steering=-50)
# action_front.run_for_rotations(-0.6)
# drive.move(6, steering=-100)
# action_back.run_for_rotations(3)

