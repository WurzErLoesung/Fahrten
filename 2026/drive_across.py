from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
from pupdevices_new import PupDevicesNew
from yaw import Yaw


hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")

watch = StopWatch()

hub.speaker.beep()

def drive_across(pd):
    #DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(-125)
    pd.drive_base.settings(800, 500)
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)
    yield True

    #pd.drive_base.arc(-50, distance = -150)

    #yaw(-110)
    pd.drive_base.straight(-450)
    yaw(-90)
    pd.drive_base.straight(-750)
    pd.drive_base.arc(200, distance=-800)
    yield False
    print("Fahrt hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()


if __name__ == "__main__":
    for element in drive_across(PupDevicesNew()): pass