from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
from pupdevices import PupDevices

hub = PrimeHub()

def drive3(pd):
    #DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.drive_base.settings(straight_speed=40, straight_acceleration=80)

    hub.speaker.beep()


    pd.drive_base.straight(100)
    pd.drive_base.settings(straight_speed=600, straight_acceleration=500)
    pd.drive_base.straight(-150)

    yield False

    print(pd.timer.time())

if __name__ == "__main__":
    for element in drive3(PupDevices()): pass