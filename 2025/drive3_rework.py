from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from pupdevices import PupDevices
from yaw import Yaw


hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")

watch = StopWatch()

hub.speaker.beep()

def drive3(pd):
    #DriveBase initialisieren
    default_speed = 600 # 350
    turn_velocity = 100
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(default_speed, 500)
    pd.action_front.run_angle(300, -10)
    db = pd.drive_base
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)
    watch = StopWatch()
    yield True

    # Trident, shark and corals
    db.settings(100, 50)
    db.straight(150)
    yield True
    yaw(-35, max_velocity=turn_velocity)
    yield True
    yaw(0, max_velocity=turn_velocity)
    yield True
    db.settings(default_speed, 500)
    db.straight(425) # 570
    yield True
    yaw(-48) # -45
    yield True
    db.straight(175)
    yield True
    pd.action_back.run_angle(-300, 360)
    yield True
    db.settings(150)
    wait(250)
    yield True
    db.straight(-200)
    yield True
    db.settings(default_speed)
    db.straight(-60)
    db.straight(20)
    yield True
    yaw(0)
    yield True
    db.settings(600, 900)
    db.straight(-750)

    print("Fahrt3 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()
    print(pd.timer.time())
    yield False


if __name__ == "__main__":
    pd = PupDevices()
    pd.hub.speaker.beep(duration=200)
    for element in drive3(pd): pass