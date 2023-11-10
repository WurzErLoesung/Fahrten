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

drop_figure_time = 0.3

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

drive.move(21,steering=32)
drive.move(7, steering=-100)
yaw(0)
drive.move(-3)
yaw(-8)
drive.move(-13,steering=-38,speed=100)
yaw(38)
drive.move(34, steering=5)
action_front.run_for_seconds(drop_figure_time, speed=-100)
drive.move(1)
drive.move(30, steering=46)
value = (2 if color.get_color() == 'yellow' else 1)
print(value)
for i in range(value):
    drive.move(12, speed=60)
    if i == 0: action_front.run_for_seconds(drop_figure_time, speed=-100)
    drive.move(-5)
    wait_for_seconds(1)
drive.move(-10, steering=70)
drive.move(15, steering=-30)
drive.move(8)
yaw(85)
drive.move(12)
action_front.run_for_seconds(drop_figure_time, speed=-100)
drive.move(15,steering=-24)
drive.move(30)
yaw(0)
drive.move(20)
