# Bei Fragen und Problemen an Simon Unger wenden
# Fahrt ist zuständig für POWER ENGINE und TOY FACTORY

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until
from spike.control import Timer as SpikeTimer
from math import *

# Wait until force sensor is pressed
print("Ready")
force = ForceSensor('D')
wait_until(force.is_pressed)
wait_for_seconds(0.5)

# function to activate TOY FACTORY
def dropEnergy():
    action.run_for_rotations(4, 80)

# funtion so stop on Black Line
def onBlackLine():
    return ColorLeft.get_color() == "black" and ColorRight.get_color() == "black"

# rotating relative to current position
def relative_yaw(target_yaw: int):
    yaw(current_yaw + target_yaw)

# rotating to a specific position
def yaw(target_yaw: int):
    drive.start(100 * (min(1, max(MotionSensor.get_yaw_angle() - target_yaw, -1))), 10)
    wait_until(MotionSensor.get_yaw_angle, target_value=target_yaw)
    drive.stop()
    wait_for_seconds(0.1)
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

# VAR INITIALIZATION
start_yaw = MotionSensor.get_yaw_angle()
current_yaw = start_yaw
# Adjust robots default speed
default_speed = 55
# Adjust how far the Robot moves out of HOMEZONE
way_out_home = 50
# Adjust the steering out of HOMEZONE
steering_out_home = -7
# Adjust how far the robot moves back after standing on black line
back_after_black = -10
# Adjust yaw for aligning on black line
yaw_align_black = 45
# Adjust way back after POWER ENGINE
back_after_power = -15
# Adjust alignment yaw for TOY FACTORY
yaw_toy_factory = -37 # BEFORE: -35
# Adjust way to TOY FACTORY
way_toy_factory = -19 # BEFORE: -20
# Adjust way back for TOY FACTORY
back_toy_factory = 0


# Drive to POWER ENGINE
drive.set_default_speed(default_speed)
current_yaw = yaw(2)
drive.move(way_out_home, "cm", steering_out_home)
current_yaw = yaw(0)
drive.start()
wait_until(onBlackLine)
drive.stop()

# Align linear to POWER ENGINE
drive.move(back_after_black, speed=70)
current_yaw = yaw(yaw_align_black)
drive.start(0)
wait_until(ColorLeft.get_color, target_value="black")
wait_for_seconds(max(0, 0.7 - (default_speed/100)))
drive.stop()
current_yaw = yaw(-90)

# Activate POWER ENGINE
drive.start()
wait_until(onBlackLine)
wait_for_seconds(0.5)
drive.stop()
wait_for_seconds(0.25)

# Align for TOY FACTORY
drive.move(back_after_power)
current_yaw = yaw(yaw_toy_factory)
drive.move(way_toy_factory)
drive.move(back_toy_factory)

# Activate TOY FACTORYs
dropEnergy()

# Drive Back to HOMEZONE
drive.start()
wait_until(ColorLeft.get_color, target_value="black")
drive.stop()
current_yaw = yaw(5)
drive.start(2, -100)

wait_until(force.is_pressed)
drive.stop()
