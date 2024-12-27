from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from action_arc import action_arc
from pupdevices import PupDevices

pd = PupDevices()
hub = PrimeHub() 
watch = StopWatch()

#DriveBase initialisieren
wheel_diameter = 56
axle_track = 113
drive_base = DriveBase(pd.left_motor, pd.right_motor, wheel_diameter, axle_track)
drive_base.use_gyro(True)
drive_base.settings(straight_speed=900, straight_acceleration=500, turn_rate=100)
StopWatch = watch
hub.speaker.beep()

def drive4():
    # Dreizack
    drive_base.straight(-360)
    yield True
    drive_base.turn(20)
    yield True
    drive_base.straight(-130)
    yield True
    drive_base.turn(-20)
    yield True
    drive_base.straight(-75)
    yield True
    drive_base.turn(-8)
    yield True
    drive_base.straight(-25)
    yield True
    drive_base.turn(-8)
    yield True
    drive_base.straight(-500)
    yield True
    pd.action_back.run_time(500, 2500)
    yield True
    pd.action_back.run_angle(50, -240)
    yield True
    drive_base.straight(150)
    yield True
    drive_base.turn(90)
    yield True
    drive_base.straight(400)
    yield False

    print("Fahrt 4 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()


if __name__ == "__main__":
    drive4()
