# Bei Fragen und Problemen an Simon Unger wenden
# Fahrt ist zuständig für Smart Grid, Solar Park, Öl-Plattform sowie wegräumen blauer Wassereinheiten

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
    return yaw(current_yaw + target_yaw)

# rotating relative to current position
def yaw(target_yaw: int):
    drive.start(100 * (min(1, max(MotionSensor.get_yaw_angle() - target_yaw, -1))), 10)
    wait_until(MotionSensor.get_yaw_angle, target_value=target_yaw)
    drive.stop()
    return MotionSensor.get_yaw_angle()

# funtion so stop on Black Line
def onLine():
    return ColorLeft.get_color() == "black" and ColorRight.get_color() == "black"
    
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
# Adjust Default Speed
default_speed = 50
# Adjust way out of START ZONE
way_out_start = 63
# Adjust steering out of START ZONE
steering_out_start = 15


# Drive to SMART GRID
drive.set_default_speed(default_speed)
drive.move(-way_out_start, "cm", steering_out_start)
current_yaw = yaw(0)
wait_for_seconds(0.1)

drive.start(0, -default_speed)
wait_until(onLine)
drive.stop()
drive.move(2)
wait_for_seconds(0.1)

current_yaw = yaw(90)
wait_for_seconds(0.1)

# Activate SMART GRID
drive.move(-45)
drive.move(22, "cm", 0, 60)

# Move to SOLAR FARM
start_yaw = yaw(179)
MotionSensor.reset_yaw_angle()
current_yaw = start_yaw

current_yaw = yaw(45)

drive.move(15)
drive.move(18, "cm", -20)
current_yaw = yaw(90)
drive.move(11)

# Collect ENERGY
current_yaw = yaw(16)
drive.move(17)

# Store ENERGY and move to OIL PLATFORM
current_yaw = yaw(-90)
drive.move(8)

current_yaw = yaw(-80)
drive.move(3)
start_yaw = yaw(90)
MotionSensor.reset_yaw_angle()
start_yaw = yaw(100)
MotionSensor.reset_yaw_angle()
current_yaw = start_yaw
drive.move(-10)

for i in range(3):
    drive.start(speed=-100)
    wait_for_seconds(1)
    drive.move(20, "cm", -2)
    wait_for_seconds(0.1)
    current_yaw = yaw(0)

start_yaw = yaw(150)
drive.move(24)
current_yaw = yaw(90)
drive.move(45, "cm", 0, 70)
current_yaw = yaw(179)

drive.start()
wait_until(force.is_pressed)
drive.stop()