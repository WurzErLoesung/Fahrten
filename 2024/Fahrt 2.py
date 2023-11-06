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

hub.light_matrix.show_image('HAPPY')
drive_right = Motor ("A")
drive_left = Motor ("E")
action_front = Motor ("D")
action_back = Motor ("B")
drive = MotorPair("E", "A")
gyro = hub.motion_sensor
color = ColorSensor ("C")

gyro.reset_yaw_angle()

drive.set_stop_action("brake")

drive.move(20,steering=20)
yaw(15)
yaw(10)
drive.move(-3)
yaw(-10)
drive.move(-13,steering=-35,speed=100)
yaw(42)
drive.move(34)
action_front.run_for_seconds(1,speed=-100)
drive.move(1)
drive.move(30, steering=43)
action_front.run_for_seconds(1,speed=-100)
for i in range((2 if color.get_color() == 'violet' else 1)):
    drive.move(10)
    wait_for_seconds(1.5)
    drive.move(-10)
yaw(70)
drive.move(40)
   
