from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
from pupdevices_new import PupDevices
from yaw import Yaw


hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")

watch = StopWatch()

hub.speaker.beep()

def crane(pd):
    #DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(-90)
    pd.drive_base.settings(250, 500)
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)
    yield True


    pd.drive_base.straight(-680)
    yield True

    pd.action_left.run_time(-1000, 1400)
    yield True

    yaw(-163)
    pd.drive_base.straight(80)

    pd.drive_base.straight(-80)

    yaw(-112)
    pd.drive_base.straight(300)

    pd.drive_base.straight(-100)

    yaw(-80)

    pd.drive_base.settings(700)
    
    pd.drive_base.straight(500)

    
    yield False
    print("Fahrt hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()


if __name__ == "__main__":
    for element in crane(PupDevices()): pass