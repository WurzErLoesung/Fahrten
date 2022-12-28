from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

print("Ready")
force = ForceSensor('D')
wait_until(force.is_pressed)
wait_for_seconds(0.5)

def relative_yaw(target_yaw: int):
    yaw(current_yaw + target_yaw)

def yaw(target_yaw: int):
    drive.start(100 * (min(1, max(MotionSensor.get_yaw_angle() - target_yaw, -1))), 10)
    wait_until(MotionSensor.get_yaw_angle, target_value=target_yaw)
    drive.stop()
    return MotionSensor.get_yaw_angle()

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
# Adjust Default Speed
default_speed = 50
# Adjust Speed to OIL VEHICLE
speed_vehicle = 40
# Adjust way to OIL VEHICLE
way_to_oil = 55
# Adjust way to CENTER
way_to_center = 120
# Adjust steering to CENTER
steering_to_center = 7
# Adjust way to GOAL
way_to_goal = 30
# Adjust steering to GOAL
steering_to_goal = 2

# Collect OIL VEHICLE
drive.set_default_speed(default_speed)
drive.move(way_to_oil, "cm", 0, speed_vehicle)
wait_for_seconds(0.25)
drive.move(-way_to_oil)

# Wait until Button is pressed
wait_until(force.is_pressed)
wait_for_seconds(0.5)

# Drive to CENTER and drop building
drive.move(way_to_center, "cm", steering_to_center)
wait_for_seconds(1)

# Drive to GOAL
drive.move(way_to_goal, "cm", steering_to_goal)
