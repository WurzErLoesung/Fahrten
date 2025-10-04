from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
from pupdevices import PupDevices
from yaw import Yaw


hub = PrimeHub()

print(f"{hub.system.name()}: {hub.battery.voltage()} mV")
print(f"{hub.system.name()}: {hub.battery.current()} mA")

watch = StopWatch()

hub.speaker.beep()

def trolley(pd):
    #DriveBase initialisieren

    pd.drive_base.use_gyro(True)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(500, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    yield True

    # Drive to trolley
    pd.drive_base.straight(420)
    yaw(65)
    pd.drive_base.straight(420)
    
    # Activate trolley
    yaw(12) #20
    pd.drive_base.straight(-24)
    pd.action_left.run_angle(-1000, 1450)

    # Pick up artefact
    yaw(10)#15
    pd.drive_base.straight(150)#155
    pd.action_right.run_angle(2000, 1000)
    pd.action_right.run_angle(-2000, 1000)

    # Activate statue
    pd.drive_base.straight(-20)
    pd.action_left.run_angle(500, 300)
    pd.drive_base.straight(-80)
    yaw(-45)
    pd.drive_base.straight(25)
    pd.action_left.run_angle(-500, 300)
    pd.drive_base.straight(-40)
    pd.action_left.run_angle(1050, 450)
    yaw(-65)
    pd.action_left.run_angle(1050, 450)

    # Drive home
    pd.drive_base.settings(900, 500)
    pd.drive_base.straight(30)
    yaw(255)
    pd.drive_base.straight(290)
    yaw(200)
    pd.drive_base.straight(820)
    
    yield False
    print("Fahrt hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()

def test(pd):
    #DriveBase initialisieren

    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(200, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    yield True



if __name__ == "__main__":
    for element in trolley(PupDevices()): pass
    # for element in trolley(PupDevices()): pass

