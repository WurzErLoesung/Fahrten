from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import (ColorSensor, ForceSensor, Motor,
                                 UltrasonicSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, run_task, wait

from pupdevices import PupDevices
from yaw_old import Yaw

hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")
print(hub.system.name())

watch = StopWatch

hub.speaker.beep()


def brush(pd):
    #DriveBase initialisieren

    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(950, 950)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor, min_velocity=200, max_velocity=600, acceleration=950)
    yield True


    pd.drive_base.straight(100)
    yaw(16)
    pd.drive_base.straight(505)
    yaw(-90)
    pd.drive_base.straight(120)
    pd.action_left.run_angle(1000, -350)
    pd.action_left.run_angle(800, 350, wait=False)
    pd.action_right.run_angle(300, 260)
    pd.action_right.run_angle(600, -970)
    pd.action_right.run_angle(800, 450)
    
    pd.drive_base.straight(-120)
    yaw(20)
    pd.drive_base.straight(-620)




    yield False
    print("Fahrt hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()


if __name__ == "__main__":
    for element in brush(PupDevices()):
        pass
