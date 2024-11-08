from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import equal_to
from math import *
hub = PrimeHub()

print("Ready")
hub.light_matrix.show_image('HAPPY')
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

def black_found():
    if ColorLeft.get_color() in ["white", "black"] or ColorRight.get_color() in ["white", "black"]:
        return True

# INITIALIZATION
MotionSensor = hub.motion_sensor
MotionSensor.reset_yaw_angle()
drive = MotorPair('B', 'F')
action = Motor('C')
ColorLeft = ColorSensor('E')
ColorRight = ColorSensor('A')
drive.set_stop_action("hold")


drive.start(speed=100)
wait_for_seconds(1)
action.run_for_rotations(0.5, speed=70)
drive.start(-20, speed=80)
action.start(-100)
wait_for_seconds(0.3)
action.stop()
wait_for_seconds(0.7)
drive.start(40, speed=80)
wait_for_seconds(0.5)
drive.start(10, speed=100)
wait_until(force.is_pressed)
drive.stop()