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
    default_speed = 600 # 350
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(straight_speed=150, straight_acceleration=500)
    db = pd.drive_base


    yaw = Yaw(hub, pd.left_motor, pd.right_motor, max_velocity=400)

    # grab load
    pd.action_front.run_angle(350, 100)
    yield True

    # drop load into boat and move it
    # db.straight(150)
    db.straight(400)
    yield True
    pd.action_back.run_angle(350, 360)
    yield True
    db.settings(default_speed)
    db.straight(470)
    yield True

    # move tower
    pd.action_back.run_angle(-350, 340)
    yield True
    pd.action_back.run_angle(350, 200)
    yield True
    # db.straight(5000)
    # pd.action_back.stop()

    # finish boat, solve half of the tower, drop load box
    db.straight(100)
    yield True
    db.straight(-160)
    yield True
    pd.action_front.run_angle(-550, 80)
    yield True
    db.settings(950, 1500)
    db.straight(-200)
    yield True

    # finish tower
    pd.drive_base.settings(straight_speed=default_speed, straight_acceleration=500)
    pd.action_back.run_angle(350, -220)
    yaw(-25)
    yield True
    db.straight(220)
    yield True
    yaw(0)
    yield True
    db.straight(-190)
    yield True

    # leave
    yield True
    yaw(-20)
    yield True
    db.straight(350) # 270
    yield True
    yaw(7)
    yield True
    db.straight(1300)
    # db.curve(1000, -10)
    yield False
    
if __name__ == "__main__":
    for element in  drive3(PupDevices()): pass