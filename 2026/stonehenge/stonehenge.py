from pupdevices import PupDevices
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import (ColorSensor, ForceSensor, Motor,
                                 UltrasonicSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, run_task, wait
from yaw import Yaw

hub = PrimeHub()

print(f"{hub.system.name()}: {hub.battery.voltage()} mV")
print(f"{hub.system.name()}: {hub.battery.current()} mA")

watch = StopWatch()

hub.speaker.beep()


def stonehenge(pd):
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(straight_speed=777, straight_acceleration=700)
    yaw = Yaw(
        hub,
        pd.right_motor,
        pd.left_motor,
        min_velocity=100,
        max_velocity=400,
        acceleration=500,
    )
    yield True

    # driving to stonehenge
    pd.drive_base.straight(50)
    yield True
    yaw(-15)  # -18
    yield True
    pd.drive_base.straight(555)  # 550 553
    yield True
    yaw(0)
    yield True
    pd.drive_base.straight(40)
    yield True
    yaw(43)  # 45 42
    yield True
    pd.drive_base.straight(300)
    yield True

    # solving everything
    pd.action_left.run_angle(590, -850)  # -610 690 820
    yield True
    pd.action_left.run_angle(600, 1480)  # 1470
    yield True
    pd.action_left.run_angle(600, -250)  # -200
    yield True
    for i in range(2):
        pd.action_right.run_angle(1000, -640)  # 600
        yield True
        pd.action_right.run_angle(100, 360)  # 350
        yield True

    # driving back to homebase
    pd.drive_base.straight(-240)
    yield True
    yaw(0)
    yield True
    pd.drive_base.straight(-40)
    yield True
    yaw(-25)
    yield True
    pd.drive_base.straight(-400)
    yield True
    yaw(-45)
    yield True
    pd.drive_base.straight(-300)
    yield True

    yield False
    print("Fahrt hat " + str(watch.time() / 1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()


if __name__ == "__main__":
    for element in stonehenge(PupDevices()):
        pass
