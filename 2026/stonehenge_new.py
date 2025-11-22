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

def stonehenge(pd):
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(straight_speed=777, straight_acceleration=700)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor, min_velocity=100, max_velocity=400, acceleration=500)
    # driving to stonehenge
    pd.drive_base.straight(500)
    wait(1000)
    pd.drive_base.straight(-500)
    return

    pd.drive_base.straight(50)
    yaw(-18)
    pd.drive_base.straight(550)
    yaw(0)
    pd.drive_base.straight(40)
    yaw(45)
    pd.drive_base.straight(300)

    # solving everything
    pd.action_left.run_angle(600, -660)
    pd.action_left.run_angle(600, 1200)
    pd.action_left.run_angle(600, -200)
    for i in range(3):
        pd.action_right.run_angle(1000, -600)
        pd.action_right.run_angle(100, 350)
    yield True

    # driving back to homebase
    pd.drive_base.straight(-240)
    yaw(0)
    pd.drive_base.straight(-40)
    yaw(-25)
    pd.drive_base.straight(-400)
    yaw(-45)
    pd.drive_base.straight(-300)
    
    
    
    

if __name__ == "__main__":
    for element in stonehenge(PupDevices()): pass
