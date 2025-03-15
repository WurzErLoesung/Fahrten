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


def live_challenge(pd):
    #DriveBase initialisieren
    pd.db.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.db.settings(250, 500)
    yaw = Yaw(hub, pd.lm, pd.rm)

    pd.db.straight(20)

    print("LiveChallenge Programm hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()



if __name__ == "__main__":
    live_challenge(PupDevices())
