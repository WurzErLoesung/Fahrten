from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
bpm = 180

sounds = [
    (60, 1.5 * 60 / bpm - 0.1), 
    (60, 0.5 * 60 / bpm - 0.1),
    (62, 2 * 60 / bpm - 0.1),
    (60, 2 * 60 / bpm - 0.1),
    (65, 2 * 60 / bpm - 0.1),
    (64, 4 * 60 / bpm - 0.1),
    (60, 1.5 * 60 / bpm - 0.1),
    (60, 0.5 * 60 / bpm - 0.1),
    (62, 2 * 60 / bpm - 0.1),
    (60, 2 * 60 / bpm - 0.1),
    (67, 2 * 60 / bpm - 0.1),
    (65, 4 * 60 / bpm - 0.1),
    (60, 1.5 * 60 / bpm - 0.1),
    (60, 0.5 * 60 / bpm - 0.1),
    (72, 2 * 60 / bpm - 0.1),
    (69, 2 * 60 / bpm - 0.1),
    (65, 1.5 * 60 / bpm - 0.1),
    (65, 0.5 * 60 / bpm - 0.1),
    (64, 2 * 60 / bpm - 0.1),
    (62, 6 * 60 / bpm - 0.1),
    (70, 1.5 * 60 / bpm - 0.1),
    (70, 0.5 * 60 / bpm - 0.1),
    (69, 2 * 60 / bpm - 0.1),
    (65, 2 * 60 / bpm - 0.1),
    (67, 2 * 60 / bpm - 0.1),
    (65, 4 * 60 / bpm - 0.1)
]

light_matrix = [
    [100, 0, 100, 0, 100],
    [0, 0, 0, 0, 0],
    [0, 100, 100, 100, 0],
    [0, 100, 100, 100, 0],
    [0, 0, 100, 0, 0]
]

for y in range(len(light_matrix)):
    for x in range(len(light_matrix[y])):
        hub.light_matrix.set_pixel(x, y, light_matrix[y][x])

hub.speaker.set_volume(100)
for i in range(3):
    hub.speaker.beep(67, 0.1)
    wait_for_seconds(2 * 60 / bpm - 0.1)
for element in sounds:
    hub.speaker.beep(element[0], element[1])
    wait_for_seconds(0.1)


gyro = hub.motion_sensor
gyro.reset_yaw_angle()

drive = MotorPair('E', 'A')
drive.move(10)
drive.move(-10)
drive.move(10, steering = 100)
drive.move(10, steering = -100)
drive.move(10)
drive.move(-10)
drive.move(10, steering = -100)
drive.move(10, steering = 100)
drive.start(steering=-100)

def stop():
    return gyro.get_yaw_angle() > -5 and gyro.get_yaw_angle() < 5
wait_for_seconds(1)
wait_until(stop)
drive.stop()

hub.light_matrix.write("Happy Birthday!")

for y in range(len(light_matrix)):
    for x in range(len(light_matrix[y])):
        hub.light_matrix.set_pixel(x, y, light_matrix[y][x])
