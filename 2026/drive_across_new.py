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
    pd.drive_base.settings(500, 400)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor, min_velocity=100, max_velocity=600, acceleration=400)
    yield True

    #drive to market
    pd.drive_base.straight(160)
    yaw(90)
    pd.drive_base.straight(1105)
    yaw(0)
    
    #solve scale
    pd.drive_base.straight(110)
    pd.drive_base.straight(-200)
    yaw(-4)
    #turn gear
    pd.action_left.run_angle(700, -1500)

    #drive to homebase
    pd.action_left.run_angle(700, 130, wait=False)
    yaw(8)
    pd.drive_base.straight(50)
    #pd.drive_base.straight(-20)
    yaw(105)
    pd.drive_base.settings(977, 700)
    pd.drive_base.straight(800)

    yield False
    print("Fahrt hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()


if __name__ == "__main__":
    for element in drive_across_new(PupDevices()): pass
