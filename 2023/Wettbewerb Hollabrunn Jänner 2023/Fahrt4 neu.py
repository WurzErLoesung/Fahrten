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

def relative_yaw(target_yaw: int):
    yaw(current_yaw + target_yaw)

def yaw(target_yaw: int):
    drive.start(100 * (min(1, max(MotionSensor.get_yaw_angle() - target_yaw, -1))), 10)
    wait_until(MotionSensor.get_yaw_angle, target_value=target_yaw)
    drive.stop()
    return MotionSensor.get_yaw_angle()

hub = PrimeHub()
drive = MotorPair('B', 'F')
MotionSensor = hub.motion_sensor
MotionSensor.reset_yaw_angle()
ColorLeft = ColorSensor('E')
ColorRight = ColorSensor('A')


# VAR INITIALIZATION
start_yaw = MotionSensor.get_yaw_angle()
current_yaw = start_yaw
default_speed = 40

# move to storage task and stop slowly
drive.set_default_speed(default_speed)
drive.set_stop_action('coast')
drive.move(33.5, "cm", -5)
drive.move(39, "cm", 5)
drive.move(2, "cm", 5, 10)
wait_for_seconds(0.3)

# collect drawer from storage
drive.move(5, "cm", 0, -4)
drive.move(-16)
current_yaw = yaw(45)
drive.move(5)
drive.start()
wait_until(onBlackLine)
wait_for_seconds(0.5)
drive.stop()
current_yaw = yaw(90)
drive.move(-4)
for i in range(4):
    drive.move(-10, speed=100)
    wait_for_seconds(0.2)
    drive.move(9)
    wait_for_seconds(0.1)
    current_yaw = yaw(90)

current_yaw = yaw(0)
drive.move(-12)
current_yaw = yaw(-20)
drive.move(-10, "cm", -88)
drive.move(30, "cm", 50)
drive.start()

wait_until(force.is_pressed)
drive.stop()