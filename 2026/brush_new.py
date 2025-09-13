from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
from pupdevices import PupDevices
from yaw import Yaw


hub = PrimeHub()

print(f"{hub.system.name()}: {hub.battery.voltage()} mV")
print(f"{hub.system.name()}: {hub.battery.current()} mA")

watch = StopWatch()

hub.speaker.beep()

def brush_new(pd):
    #DriveBase initialisieren

    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(950, 950)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor, min_velocity=100, max_velocity=500, acceleration=800)
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

def test(pd):
    #DriveBase initialisieren

    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(200, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    yield True


if __name__ == "__main__":
    for element in brush_new(PupDevices()): pass
