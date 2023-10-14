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

def relative_yaw(yaw_step: int):
    yaw(gyro.get_yaw_angle() + yaw_step)
action_front = Motor('D')

hub.light_matrix.show_image('HAPPY')

action_back.run_for_rotations(0.5)
drive.move(-30, speed=40)
action_back.run_for_rotations(-0.5)
drive.move(-10)
action_back.run_for_rotations(0.5)
drive.move(3)
drive.set_stop_action('coast')
drive.move(-2, steering=-100)
drive.move(-1, steering=100)
drive.set_stop_action('brake')
drive.move(40, steering=-7)

wait_for_seconds(3)

drive.start(speed=40)
wait_for_seconds(2)
action_front.run_for_seconds(0.5, speed=-100)
wait_for_seconds(0.5)
drive.stop()
drive.move(-1)
drive.move(-10, 'cm', 100, 10)
drive.move(-30)
drive.move(10, steering=-100)
drive.move(40)