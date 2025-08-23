from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
from pupdevices import PupDevices
from yaw import Yaw


hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")

watch = StopWatch()

hub.speaker.beep()

def trolley(pd):
    #DriveBase initialisieren

    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(200, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    yield True

    pd.drive_base.straight(620)
    yaw(80)
    pd.drive_base.straight(355)
    yaw(25)
    pd.drive_base.straight(-10)
    pd.action_left.run_angle(-300, 500)
    pd.drive_base.straight(10)
    yaw(10)
    pd.drive_base.straight(145)
    pd.action_right.run_angle(2000, 1000)
    pd.action_right.run_angle(-2000, 1000)
    pd.drive_base.straight(-100)
    pd.drive_base.settings(900, 500)
    yaw(80)
    pd.drive_base.straight(-155)
    yaw(30)
    pd.drive_base.straight(-820)



   
    
    yield False
    print("Fahrt hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()


if __name__ == "__main__":
    for element in trolley(PupDevices()): pass