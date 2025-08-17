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

def drive4(pd):
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(500, 500)
    yaw = Yaw(hub, pd.left_motor, pd.right_motor, positive_direction=-1)
    yield True

    pd.action_right.run_until_stalled(-400, then=Stop.COAST, duty_limit=35)
    pd.drive_base.straight(390)
    for i in range(3):
        pd.action_right.run_angle(1500, 150)
        wait(250)
        pd.action_right.run_angle(1500, -170)
        wait(250)
    yield True
    pd.action_right.run_until_stalled(-400, then=Stop.COAST, duty_limit=35)

    pd.drive_base.straight(-100)
    yaw(-30)
    pd.drive_base.straight(460)
    yaw(60)
    pd.drive_base.straight(100)
    pd.action_right.run_angle(100, 150)
    yaw(-40)
    pd.action_right.run_angle(100, -120)
    yaw(-30)
    pd.drive_base.straight(-72)
    yaw(90)
    pd.drive_base.straight(350)
    pd.drive_base.straight(-20)

    

if __name__ == "__main__":
    for element in drive4(PupDevices()): pass
        
