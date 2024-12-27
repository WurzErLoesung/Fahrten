from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from action_arc import action_arc

hub = PrimeHub()
watch = StopWatch()

#DriveBase initialisieren
wheel_diameter = 56
axle_track = 113
drive_base = DriveBase(pd.left_motor, pd.right_motor, wheel_diameter, axle_track)
drive_base.use_gyro(False)
drive_base.settings(straight_speed=900, straight_acceleration=500, turn_rate=60)
StopWatch = watch
hub.speaker.beep()


def drive6():
    # Boat
    drive_base.straight(-5)
    yield True
    drive_base.straight(240)
    yield True
    drive_base.turn(-28)
    yield True
    drive_base.straight(125)
    yield True
    drive_base.turn(-17)
    yield True
    drive_base.straight(20)
    yield True
    drive_base.turn(10)
    yield True

    # Lift Boat
    pd.action_front.run_angle(500, -960)
    yield True

    # Yeet Boat
    drive_base.settings(straight_acceleration=5000)
    yield True
    drive_base.straight(-200)
    yield True
    drive_base.settings(straight_acceleration=500)
    yield True

    drive_base.turn(-20)
    yield True
    drive_base.straight(250)
    yield True
    drive_base.turn(50)
    yield True
    drive_base.straight(200)
    yield True
    drive_base.turn(50)
    yield True
    drive_base.straight(250)
    yield True
    pd.action_front.run_angle(500, 960)
    yield True
    drive_base.settings(straight_speed=500)
    yield True
    drive_base.straight(-15)
    yield True
    drive_base.settings(straight_speed=900)
    yield True

    # drive to whales
    drive_base.straight(-180)
    yield True
    drive_base.turn(92)
    yield True
    drive_base.straight(-90)
    yield True

    # solve whales
    pd.action_back.run_angle(1500, -590)
    yield True
    pd.action_back.run_angle(200, -530)
    yield True

    # drive to end
    wait(500)
    yield True
    drive_base.straight(30)
    yield True
    wait(1000)
    yield True
    drive_base.straight(100)
    yield True
    pd.action_back.run_angle(1500, 390)
    yield True
    drive_base.turn(90)
    yield True
    drive_base.straight(50)
    yield True
    drive_base.turn(65)
    yield True
    drive_base.straight(700)
    yield True

    # end
    pd.action_front.run_angle(500, -960)
    yield False

    print("Fahrt 6 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()


if __name__ == "__main__":
    drive6()