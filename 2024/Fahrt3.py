#Ausrichtung:
# linke Ecke mit Aufsatz
# Zeit= ~18 sec.


from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import *
from math import *

hub = PrimeHub()
drive = MotorPair('E', 'A')
action_back = Motor('B')
action_front = Motor('D')
gyro = hub.motion_sensor
gyro.reset_yaw_angle()

def yaw(target_yaw: int = 0):
    direction = min(1, max(-1, (gyro.get_yaw_angle() - target_yaw + 180) % 360 - 180))# Wählt für alle Gradzahlen unter dem target_yaw -1, für alle Zahlen darüber +1 aus
    steering = 100 * direction                                    # Volle Kanne nach links oder nach rechts (100 oder -100)
    drive.start(steering, 20)                                    # Langsam, aber stark in Richtung drehen
    wait_until(gyro.get_yaw_angle, equal_to, target_yaw)            # Wartet, bis die Richtung 0° ist
    drive.stop()

def relative_yaw(yaw_step: int):
    yaw((gyro.get_yaw_angle() + yaw_step + 180) % 360 - 180)
action_front = Motor('D')


drive.move(-35, speed=100)
drive.move(33, steering=50)
yaw(-132)
drive.move(47.5, speed=80)
drive.move(-1)
print("test")
relative_yaw(-88)
drive.move(44)
yaw(0)
action_back.run_for_rotations(0.5)
drive.move(75, speed=100)
