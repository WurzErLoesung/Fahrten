from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor,
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

color = ColorSensor(Port.D)

print(color.hsv())