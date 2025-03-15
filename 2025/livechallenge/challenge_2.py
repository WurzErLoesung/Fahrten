from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
import umath as math


motor = Motor(Port.A)

def straight(speed):
    toggle = True
    while True:
        motor.run_angle((-1 * toggle) * (500 + (not toggle)*500), 150 + toggle*100)
        toggle = not toggle
        wait(50)

motor.run_angle(-500, 5*360)
# straight(-800)
