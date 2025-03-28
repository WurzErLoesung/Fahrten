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
    default_speed = 600
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(straight_speed=default_speed, straight_acceleration=500)
    yaw = Yaw(hub, pd.left_motor, pd.right_motor, max_velocity=400)

    # Zur Taucherin
    pd.drive_base.straight(-170)
    yield True
    yaw(25)
    yield True
    pd.drive_base.straight(-270)
    yaw(-15)
    yaw(24)
    pd.drive_base.straight(-105)
    yield True

    #Taucherin abliefern
    pd.action_front.run_angle(400, 330)
    yield True
    # yaw(25)
    pd.drive_base.straight(75) # 55
    yield True
    # pd.action_front.run_angle(800, -325)
    yield True

    #Korallenknospen
    # pd.action_front.run(-800)
    # yaw(-18) #-20
    # pd.action_front.stop()
    # yield True
    # # return
    # # pd.drive_base.straight(-45)
    # yield True
    # yaw(-10)
    # return
    # pd.drive_base.straight(15) # 50
    # yield True
    # # return

    #Korallenbaum
    pd.action_front.run(-400)
    yaw(90.2, max_velocity=300) # 90
    pd.action_front.stop()
    yield True
    # pd.drive_base.straight(7) # -5
    # yield True
    # wait(5_000)
    # wait(250)
    pd.action_back.run_angle(100, 150)
    yaw(90, max_velocity=300) # 90
    pd.action_back.run_angle(500, 425)
    yield True
    pd.action_back.run_angle(500, -200)
    yield True
    # wait(250)
    # wait(5_000)

    # Zum Schiffswrack
    yaw(70)
    yield True
    pd.drive_base.straight(90) # 90 # 110
    yield True
    yaw(90)
    yield True
    pd.drive_base.straight(-460) # -350 # -380
    pd.drive_base.straight(30) # 0
    
    # Shrimp
    pd.action_front.run_angle(900, 750) # 550
    yield True
    pd.drive_base.straight(200)
    yield True
    yaw(35)
    yield True
    pd.drive_base.straight(650)
    yield False

if __name__ == "__main__":
    for element in  drive2(PupDevices()): pass
