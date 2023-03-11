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
default_speed = 60

drive.set_default_speed(default_speed)
drive.set_stop_action('coast')

# drive to storage task
drive.move(15, "cm", 0, 50)
yaw(0)
action.run_for_degrees(-110, 50)
yaw(30)
drive.move(34, "cm", 0, 50)
yaw(0)

# drop energy
drive.move(25, "cm", 0, 40)
yaw(0)

#readjust for oil
drive.move(-16, "cm", 0)
yaw(40)
drive.move(17, "cm", 0)
yaw(-90)
wait_for_seconds(0.5)
yaw(-90)

#oil task
drive.move(10, "cm", 0)
for i in range(4):
    yaw(-90)
    drive.move(1, "seconds", 0, 100)
    drive.move(-5, "cm")

#collect energies
yaw(-90)
drive.move(-10, "cm")
yaw(-179)
action.run_for_degrees(110, 50)

MotionSensor.reset_yaw_angle()
yaw(58)
drive.move(-8, "cm", 0, 20)
yaw(53)
action.run_for_degrees(-110, 50)
drive.move(-8, "cm", 0, 20)
yaw(50)
action.run_for_degrees(110, 50)
yaw(135)
drive.move(-32, "cm")
action.run_for_degrees(-110, 50)
yaw(0)