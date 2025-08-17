from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
from pupdevices import PupDevices
from yaw import Yaw


hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")
print(hub.system.name())

watch = StopWatch

hub.speaker.beep()

def drive1(pd):
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(500, 400)
    yaw = Yaw(hub, pd.left_motor, pd.right_motor, positive_direction=-1)
    yield True

    pd.drive_base.straight(670)
    pd.drive_base.straight(-150)
    pd.drive_base.straight(100)
    pd.action_left.run_angle(1000, 700)
    yield True

    pd.drive_base.straight(-100)
    yaw(45)
    pd.drive_base.straight(170)
    yaw(-47)
    pd.action_right.run_angle(1000, -170)
    pd.drive_base.straight(170)
    pd.action_right.run_angle(1000, -40)
    pd.drive_base.straight(170)
    pd.action_right.run_angle(1000, 180)
    pd.drive_base.straight(-200)
    yaw(20)
    pd.drive_base.straight(-800)
    print(pd.timer.time())
    yield True

if __name__ == "__main__":
    for element in drive1(PupDevices()): pass
        
