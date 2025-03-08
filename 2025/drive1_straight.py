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

def drive1(pd):
    #DriveBase initialisieren
    default_speed = 400 # 500
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(default_speed, 400)
    pd.action_front.run_angle(300, -10)
    db = pd.drive_base
    yaw = Yaw(hub, pd.left_motor, pd.right_motor, max_velocity=400) # 500
    watch = StopWatch()
    yield True

    # unknown ocean creature (der/die/das Kaktopus)
    wait(5000)
    db.straight(-700) # -170
    print("Fahrt1 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    yield False


if __name__ == "__main__":
    pd = PupDevices()
    pd.hub.speaker.beep(duration=200)
    for element in drive1(pd): pass