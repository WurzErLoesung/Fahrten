from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

force = ForceSensor('D')
wait_until(force.is_pressed)
wait_for_seconds(0.5)

hub = PrimeHub()
drive = MotorPair('B', 'F')

# move to storage task and stop slowly
drive.set_default_speed(50)
drive.set_stop_action('coast')
drive.move(33.5, "cm", -5, 40)
drive.move(39, "cm", 5, 30)
drive.move(1.5, "cm", 5, 10)
wait_for_seconds(0.3)

# collect drawer from storage
drive.move(5, "cm", 0, -4)
drive.move(-16)
drive.move(-15, "cm", -88, 40)
drive.start(10, 50)

wait_until(force.is_pressed)
drive.stop()
