# Bei Fragen und Problemen an Simon Unger wenden
# Fahrt ist zuständig für weiße Batterie (Energie einladen und Lade mitnehmen) sowie den Wassertank (Wassereinheit herunterrollen lassen)

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

force = ForceSensor('D')
wait_until(force.is_pressed)
wait_for_seconds(0.5)

# VAR INITIALIZATION
default_speed = 40

hub = PrimeHub()
drive = MotorPair('B', 'F')

# move to storage task and stop slowly
drive.set_default_speed(default_speed)
drive.set_stop_action('coast')
drive.move(33.5, "cm", -5)
drive.move(38, "cm", 5)
drive.move(2, "cm", 5, 10)
wait_for_seconds(0.3)

# collect drawer from storage
drive.move(5, "cm", 0, -4)
drive.move(-16)
drive.move(-15, "cm", -88)
drive.start(10)

wait_until(force.is_pressed)
drive.stop()
