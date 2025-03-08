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
    pd.drive_base.settings(straight_speed=500, straight_acceleration=500)
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)

    #pd.action_back.run_angle(900, 400)

    pd.drive_base.settings(straight_speed=500)
    pd.drive_base.straight(-265)
    pd.drive_base.straight(50)
    yaw(-25)
    pd.drive_base.straight(150)
    yaw(0)
    pd.drive_base.straight(-300)
    pd.drive_base.straight(-200)
    yaw(20)
    pd.drive_base.straight(900)

if __name__ == "__main__":
    for element in  drive3(PupDevices()): pass