from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import (ColorSensor, ForceSensor, Motor, UltrasonicSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, run_task, wait
from pupdevices import PupDevices
from yaw import Yaw

hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")

watch = StopWatch()

hub.speaker.beep()


def ship(pd):
    # DriveBase initialisieren
<<<<<<< HEAD
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(90)
    pd.drive_base.settings(977, 550)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    yield True

    # pd.action_right.run_angle(950, 330)
    # yield True
    # pd.action_right.run_angle(-900, 715)
    # yield True

    pd.drive_base.arc(2800, distance=650)  # 530
    yield True

    pd.action_right.run_angle(1350, -60, wait=False)
    yield True

    pd.drive_base.settings(977, 977)

    pd.drive_base.straight(-530)
    yield True
=======
    pd.drive_base.use_gyro(True)
    pd.imu.reset_heading(90)
    pd.drive_base.settings(977, 977)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    yield True
    # pd.action_right.run_angle(950, 330)
    # pd.action_right.run_angle(-900, 715)
    pd.drive_base.arc(3500,distance=490) #530
    pd.action_left.run_angle(1500, 60, wait=False)
    pd.drive_base.straight(-515)
>>>>>>> 3b434bf4996006613086d9c4fc55cfb0a7bcdbfb

    yield False
    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    # print(pd.timer.time())
    watch.reset()


if __name__ == "__main__":
    for element in ship(PupDevices()):
        pass
