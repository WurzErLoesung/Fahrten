#Ausrichtung:
#blaue Base
#x-Achse West-Ost, y-Achse Süd-Nord
#Räder nach Norden
#Mitte der Lauffläche des rechten Reifens auf x=-4, y=~2,5 (am besten mittels Bande [4 Teile] ausrichten)


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

drive_right = Motor ("A")
drive_left = Motor ("E")
action_front = Motor ("D")
action_back = Motor ("B")
drive = MotorPair ("E", "A")
gyro = hub.motion_sensor

gyro.reset_yaw_angle()
action_front.set_default_speed(100)
drive.set_stop_action("brake")


drive.move(-16, speed=90)
yaw(-41)
action_front.run_for_rotations(-2)
drive.move(-32, steering=4, speed=80)
action_front.run_for_rotations(-1)
drive.move(17)
yaw(0)
action_front.run_for_rotations(2.3)
drive.move(-45, speed=100)
drive.move(13)
yaw(43)
drive.move(-18)
action_back.run_for_rotations(1)
action_front.run_for_rotations(-1)
drive.move(20)
yaw(0)
drive.move(40)
                