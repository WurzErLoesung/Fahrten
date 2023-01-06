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
action = Motor('C')
ColorLeft = ColorSensor('E')
ColorRight = ColorSensor('A')
drive.set_stop_action("hold")

# Variable Initialization
start_yaw = MotionSensor.get_yaw_angle()
current_yaw = start_yaw
# Adjust Default Speed
default_speed = 35
# Adjust Speed to OIL VEHICLE
speed_vehicle = 35
# Adjust way to OIL VEHICLE
way_to_oil = 55
# Adjust straight way at start of Part 2
straight_part_two = 3
# Asjust way to CENTER
way_to_center = 101
# Adjust steering to CENTER
steering_to_center = 12
# Adjust way to drop at CENTER
way_drop_center = 25
# Adjust yaw for drop at CENTER
yaw_drop_center = 90
# Adjust way after drop at CENTER
way_after_center = 5.5
# Adjust yaw to BATTERY
yaw_after_center = 45
# Adjust way to BATTERY
way_to_solar = 70
# Adjust speed to BATTERY & GOAL
speed_to_goal = 70

# Collect OIL VEHICLE
current_yaw = yaw(1)
drive.set_default_speed(default_speed)
drive.set_stop_action("coast")
drive.move(way_to_oil/2, "cm", 0, speed_vehicle)
yaw(0)
drive.move(way_to_oil/2, "cm", 0, speed_vehicle)
wait_for_seconds(0.25)
drive.start(speed=-speed_vehicle)
wait_until(force.is_pressed)
wait_for_seconds(0.5)
drive.stop()

# Wait until Button is pressed
wait_until(force.is_pressed)
wait_for_seconds(0.5)

# PART 2

drive.move(straight_part_two)

# Drive to CENTER
drive.move(way_to_center, "cm", steering_to_center)

# Drop at CENTER
drive.move(-way_drop_center)
current_yaw = yaw(yaw_drop_center)

# Move to BATTERY
drive.move(way_after_center)
current_yaw = yaw(yaw_after_center)
drive.set_stop_action("hold")
drive.move(65, "cm", 0, speed_to_goal)
action.run_for_seconds(0.5, -50)
drive.start(speed=speed_to_goal)
wait_for_seconds(0.2)
drive.move(3, "cm", 0, -100)
