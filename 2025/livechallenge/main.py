from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
from yaw import Yaw

m = Motor(Port.A)
action = Motor(Port.E)
distance = UltrasonicSensor(Port.C)

hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")

watch = StopWatch()

hub.speaker.beep()


def live_challenge():
    action.run_angle(400, -70)
    action.run_angle(200, -80)

    print("LiveChallenge Programm hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()



if __name__ == "__main__":
    live_challenge()
