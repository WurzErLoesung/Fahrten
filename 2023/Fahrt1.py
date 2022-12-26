from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until
from spike.control import Timer as SpikeTimer
from math import *

def relative_yaw(target_yaw: int):
    yaw(current_yaw + target_yaw)

def yaw(target_yaw: int):
    drive.start(100 * (min(1, max(MotionSensor.get_yaw_angle() - target_yaw, -1))), 10)
    wait_until(MotionSensor.get_yaw_angle, target_value=target_yaw)
    drive.stop()
    current_yaw = MotionSensor.get_yaw_angle()

# INITIALIZATION
hub = PrimeHub()
MotionSensor = hub.motion_sensor
MotionSensor.reset_yaw_angle()
drive = MotorPair('B', 'F')
ColorLeft = ColorSensor('E')
ColorRight = ColorSensor('A')
drive.set_stop_action("hold")

# Variable Initialization
start_yaw = MotionSensor.get_yaw_angle()
current_yaw = start_yaw
windmill_alignment_yaw = 45

# TV
drive.set_default_speed(30)
drive.move(55)
drive.move(-15)
yaw(start_yaw)

# Drive to windmill
drive.move(5, steering=100)
drive.move(45)
drive.set_default_speed(60)
yaw(windmill_alignment_yaw)

# Do windmill
for i in range(4):
    drive.set_default_speed(80)
    drive.move(1, 'seconds')
    wait_for_seconds(0.25)
    drive.set_default_speed(20)
    drive.move(-2)
    yaw(windmill_alignment_yaw)
    drive.move(-8)
    wait_for_seconds(0.75)

# Drive to Car
drive.move(-10)
yaw(-80)
drive.move(35)
relative_yaw(35)

# Activate Car
drive.set_default_speed(30)
drive.move(10)