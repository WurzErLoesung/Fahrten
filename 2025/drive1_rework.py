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
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(250, 500)
    pd.action_front.run_angle(300, -10)
    db = pd.drive_base
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)
    yield True

    # unknown ocean creature
    db.straight(-152)
    yaw(-45)
    db.straight(-495)
    db.straight(400)
    yield True

    # collect stuff
    db.straight(-150)
    yaw(0)
    db.straight(-250)
    yaw(45)
    db.straight(-140)
    db.straight(165)
    
    # wales
    yaw(-41)
    db.straight(-20)
    pd.action_front.run_angle(800, 140)
    wait(50)
    pd.action_front.run_angle(100, 40)
    db.straight(-90)
    yaw(-20)
    db.straight(120)
    pd.action_front.run_angle(800, -160)
    db.straight(-60)

    # carrot
    yaw(-95)
    db.straight(140)
    db.straight(-140)
    
    # anglerfish
    yaw(-75)
    db.straight(-300)
    yaw(-95)
    db.straight(-480)

    # anker
    yaw(-105)
    db.straight(200)
    yaw(-45)
    db.straight(50)
    yaw(-90)
    db.straight(-600)
    yaw(-75)
    
    pd.action_back.run_angle(-800, 100)
    pd.action_front.run_angle(800, 160)
    pd.action_back.run_angle(800, 100)
    pd.action_front.run_angle(-800, 140)

    db.straight(150)
    yaw(-135)
    db.straight(-800)
    





if __name__ == "__main__":
    pd = PupDevices()
    pd.hub.speaker.beep(duration=200)
    for element in drive1(pd): pass
