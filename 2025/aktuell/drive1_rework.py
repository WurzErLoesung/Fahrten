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
    default_speed = 200 # 250
    
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(default_speed, 500)
    pd.action_front.run_angle(300, -10)
    db = pd.drive_base
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)
    yield True

    # unknown ocean creature
    db.straight(-180) # -170
    yield True
    yaw(-45)
    yield True
    db.straight(-480) # -495
    yield True
    db.straight(400)
    yield True

    # collect stuff
    yaw(-25)
    yield True
    db.straight(-350)
    yield True
    yaw(35)
    yield True
    db.straight(-160)
    yield True
    db.straight(155)
    yield True
    
    # wales
    yaw(-35) # -40
    yield True
    
    db.straight(-40)
    yield True
    pd.action_front.run_angle(800, 140)
    yield True
    wait(50)
    yield True
    pd.action_front.run_angle(100, 40)
    yield True
    db.straight(-60)
    yield True
    yaw(-25)
    yield True
    db.straight(125)
    yield True
    pd.action_front.run_angle(400, -160)
    yield True
    db.straight(-55) ## -55
    yield True

    # carrot
    yaw(-100)
    yield True
    db.straight(150)
    yield True
    db.straight(-190) # -160
    yield True
    
    # anglerfish
    yaw(-66) ##-70
    yield True
    db.straight(-255) #-260 # -255
    yield True
    yaw(-95) ##-95
    yield True
    db.straight(-520) ##-525
    yield True

    # anker
    yaw(-105)
    yield True
    db.straight(210)
    yield True
    yaw(-45)
    yield True
    db.straight(70)
    yield True
    yaw(-50)
    yield True
    db.straight(-55) #-55
    yield True

    # coral reef and shark
    yaw(-93)
    yield True
    db.straight(-550)
    yield True
    pd.action_back.run_angle(-800, 130)
    yield True
    pd.action_back.run_angle(800, 130)
    yield True
    db.settings(straight_speed=100)
    db.straight(-55)
    yield True
    db.settings(straight_speed=default_speed)
    yaw(-75)
    yield True

    pd.action_front.run_angle(800, 160)
    yield True
    #pd.action_front.run_angle(-800, 140)
    pd.action_front.run_angle(-100, 45)
    yield True

    yaw(-90)
    yield True
    db.straight(-35)
    yield True
    pd.action_front.run_angle(-100, 100)
    yield True
    db.straight(35)
    yield True

    yaw(-75)
    yield True

    # collect remaining stuff and get da fuq outta here
    db.straight(90)
    yield True
    yaw(-150)
    yield True
    db.straight(-850)
    yield True
    





if __name__ == "__main__":
    pd = PupDevices()
    pd.hub.speaker.beep(duration=200)
    for element in drive1(pd): pass