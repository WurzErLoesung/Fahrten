from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from action_arc import action_arc
from yaw import Yaw
from pupdevices import PupDevices

pd = PupDevices()
hub = PrimeHub()

yaw = Yaw(hub, pd.left_motor, pd.right_motor)

watch = StopWatch()

#DriveBase initialisieren
wheel_diameter = 56
axle_track = 113
drive_base = DriveBase(pd.left_motor, pd.right_motor, wheel_diameter, axle_track)
drive_base.use_gyro(False)
drive_base.settings(straight_speed=900, straight_acceleration=500)
StopWatch = watch
hub.speaker.beep()


def drive2():
    # Korallenbaum
    drive_base.straight(190)
    yield True
    pd.action_back.run_angle(500, 250)
    yield True
    # action_arc(drive_base, -1, pd.action_back, 27, 200, 90, 30, 15)
    action_arc(drive_base, -1, pd.action_back, 20, 182, 92, 30, 20)
    yield True
    pd.action_back.run_angle(500, -430)
    yield True
    drive_base.straight(-95)
    yield True

    # zu Schiffwrack
    yaw(-130)  # 130
    yield True
    drive_base.straight(-325)  # -327
    yield True
    # drive_base.turn(-57
    yaw(-90)
    yield True

    drive_base.settings(100)
    drive_base.straight(-150)
    yield True
    pd.action_front.run_angle(1000, 70)
    yield True
    drive_base.settings(50)
    drive_base.straight(-65)  # -57
    yield True
    pd.action_front.run_angle(1000, -80)  # 1000 -90
    yield True
    drive_base.straight(150)
    yield True
    drive_base.settings(900)

    # Korallenbaum Teil 2
    drive_base.turn(-12)
    yield True
    drive_base.straight(120)
    yield True
    drive_base.straight(-90)  # 90
    yield True
    yaw(0)
    yield True

    # Hai und Taucherin
    drive_base.straight(190)  # 200
    yield True
    yaw(-80)  # -82
    yield True
    pd.action_back.run_angle(1250, -210)
    yield True
    drive_base.straight(140)  # 130
    yield True
    pd.action_back.run_angle(1250, 450)
    yield True

    # Korallenriff + Taucherin abliefern
    drive_base.straight(-90)
    yield True
    yaw(0)
    yield True
    drive_base.straight(-170)
    yield True
    yaw(32)
    yield True
    drive_base.straight(180)
    yield True
    pd.action_back.run_angle(1250, -800)
    yield True
    drive_base.straight(-800)
    yield False

    print("Fahrt 2 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()

if __name__ == "__main__":
    drive2()
