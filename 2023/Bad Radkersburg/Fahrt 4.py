# Bei Fragen und Problemen an Simon Unger wenden
# Fahrt ist zuständig für weiße Batterie (Energie einladen und Lade mitnehmen) sowie den Wassertank (Wassereinheit herunterrollen lassen)

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

force = ForceSensor('D')
wait_until(force.is_pressed)
wait_for_seconds(0.5)

def onBlackLine():
    return ColorLeft.get_color() == "black" or ColorRight.get_color() == "black"

def leftOnBlack():
    return ColorLeft.get_color() == "black"

def relative_yaw(target_yaw: int):
    yaw(current_yaw + target_yaw)

def yaw(target_yaw: int):
    drive.start(100 * (min(1, max(MotionSensor.get_yaw_angle() - target_yaw, -1))), 10)
    wait_until(MotionSensor.get_yaw_angle, target_value=target_yaw)
    drive.stop()
    return MotionSensor.get_yaw_angle()

hub = PrimeHub()
drive = MotorPair('B', 'F')
action = Motor('C')
MotionSensor = hub.motion_sensor
MotionSensor.reset_yaw_angle()
ColorLeft = ColorSensor('E')
ColorRight = ColorSensor('A')


# VAR INITIALIZATION
start_yaw = MotionSensor.get_yaw_angle()
current_yaw = start_yaw
default_speed = 50

# move to storage task and stop slowly
drive.set_default_speed(default_speed)
drive.set_stop_action('coast')
drive.move(33.5, "cm", -13)
drive.move(37, "cm", 12)
drive.move(5, "cm", 12, 10)
wait_for_seconds(0.3)

# collect drawer from storage
drive.move(-21)
current_yaw = yaw(45)
drive.start()
wait_for_seconds(0.2)
wait_until(onBlackLine)
drive.stop()
drive.move(5)
current_yaw = yaw(90)
drive.move(-4)

for i in range(3):
    drive.start(0, -50)
    wait_for_seconds(0.5)
    drive.stop()
    drive.move(5)

drive.move(5, "cm")
drive.move(-8, "cm", -60)
drive.move(12, "cm")
drive.move(5, "cm", -20)
current_yaw = yaw(90)
drive.move(-5, "cm")

action.run_for_seconds(1.5, -100)

drive.move(22, "cm", 7)
drive.move(5, "cm", -100)
current_yaw = yaw(140)
drive.move(25, "cm", -10)
current_yaw = yaw(175)
drive.move(20, "cm")

drive.start(0, -50)
action.start(100)
wait_for_seconds(2)
action.stop()
drive.stop()
drive.start(5, 50)
action.start(-100)
wait_for_seconds(1)
drive.stop()
wait_for_seconds(1.5)
action.stop()
drive.move(10, "cm", -5)

wait_until(force.is_pressed)
drive.stop()