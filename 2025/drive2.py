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
    pd.drive_base.settings(straight_speed=900, straight_acceleration=500)
    hub.speaker.beep()
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)

    #Korallenbaum
    pd.drive_base.straight(190)
    yield True
    pd.action_back.run_angle(500, 250)
    yield True
    # action_arc(pd.drive_base, -1, pd.action_back, 27, 200, 90, 30, 15)
    action_arc(pd.drive_base, -1, pd.action_back, 20, 182, 92, 30, 20)
    yield True
    pd.action_back.run_angle(500, -430)
    yield True
    pd.drive_base.straight(-95)
    yield True

    # zu Schiffwrack
    yaw(-130)  # 130
    yield True
    pd.drive_base.straight(-325)  # -327
    yield True
    # pd.drive_base.turn(-57
    yaw(-90)
    yield True

    pd.drive_base.settings(100)
    pd.drive_base.straight(-150)
    yield True
    pd.action_front.run_angle(1000, 70)
    yield True
    pd.drive_base.settings(50)
    pd.drive_base.straight(-65)  # -57
    yield True
    pd.action_front.run_angle(1000, -80)  # 1000 -90
    yield True
    pd.drive_base.straight(150)
    yield True
    pd.drive_base.settings(900)

    # Korallenbaum Teil 2
    pd.drive_base.turn(-12)
    yield True
    pd.drive_base.straight(120)
    yield True
    pd.drive_base.straight(-90)  # 90
    yield True
    yaw(0)
    yield True

    # Hai und Taucherin
    pd.drive_base.straight(190)  # 200
    yield True
    yaw(-80)  # -82
    yield True
    pd.action_back.run_angle(1250, -210)
    yield True
    pd.drive_base.straight(140)  # 130
    yield True
    pd.action_back.run_angle(1250, 450)
    yield True

    # Korallenriff + Taucherin abliefern
    pd.drive_base.straight(-90)
    yield True
    yaw(0)
    yield True
    pd.drive_base.straight(-170)
    yield True
    yaw(32)
    yield True
    pd.drive_base.straight(180)
    yield True
    pd.action_back.run_angle(1250, -800)
    yield True
    pd.drive_base.straight(-800)
    yield False

    print("Fahrt 2 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()

if __name__ == "__main__":
    for element in  drive2(PupDevices()): pass
