from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from action_arc import action_arc
from yaw import Yaw

hub = PrimeHub()
# Motoren initialisieren 
left_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE) 
right_motor = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)

action_front = Motor(Port.C)
action_back = Motor(Port.A)

ultra = UltrasonicSensor(Port.E)
color = ColorSensor(Port.D)
watch = StopWatch()
yaw = Yaw(hub, left_motor, right_motor)

#DriveBase initialisieren
wheel_diameter = 56 
axle_track = 113 
drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
drive_base.use_gyro(False) 
drive_base.settings(straight_speed=400, straight_acceleration=500)
StopWatch = watch
hub.speaker.beep()


def drive5():
    drive_base.straight(115)
    yield True
    drive_base.settings(400)
    yield True
    drive_base.straight(-125)
    yield True

    wait(10000)
    yield True

    # Boot hinschieben
    drive_base.settings(100)
    yield True
    drive_base.straight(200)
    yield True
    drive_base.settings(300)
    yield True
    drive_base.straight(700)
    yield True

    # Krabben aufstellen
    drive_base.straight(-225)
    yield True
    action_back.run_angle(360, 360)
    yield True
    drive_base.straight(-100)
    yield True
    drive_base.settings(900)
    yield True

    # zu blauer Base
    yaw(-30)
    yield True
    drive_base.straight(-50)
    yield True
    action_front.run_angle(1250, 850) # Schieber abwerfen
    yield True
    drive_base.settings(800)
    yield True
    drive_base.straight(350)
    yield True
    yaw(5)
    yield True
    drive_base.straight(900)
    yield False

    print("Fahrt 2 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()


if __name__ == "__main__":
    drive5()
