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

    # yellow non-submarine
    db.straight(320)
    yield True
    yaw(-30)
    yield True
    db.straight(130)
    yield True
    pd.action_back.run_angle(800, 2.5*360)
    yield True
    yaw(-20)
    yield True

    # do to big whale and reset action back
    db.straight(-330)
    yield True
    db.straight(580)
    yield True
    yaw(-135)
    yield True
    pd.action_back.run(-840)
    yield True
    db.straight(-250)
    yield True
    pd.action_back.stop()
    yield True
    pd.action_front.run_angle(300, 90)
    yield True
    wait(500)
    yield True
    pd.action_front.run_angle(-300, 110)
    yield True

    # annoy enemies
    db.straight(310)
    yield True
    yaw(-74)
    yield True
    #pd.action_back.run_angle(-800, 2.7*360)
    db.straight(520)
    yield True
    while 120 * 1000 < pd.timer.time() < 145 * 1000:
        wait(100)
        yield True
    if pd.timer.time() > 145 * 1000: 
        pd.action_back.run_angle(800, 2.4*360)
        yield True
    while 120 * 1000 < pd.timer.time() < 149 * 1000:
        wait(100)
        yield True

    # finish drive 5 with kaktopus
    yaw(-135)
    print("Fahrt5 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    yield False


if __name__ == "__main__":
    for element in drive5(PupDevices()): pass