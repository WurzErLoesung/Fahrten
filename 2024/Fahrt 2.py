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

def drop_figure():
    drop_figure_time = 1.3
    action_front.run_for_seconds(drop_figure_time, speed=-100) 
    action_front.run_for_seconds(drop_figure_time, speed=100)


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

#3d Kino
drop_figure_time = 1.3
drive.move(21,steering=32)
drive.move(7, steering=-100)
yaw(0)
drive.move(-3)
yaw(-8)
drive.move(-13,steering=-38,speed=100)

wait_for_seconds(5)
drive.move(-57, steering=2)
drop_figure()
drive.move(-1)
#second person
drop_figure()
#Aufgabe Szenenwechsel
value = (2 if color.get_color() == 'yellow' else 1) 
relative_yaw(180)
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
