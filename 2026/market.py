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

def market(pd):
    #DriveBase initialisieren

    pd.drive_base.use_gyro(True)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(900, 600)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor, min_velocity=100, max_velocity=450, acceleration=600)
    yield True

    pd.drive_base.straight(60)
    yaw(-45)
    pd.drive_base.straight(485)
    pd.action_right.run_angle(900, 1000, wait=False)
    pd.action_left.run_angle(900, -700)
    pd.drive_base.straight(-150)
    pd.action_left.run_angle(900, 200, wait=False)
    pd.drive_base.straight(70, wait=False)
    wait(500)
    yaw(-60)
    pd.drive_base.straight(-500)

    yield False
    print("Fahrt hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()

if __name__ == "__main__":
    for element in market(PupDevices()): pass
