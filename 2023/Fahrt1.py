# Bei Fragen und Problemen an Simon Unger wenden
# Fahrt ist zuständig für TV, Windrad, Auto und akku mitenehmen neben Trichter.

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until
from spike.control import Timer as SpikeTimer
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

# VAR INITIALIZATION
start_yaw = MotionSensor.get_yaw_angle()
current_yaw = start_yaw
# Adjust how far Robot moves in direction of WINDMILL
windmill_alignment_length = 42
# Adjust Yaw of Alignment
windmill_alignment_yaw = 47
# Adjust Speed when activating windmill
windmill_speed = 70
# Adjust number of repeats during windmill
windmill_repeatation = 3
# Adjust how long the robot moves to activate windmill
windmill_time = 1
# Adjust adjustment length
car_alignment_length = 6
# Adjust how far robot moves in direction of the car
car_alignment_width = 25
# Adjust alignment yaw for the car
car_alignment_yaw = -52
# Adjust how far the robot moves to activate car
car_length = 30
# Adjust Speed for activating car
car_speed = 60
# Adjust the robot's default speed
default_speed = 55
# Adjust how far the robot moves back after activating the car
backwards_after_car = -18
# Adjust the steering when moving backwards after car
steering_after_car = 37

# TV
drive.set_default_speed(default_speed)
drive.move(55, "cm", 0, default_speed)
drive.move(-10, "cm", 0, default_speed)
current_yaw = yaw(start_yaw)

# Drive to WINDMILL
current_yaw = yaw(-45)
drive.move(windmill_alignment_length)
current_yaw = yaw(windmill_alignment_yaw)
drive.move(14)

# WINDMILL
for i in range(windmill_repeatation):
    drive.set_default_speed(windmill_speed)
    drive.start()
    wait_for_seconds(windmill_time)
    drive.stop()
    drive.set_default_speed(default_speed)
    drive.move(-4)
    current_yaw = yaw(windmill_alignment_yaw)
    current_yaw = yaw(windmill_alignment_yaw)
    wait_for_seconds(0.25)

# Drive to CAR
drive.move(-10)
current_yaw = yaw(0)
drive.move(car_alignment_length)
current_yaw = yaw(-90)
drive.move(car_alignment_width)
current_yaw = yaw(car_alignment_yaw)

# Acitivate CAR
drive.move(car_length, "cm", 1, car_speed)
drive.move(backwards_after_car, "cm", steering_after_car)

# Drive back to HOMEZONE
current_yaw = current_yaw = yaw(car_alignment_yaw)
drive.move(-40, "cm", 0, default_speed)
drive.move(-120, "cm", -2, default_speed)
