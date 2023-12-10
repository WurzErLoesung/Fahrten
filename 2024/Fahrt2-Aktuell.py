#Ausrichtung
#mitte vom linken Rad: x= 8, y=10,5

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import *
from math import *

def yaw(target_yaw: int = 0):
    direction = min(1, max(-1, gyro.get_yaw_angle() - target_yaw))# Wählt für alle Gradzahlen unter dem target_yaw -1, für alle Zahlen darüber +1 aus
    steering = 100 * direction                                    # Volle Kanne nach links oder nach rechts (100 oder -100)
    drive.start(steering, 10)                                    # Langsam, aber stark in Richtung drehen
    wait_until(gyro.get_yaw_angle, equal_to, target_yaw)            # Wartet, bis die Richtung 0° ist
    drive.stop()

#Funktion fürs Drehen aus der aus der aktuellen Position um eine Anzahl an Grad
def relative_yaw(yaw_step: int):
    yaw(gyro.get_yaw_angle() + yaw_step)

drop_figure_time = 0.5
#Funktion um die Zuschauer fallen zu lassen
def drop_figure():
    action_front.run_for_seconds(drop_figure_time, speed=-100)

#Initalisierung der Motoren und Sensoren
hub = PrimeHub()

drive_right = Motor ("A")
drive_left = Motor ("E")
action_front = Motor ("D")
action_back = Motor ("B")
drive = MotorPair("E", "A")
gyro = hub.motion_sensor
color = ColorSensor ("C")

gyro.reset_yaw_angle()#Gradzahl des Gyrosensors zurücksetzen

drive.set_stop_action("brake")#Bremseinstellung wird zu "brake" geändert (bremst schnell, lässt die Reifen aber frei auslaufen)

drive.set_default_speed(50) #Standard Schnelligkeit 50%

#3d Kino
drive.move(22, steering=32)
drive.move(7, steering=-100)
yaw(0)
drive.move(-3)
yaw(-8)
drive.move(-13, steering=38, speed=100)

wait_for_seconds(10)

drive.move(33, steering = -15) #Fährt zu Popcorn
drop_figure() #lässt erste Figur fallen
drop_figure_time=0.3
drive.move(-2)
drive.move(40, steering = 40) #Fährt zu Aufgabe Szenenwechsel
drop_figure() #lässt zweite Figur bei Szenenwechsel fallen
#Aufgabe Szenenwechsel
value = (1 if color.get_color() == 'yellow' else 0)
print(value)
if value == 1:
    drive.move(-5)
    drive.move(5)

drive.move(-5)
