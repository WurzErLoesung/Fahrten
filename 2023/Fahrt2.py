# Bei Fragen und Problemen an Simon Unger wenden
# Fahrt ist zuständig für Kraftwerk und Spielzeugfabrik

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until
from spike.control import Timer as SpikeTimer
from math import *

print("Ready")
force = ForceSensor('D')
wait_until(force.is_pressed)
wait_for_seconds(0.5)

def dropEnergy():
    action.start(-30)
    wait_for_seconds(3)
    action.stop()

def onBlackLine():
    return ColorLeft.get_color() == "black" and ColorRight.get_color() == "black"

def relative_yaw(target_yaw: int):
    yaw(current_yaw + target_yaw)

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
default_speed = 50


# Drive to POWER ENGINE
drive.set_default_speed(default_speed)
current_yaw = yaw(2)
drive.start()
wait_until(onBlackLine)
drive.stop()

# Align linear to POWER ENGINE
drive.move(-10)
current_yaw = yaw(45)
drive.start()
wait_until(ColorLeft.get_color, target_value="black")
wait_for_seconds(max(0, 0.7 - (default_speed/100)))
drive.stop()
current_yaw = yaw(-90)

# Activate POWER ENGINE
drive.start()
wait_until(onBlackLine)
wait_for_seconds(1)
drive.stop()
wait_for_seconds(0.25)

# Align for TOY FACTORY
drive.move(-15)
current_yaw = yaw(-35)
drive.move(-20)
drive.move(3)

# Activate TOY FACTORYs
dropEnergy()

# Drive Back to HOMEZONE
drive.start()
wait_until(ColorLeft.get_color, target_value="black")
drive.stop()
current_yaw = yaw(5)
drive.move(-180, "cm", 2)
