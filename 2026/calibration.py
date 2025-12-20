from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import (ColorSensor, ForceSensor, Motor,
                                 UltrasonicSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, run_task, wait

from pupdevices import PupDevices
from yaw import Yaw

hub = PrimeHub()
print(f"{hub.battery.voltage()/1000} Volt")
watch = StopWatch()
hub.speaker.beep()
pd = PupDevices()

"""
Color.MAGENTA = Color(h=333, s=75, v=78)
Color.RED = Color(h=355, s=86, v=90)
Color.BLUE = Color(h=214, s=89, v=82)
Color.GREEN = Color(h=158, s=75, v=45)
Color.YELLOW = Color(h=52, s=59, v=100)
Color.WHITE = Color(h=0, s=0, v=100)
Color.NONE = Color(h=0, s=0, v=0)
Color.BLACK = Color(h=170, s=20, v=36)
"""

while True:
    print(f"Color: {pd.color.color()}, hsv: {pd.color.hsv()}")
    wait(500)
