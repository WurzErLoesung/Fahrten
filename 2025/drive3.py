from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task

hub = PrimeHub()

#DriveBase initialisieren
wheel_diameter = 56 
axle_track = 113 
drive_base = DriveBase(pd.left_motor, pd.right_motor, wheel_diameter, axle_track)
drive_base.use_gyro(True) 
drive_base.settings(straight_speed=900, straight_acceleration=500)

hub.speaker.beep()

def drive3():
    drive_base.settings(300)
    drive_base.straight(100)
    yield True
    drive_base.straight(-100)
    yield False

if __name__ == "__main__":
    drive3()
