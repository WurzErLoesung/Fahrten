from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until
from spike.control import Timer as SpikeTimer
from spike.operator import *
from math import *
import uasyncio as asyncios

# INITIALIZATION
hub = PrimeHub()
MotionSensor = hub.motion_sensor
MotionSensor.reset_yaw_angle()
drive = MotorPair('B', 'F')
driveLeft = Motor('B')
driveRight = Motor('F')
driveLeft.set_stall_detection(True)
driveRight.set_stall_detection(True)
motor = Motor('D')
ColorLeft = ColorSensor('E')
ColorRight = ColorSensor('A')

# DRIVING TO BLACK LINE
drive.set_default_speed(50)
drive.start()

def onBlack():
    return ColorLeft.get_color() == "black" and ColorRight.get_color() == "black"

wait_until(onBlack)
drive.stop()
wait_for_seconds(0.1)

# ADJUSTMENT
drive.move(-20)
drive.move(32, steering=-45)
drive.start(-100, 10)
wait_until(MotionSensor.get_yaw_angle, greater_than_or_equal_to, 90)
drive.stop()
wait_for_seconds(0.1)

# RUN TASK
drive.set_default_speed(30)
drive.move(-10)
wait_for_seconds(0.1)
drive.move(25)

# DRIVE BACK
drive.move(-5, steering=-100)
drive.move(-80, steering=-20)