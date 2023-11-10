from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import *
from math import *

def yaw(target_yaw: int = 0):
    direction = min(1, max(-1, gyro.get_yaw_angle() - target_yaw))
    steering = 100*direction
    drive.start(steering, 10)
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
drive = MotorPair ("E", "A")
gyro = hub.motion_sensor

gyro.reset_yaw_angle()

drive.set_stop_action("brake")



yaw(-48)
drive.move(55)
action_front.run_for_rotations(10, speed = 100)
drive.move(-20)
yaw(10)
drive.move(54)
yaw(37)
drive.move(20, speed = 60)
drive.move(-20)
yaw(150)
drive.move(75)
