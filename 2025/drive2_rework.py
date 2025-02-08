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

def drive2(pd):
    #DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(straight_speed=500, straight_acceleration=500)
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)

    # Zur Taucherin
    pd.drive_base.straight(-180)
    yaw(25)
    pd.drive_base.straight(-370)

    #Taucherin abliefern
    pd.action_front.run_angle(400, 325)
    pd.drive_base.straight(70)
    pd.action_front.run_angle(800, -325)

    #Korallenknospen
    yaw(-20)
    pd.drive_base.straight(-50)
    pd.drive_base.straight(47)

    #Korallenbaum
    yaw(90)
    pd.drive_base.straight(-5)
    pd.action_back.run_angle(400, 575)
    pd.action_back.run_angle(500, -200)

    # Zum Schiffswrack
    yaw(70)
    pd.drive_base.straight(90)
    yaw(90)
    pd.drive_base.straight(-350)
    
    # Shrimp
    pd.action_front.run_angle(900, 550)
    pd.drive_base.straight(200)
    yaw(35)
    pd.drive_base.straight(550)

if __name__ == "__main__":
    for element in  drive2(PupDevices()): pass