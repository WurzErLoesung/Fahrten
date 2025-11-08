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

def drive_across_new(pd):
    #DriveBase initialisieren
    pd.drive_base.use_gyro(True)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(400, 300)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    yield True

    #drive to market
    pd.drive_base.straight(160)
    yaw(90)
    pd.drive_base.straight(1105)
    yaw(0)
    
    #solve scale
    pd.drive_base.straight(100)
    pd.drive_base.straight(-190)
    yaw(-2)
    #turn gear
    pd.action_left.run_angle(700, -1500)

    #drive to homebase
    pd.action_left.run_angle(700, 100, wait=False)
    yaw(10)
    pd.drive_base.straight(90)
    yaw(110)
    pd.drive_base.settings(977, 700)
    pd.drive_base.straight(800)

    yield False
    print("Fahrt hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()


if __name__ == "__main__":
    for element in drive_across_new(PupDevices()): pass
