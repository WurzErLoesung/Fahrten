from pupdevices import PupDevices
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import (ColorSensor, ForceSensor, Motor,
                                 UltrasonicSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, run_task, wait
from yaw import Yaw

hub = PrimeHub()
print(f"{hub.battery.voltage()/1000} Volt")
watch = StopWatch()
hub.speaker.beep()


def drive_across_new(pd):
    # DriveBase initialisieren
    pd.drive_base.use_gyro(True)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(600, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    yield True
    # bring 3 items to forum
    pd.drive_base.straight(190)
    yield True
    yaw(51)
    yield True
    pd.drive_base.straight(330) #335
    yield True
    pd.drive_base.straight(-250)
    yield True
    yaw(90)
    yield True
    pd.drive_base.straight(750)
    yield True
    pd.action_right.run_angle(700, 455, wait=False)
    yield True
    yaw(141)
    yield True
    pd.drive_base.straight(-90) #-85
    yield True
    pd.action_right.run_angle(600, -500)
    yield True
    yaw(45)
    yield True
    pd.drive_base.straight(200) #220
    yield True
    pd.drive_base.straight(-280) #-300
    yield True
    yaw(112)
    yield True
    pd.drive_base.settings(900, 900)
    pd.drive_base.straight(1050)

    yield False
    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()


if __name__ == "__main__":
    for element in drive_across_new(PupDevices()):
        pass
