from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
from yaw import Yaw
from PID import PID

ml, mr = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE), Motor(Port.F)
action = Motor(Port.C)
#ultra = UltrasonicSensor(Port.D)
pid = PID(mr, ml, 56)
db = DriveBase(ml, mr, 56, 113)
hub = PrimeHub()
print(f"{hub.battery.voltage()/1000} Volt")
#watch = StopWatch()



async def live_challenge():
    #Code here
    hub.speaker.beep()
    #db.settings(950)

    await pid.straight(800, 400)

    #db.straight(800)

    #print("LiveChallenge Programm hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    #watch.reset()



if __name__ == "__main__":
    run_task(live_challenge())
