# Bei Fragen an Severin wenden
# Fahrt ist zuständig für Hand, Ölinsel und die Energiezellen daneben.

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')

motor_pair = MotorPair("B", "F")
color1 = ColorSensor("E")
color2 = ColorSensor("A")

def onBlackLine():
    if color1.get_color() and color2.get_color() == "black":
        return True
    else:
        return False
hub.motion_sensor.reset_yaw_angle()

motor_pair.move(65, "cm", steering=0, speed=80)

motor_pair.start(speed=20, steering=-100)
wait_until(hub.motion_sensor.get_yaw_angle,target_value=90)
motor_pair.stop()

motor_pair.move(8, "cm", steering=0, speed=70)

motor_pair.start(speed=20, steering=100)
wait_until(hub.motion_sensor.get_yaw_angle,target_value=0)
motor_pair.stop()


motor_pair.start(speed=50)



wait_until(onBlackLine,target_value=True)

motor_pair.stop()


motor_pair.start(speed=15, steering=-100)
wait_until(hub.motion_sensor.get_yaw_angle,target_value=90)
motor_pair.stop()

motor_pair.move(60, "cm", speed=100)

motor_pair.move(10, "cm", speed=30)

motor_pair.move(20, "cm", speed=-40)