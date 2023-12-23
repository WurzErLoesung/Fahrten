from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import *
from math import *

hub = PrimeHub()
drive = MotorPair('E', 'A')
action_back = Motor('B')
gyro = hub.motion_sensor
gyro.reset_yaw_angle()
wait_for_seconds(10)

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

action_back.run_for_rotations(-0.5)


drive.move(-35, speed=60)
yaw(0)
action_back.run_for_rotations(0.5)
drive.move(-4.5)

action_back.run_for_rotations(-0.6)
drive.move(3)


drive.set_stop_action('coast')
drive.move(-15, steering=-100, speed=100)


drive.move(-4, steering=100, speed=100)


yaw(0)

drive.move(44, steering=0)

wait_for_seconds(4)

# Mischpult (Motorgesteuerte Unterstützung notwendig)
drive.start(speed=60)
wait_for_seconds(1.9) # Previous: 1.9
action_front.run_for_seconds(0.7, speed=90)
wait_for_seconds(0.3)

drive.stop()
drive.move(-0.2)
drive.move(-10, 'cm', 100, 10)
drive.move(-30)
yaw(-70)
drive.move(70)
