from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from action_arc import action_arc
from yaw import Yaw
from pupdevices import PupDevices

hub = PrimeHub()

watch = StopWatch()

def drive3(pd):
    #DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(straight_speed=150, straight_acceleration=500)
    db = pd.drive_base

    db.settings(350)


    yaw = Yaw(hub, pd.left_motor, pd.right_motor)

    pd.drive_base.straight(300)
    yaw(45)
    pd.drive_base.straight(330)
    yaw(-7)
    wait(2000)
    db.settings(200)
    pd.drive_base.straight(160)
    db.settings(500)
    pd.drive_base.straight(80)
    pd.drive_base.straight(-300)


if __name__ == "__main__":
    for element in  drive3(PupDevices()): pass