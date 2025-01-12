from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from action_arc import action_arc
from pupdevices import PupDevices
from yaw import Yaw

hub = PrimeHub()
watch = StopWatch()


def drive6(pd):
    #DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.drive_base.settings(straight_speed=900, straight_acceleration=500, turn_rate=60)
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)
    StopWatch = watch
    hub.speaker.beep()

    # Boat
    pd.drive_base.straight(5)
    yield True
    pd.drive_base.straight(-240)
    yield True
    yaw(-28)
    yield True
    pd.drive_base.straight(-125)
    yield True
    yaw(-45)
    yield True
    pd.drive_base.straight(-20)
    yield True
    yaw(-40)
    yield True

    # Lift Boat
    pd.action_front.run_angle(500, -960)
    yield True

    # Yeet Boat
    pd.drive_base.settings(straight_acceleration=5000)
    yield True
    pd.drive_base.straight(200)
    yield True
    pd.drive_base.settings(straight_acceleration=500)
    yield True

    yaw(-55)
    yield True
    pd.drive_base.straight(-250)
    yield True
    yaw(-5)
    yield True
    pd.drive_base.straight(-220)
    yield True
    yaw(45)
    yield True
    pd.drive_base.straight(-180)
    yield True
    pd.drive_base.settings(straight_speed=40)
    pd.drive_base.straight(-60)
    yield True
    pd.drive_base.settings(straight_speed=900)
    pd.drive_base.straight(-5)
    yield True
    pd.drive_base.settings(straight_speed=40)
    yield True
    pd.action_front.run_angle(500, 960)
    yield True
    yield True
    pd.drive_base.straight(20)
    yield True
    pd.drive_base.settings(straight_speed=900)
    yield True

    # drive to whales
    pd.drive_base.straight(170)
    yield True
    yaw(135)
    yield True
    pd.drive_base.straight(75)
    yield True
    yield True

    # solve whales
    pd.action_back.run_angle(1500, -590)
    yield True
    pd.action_back.run_angle(200, -530)
    yield True

    # drive to end
    wait(500)
    yield True
    pd.drive_base.straight(-30)
    yield True
    wait(1500)
    yield True
    pd.drive_base.straight(-100)
    yield True
    pd.action_back.run_angle(1500, 390)
    yield True
    yaw(217)
    yield True
    pd.drive_base.straight(-50)
    yield True
    yaw(285)
    yield True
    pd.drive_base.straight(-670)
    yield True

    # end
    pd.action_front.run_angle(500, -960)
    yield False

    print("Fahrt 6 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()
    print(pd.timer.time())


if __name__ == "__main__":
    for element in drive6(PupDevices()): pass