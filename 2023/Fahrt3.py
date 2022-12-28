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
def onBlackLine(): #Returns True if both color sensors are seeing black
    if color1.get_color() and color2.get_color() == "black":
        return True
    else:
        return False

def moveUntilBlackLine(speed: int, delay :float = 1, steering :int = 0): #Starts the motor pair and leaves it running until onBlackLine returns True
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
motor_pair.move(62, "cm", steering=-6, speed=60) #Drive a smooth curve around "Trichter"

moveUntilBlackLine(50) #Drives straight until the black line in the middle 
motor_pair.move(3, "cm", speed=20) #Correction because the color sensors are not placed on the same position as the wheels

yaw(90) #Spins until the robot is parallel to the black line in the middle

moveUntilBlackLine(40) #Drives until the black line before the hand
motor_pair.move(20, "cm", speed=30) #Drives forward into the hand
motor_pair.move(9, "cm", speed=-15) #Drives backwards, so the hand gets triggered
motor_pair.move(11, "cm", speed=-100) #Drives backwards, so the module for the hand disconnects from the robot

yaw(23) #Spins so the robot is able to drive between the hand and the other fucking thing

motor_pair.move(10, "cm", speed=30) #Drives a bit forward, so the robot is able to do the next line without crashing into the hand
motor_pair.move(30, "cm", steering=-69, speed=30) #Drives a curve, so the robot is able to collect the batteries on the side