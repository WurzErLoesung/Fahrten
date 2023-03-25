from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

# Wait until force sensor is pressed
print("Ready")
force = ForceSensor('D')
wait_until(force.is_pressed)
wait_for_seconds(0.5)

# rotating relative to current position
def relative_yaw(target_yaw: int):
    yaw(current_yaw + target_yaw)

# rotating to a specific position
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

drive.set_default_speed(60)
drive.move(50)
wait_for_seconds(1)
drive.move(-50, speed=100)

current_yaw = yaw(45)
drive.move(10)

wait_until(ColorLeft.get_color, target_value="black")
hub.light_matrix.set_pixel(0, 0, 100)
hub.light_matrix.set_pixel(0, 1, 100)
hub.light_matrix.set_pixel(0, 2, 100)
hub.light_matrix.set_pixel(0, 3, 100)
hub.speaker.beep(60, 1)

wait_for_seconds(2)

wait_until(ColorLeft.get_color, target_value="black")
hub.light_matrix.set_pixel(3, 0, 100)
hub.light_matrix.set_pixel(3, 1, 100)
hub.light_matrix.set_pixel(3, 2, 100)
hub.light_matrix.set_pixel(3, 3, 100)
hub.speaker.beep(60, 2)