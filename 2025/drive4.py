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


def drive4(pd):
    #DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(straight_speed=900, straight_acceleration=500, turn_rate=100)
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)
    StopWatch = watch
    hub.speaker.beep()

    # Dreizack
    pd.drive_base.straight(360)
    yield True
    yaw(30)
    yield True
    pd.drive_base.straight(130)
    yield True
    yaw(10)
    yield True
    pd.drive_base.straight(75)
    yield True
    yaw(-4)
    yield True
    pd.drive_base.straight(25)
    yield True
    yield True
    pd.drive_base.straight(500)
    yield True
    pd.action_back.run_time(-500, 2500)
    yield True
    pd.action_back.run_angle(50, 240)
    yaw.reset(0)
    yield True
    pd.drive_base.straight(-150)
    yield True
    yaw(25)
    yield True
    pd.drive_base.straight(-600)
    yield False

    print("Fahrt 4 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()
    print(pd.timer.time())


if __name__ == "__main__":
    for element in drive4(PupDevices()): pass