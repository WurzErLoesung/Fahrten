#Ausrichtung:
#Linker Reifen:

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import *
from math import *

hub = PrimeHub()
drive = MotorPair('E', 'A')
action_back = Motor('B')
gyro = hub.motion_sensor
gyro.reset_yaw_angle()

def yaw(target_yaw: int = 0):
    direction = min(1, max(-1, gyro.get_yaw_angle() - target_yaw))# Wählt für alle Gradzahlen unter dem target_yaw -1, für alle Zahlen darüber +1 aus
    steering = 100 * direction                                    # Volle Kanne nach links oder nach rechts (100 oder -100)
    drive.start(steering, 10)                                    # Langsam, aber stark in Richtung drehen
    wait_until(gyro.get_yaw_angle, equal_to, target_yaw)            # Wartet, bis die Richtung 0° ist
    drive.stop()

#Funktion fürs Drehen aus der aus der aktuellen Position um eine Anzahl an Grad
def relative_yaw(yaw_step: int):
    yaw(gyro.get_yaw_angle() + yaw_step)
action_front = Motor('D')

action_back.run_for_rotations(-0.5)

#banana car
drive.move(-35, speed=40)
yaw(0)
action_back.run_for_rotations(0.5)
drive.move(-4.5)

action_back.run_for_rotations(-0.6)
drive.move(3)
drive.move(3, steering=50)
drive.set_stop_action('coast')
drive.move(-15, steering=-100)
drive.move(-5)
drive.move(-5, steering=-10)