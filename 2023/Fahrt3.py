# Bei Fragen an Severin wenden
# Fahrt ist zuständig für Hand, Ölinsel und die Energiezellen daneben.


from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *


#Initialising
hub = PrimeHub()
motor_pair = MotorPair("B", "F")
color1 = ColorSensor("E")
color2 = ColorSensor("A")
hub.motion_sensor.reset_yaw_angle()


#Black line stuff
def onBlackLine():
    if color1.get_color() and color2.get_color() == "black":
        return True
    else:
        return False

def moveUntilBlackLine(speed: int, delay = 1, steering :int = 0):
    motor_pair.start(speed=speed, steering = steering)
    wait_for_seconds(delay)
    wait_until(onBlackLine,target_value=True)
    motor_pair.stop()


#Easy to use spinning function
def yaw(targetYaw :int, speed :int=15):
    motor_pair.start(speed=speed, steering=100 * (min(1, max(hub.motion_sensor.get_yaw_angle() - targetYaw, -1))))
    wait_until(hub.motion_sensor.get_yaw_angle,target_value=targetYaw)
    motor_pair.stop()


#Code for Driving
motor_pair.move(62, "cm", steering=-6, speed=60)

#yaw(targetYaw=90, speed=20)
#motor_pair.move(5, "cm", steering=0, speed=70)
#yaw(targetYaw=0, speed=20)

moveUntilBlackLine(50)
motor_pair.move(3, "cm", speed=20)

yaw(90)

if color1.get_color == "black":
    yaw(targetYaw=0, speed=20)
    motor_pair.move(3, "cm", speed=15)
    yaw(targetYaw=90, speed=20)
elif color2.get_color == "black":
    yaw(targetYaw=180, speed=20)
    motor_pair.move(3, "cm", speed=15)
    yaw(targetYaw=90, speed=20)

moveUntilBlackLine(40)
motor_pair.move(20, "cm", speed=30)

#yaw(76)

motor_pair.move(9, "cm", speed=-15)
motor_pair.move(11, "cm", speed=-100)

yaw(23)

motor_pair.move(10, "cm", speed=30)
motor_pair.move(30, "cm", steering=-69, speed=30)