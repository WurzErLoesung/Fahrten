from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from action_arc import action_arc
from pupdevices import PupDevices
from yaw import Yaw

hub = PrimeHub() 
watch = StopWatch()


def drive5(pd):
    #DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(straight_speed=900, straight_acceleration=600, turn_rate=100)
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)
    StopWatch = watch
    hub.speaker.beep()
    db = pd.drive_base

    # Dreizack
    db.straight(320)
    yaw(-30)
    db.straight(130)
    pd.action_back.run_angle(800, 2.5*360)
    yaw(-20)
    db.straight(-330)
    db.straight(580)
    yaw(-135)
    db.straight(-250)
    pd.action_front.run_angle(300, 90)
    wait(500)
    pd.action_front.run_angle(-300, 110)
    db.straight(310)
    yaw(-74)
    pd.action_back.run_angle(-800, 2.7*360)
    db.straight(520)
    pd.action_back.run_angle(800, 2.4*360)
    while 120 * 1000 < pd.timer.time() < 149 * 1000:
        wait(100)
        yield True
    yaw(-135)
    print("Fahrt5 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()
    print(pd.timer.time())


if __name__ == "__main__":
    for element in drive5(PupDevices()): pass