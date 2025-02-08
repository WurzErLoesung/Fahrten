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

def drive4(pd):
    #DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(straight_speed=150, straight_acceleration=500)
    db = pd.drive_base


    yaw = Yaw(hub, pd.left_motor, pd.right_motor)

    pd.action_front.run_angle(350, 100)

    # db.straight(150)
    db.straight(400)
    pd.action_back.run_angle(350, 360)
    db.settings(350)
    db.straight(470)
    pd.action_back.run_angle(-350, 380)
    pd.action_back.run_angle(350, 200)
    # db.straight(5000)
    # pd.action_back.stop()
    db.straight(100)
    db.straight(-160)
    pd.action_front.run_angle(-350, 100)
    db.settings(950, 1500)
    db.straight(-200)
    pd.drive_base.settings(straight_speed=250, straight_acceleration=500)
    yaw(-25)
    db.straight(220)
    yaw(0)
    db.straight(-190)
    db.settings(500)
    yaw(-20)
    db.straight(270)
    yaw(7)
    db.straight(1000)
    # db.curve(1000, -10)
if __name__ == "__main__":
    for element in  drive3(PupDevices()): pass