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
    print(gyro.get_yaw_angle())
    print(target_yaw)
    direction = min(1, max(-1, (gyro.get_yaw_angle() - target_yaw + 180) % 360 - 180))# Wählt für alle Gradzahlen unter dem target_yaw -1, für alle Zahlen darüber +1 aus
    steering = 100 * direction                                    # Volle Kanne nach links oder nach rechts (100 oder -100)
    print(steering)
    drive.start(steering, 10)                                    # Langsam, aber stark in Richtung drehen
    wait_until(gyro.get_yaw_angle, equal_to, target_yaw)            # Wartet, bis die Richtung 0° ist
    drive.stop()

def relative_yaw(yaw_step: int):
    yaw((gyro.get_yaw_angle() + yaw_step + 180) % 360 - 180)
action_front = Motor('D')

#hub.light_matrix.show_image('HAPPY')

action_back.run_for_degrees(90)
drive.move(-35)
drive.move(30, steering=30)
yaw(-134)
drive.move(49)
drive.move(-1)
relative_yaw(-90)
drive.move(38) #4cm dazu gegeben
yaw(0)
drive.move(-10)
relative_yaw(-1)
action_back.run_for_degrees(-90)
relative_yaw(1)
drive.move(70)
