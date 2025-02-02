from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from pupdevices import PupDevices
from yaw import Yaw


hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")

watch = StopWatch()

hub.speaker.beep()

def drive1(pd):
    #DriveBase initialisieren
    default_speed = 300 # 250
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(default_speed, 500)
    pd.action_front.run_angle(300, -10)
    db = pd.drive_base
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)
    yield True

    # unknown ocean creature
    db.straight(-170)
    yaw(-45)
    db.straight(-495)
    db.straight(400)
    yield True

    # collect stuff
    yaw(-25)
    db.straight(-350)
    yaw(35)
    db.straight(-160)
    db.straight(155)
    yield True
    
    # wales
    yaw(-40)
    db.straight(-40) # -20
    pd.action_front.run_angle(800, 140)
    wait(50)
    pd.action_front.run_angle(100, 40)
    db.straight(-60) # -90
    yaw(-25)
    db.straight(125)
    pd.action_front.run_angle(800, -160)
    db.straight(-60)
    yield True

    # carrot
    yaw(-97)
    db.straight(150)
    db.straight(-160)
    yield True
    
    # anglerfish
    yaw(-75)
    db.straight(-255)
    yaw(-95)
    db.straight(-520)
    yield True

    # anker
    yaw(-105)
    db.straight(210)
    yaw(-45)
    db.straight(70)
    yaw(-50)
    db.straight(-55)
    yield True

    # coral reef and shark
    yaw(-93)
    db.straight(-550)
    pd.action_back.run_angle(-800, 130)
    pd.action_back.run_angle(800, 130)
    db.settings(straight_speed=100)
    db.straight(-55)
    db.settings(straight_speed=default_speed)
    yaw(-75)
    yield True

    pd.action_front.run_angle(800, 160)
    pd.action_front.run_angle(-800, 140)
    yield True

    # collect remaining stuff and get da fuq outta here
    db.straight(90)
    yaw(-150)
    db.straight(-850)
    yield True
    





if __name__ == "__main__":
    pd = PupDevices()
    pd.hub.speaker.beep(duration=200)
    for element in drive1(pd): pass