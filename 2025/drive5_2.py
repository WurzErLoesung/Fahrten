from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from action_arc import action_arc
from yaw import Yaw

hub = PrimeHub()

def drive5_2(pd):
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(straight_speed=400, straight_acceleration=500)
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)
    watch = StopWatch()
    
    #Boot hinschieben
    pd.drive_base.settings(100)
    pd.drive_base.straight(200)
    yield True
    pd.drive_base.settings(300)
    pd.drive_base.straight(700)
    yield True

    #Krabben aufstellen
    pd.drive_base.straight(-225)
    yield True
    pd.action_back.run_angle(-360, 360)
    yield True
    pd.drive_base.straight(-100)
    yield True
    pd.drive_base.settings(900)

    #zu blauer Base
    yaw(-30)
    yield True
    pd.drive_base.straight(-50)
    yield True
    pd.action_front.run_angle(1250, 850) #Schieber abwerfen
    yield True
    pd.drive_base.settings(800)
    pd.drive_base.straight(350)
    yield True
    yaw(5)
    yield True
    pd.drive_base.straight(900)
    yield False

    print("Fahrt 5.2 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()
    print(pd.timer.time())