from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import *
from math import *

#Ausrichtung 1 (Am Anfang von der Fahrt)
#Rote Base
#Gelbe Wand unten
#L eingehängt
#Maxerl mit Rücken nach Oben und Kopf nach Süden in den Schacht einlegen
#Schacht-Piston einmal ganz zurück ziehen
#x-Achse West-Ost, y-Achse Süd-Nord
#Räder nach Norden
#mitte vom linken Rad: x=2, y=10,5


#Ausrichtung 2 (In der Mitte von der Fahrt)
#Rote Base
#Gelbe Wand oben
#L ausgehängt
#Maxerl mit Kopf nach Oben und Osten in den Schacht einlegen
#Schacht-Piston einmal ganz zurück ziehen
#x-Achse West-Ost, y-Achse Süd-Nord
#Räder nach Norden
#Mitte des rechten Rades: x = 14, y = 10.5
#NPC-Yeeter 3000 mit Desinfektionsmittel einschmieren

def yaw(target_yaw: int = 0):
    direction = min(1, max(-1, (gyro.get_yaw_angle() - target_yaw + 180) % 360 - 180))# Wählt für alle Gradzahlen unter dem target_yaw -1, für alle Zahlen darüber +1 aus
    steering = 100*direction
    drive.start(steering, speed=15)
    wait_until(gyro.get_yaw_angle, equal_to, target_yaw)
    drive.stop()

def relative_yaw(yaw_step: int):
    yaw(gyro.get_yaw_angle() + yaw_step)

def drop_figure():
    action_front.run_for_seconds(0.7 ,speed=100)
    wait_for_seconds(0.2)
    action_front.run_for_seconds(0.7 ,speed=-100)
    wait_for_seconds(0.2)

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
# drive.move(24,steering=36, speed=100) #Fährt zum Drachen
# drive.move(9, steering=-100, speed=80) #Löst den Drachen aus
# drive.move(-15, speed=100)


# wait_for_seconds(5) #neu Ausrichten für 2. Teil

# Drives to Popcorn and drops spectator
drive.move(30, steering = -8, speed=70)
yaw()
drop_figure()

# Drives to Scene Switch and activates it
drive.move(35, steering=8)
yaw(-45)
drive.move(7, speed=40)
drive.move(-5)
yaw(-45)

# Drops spectator and activates Scene Switch if color-sensor senses yellow
drop_figure()
if color.get_color() == 'yellow':
    # yaw(-45)
    drive.move(9, speed=40)
    drive.move(-5)
# else:
#    drive.move(-4.5)

# Moves towards skateboard and drops spectator
drive.move(-3)
yaw(35)
drive.move(13, steering=-40)
yaw(89)
drop_figure()
action_back.start(speed=-100)

# Moves towards Intensive Adventure
yaw(95)
drive.move(51, steering=2)
yaw(38)
action_back.stop()
drive.move(20)
yaw(90)
drive.move(-2)

# Activates Intensive Adventure
action_back.run_for_rotations(8)
action_back.start(speed=-100)

# Moves towards Light Show and pushes it up, but still in yellow zone
drive.move(-2)
yaw()
drive.move(-25, speed=50)
action_back.stop()
action_back.run_for_rotations(10)
action_back.start(speed=-100)

# Move towards museum and drop spectator while moving The Wall down again.
drive.move(12, speed=40)
yaw(20)
drop_figure()

# Move back to Light Show and push it up into blue zone
yaw(5)
drive.move(-15,speed=40)
action_back.stop()
action_back.run_for_rotations(10)

# Move away, drop spectator next to Light Show and move towards AR
# action_back.start(speed=-100)
# drive.move(10)
# yaw(-90)
# drive.move(-30, steering=-20)
# drop_figure()
# action_back.stop()
# drive.move(-10)