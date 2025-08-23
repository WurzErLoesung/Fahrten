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

def drive_across(pd):
    #DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(-125)
    pd.drive_base.settings(800, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    yield True

    #pd.drive_base.arc(-50, distance = -150)

    #yaw(-110)
    pd.drive_base.straight(470)
    yaw(-90)
    pd.drive_base.straight(740)
    pd.drive_base.arc(400, distance=800)
    yield False
    print("Fahrt hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()


if __name__ == "__main__":
    for element in drive_across(PupDevices()): pass
