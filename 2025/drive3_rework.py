from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from pupdevices import PupDevices
from yaw import Yaw


hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")

watch = StopWatch()

hub.speaker.beep()

def drive3(pd):
    #DriveBase initialisieren
    default_speed = 350 # 250
    turn_velocity = 100
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(default_speed, 500)
    pd.action_front.run_angle(300, -10)
    db = pd.drive_base
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)
    watch = StopWatch()
    yield True

    # Trident, shark and corals
    db.settings(100, 50)
    db.straight(150)
    yaw(-35, max_velocity=turn_velocity)
    yaw(0, max_velocity=turn_velocity)
    db.settings(default_speed, 500)
    db.straight(410) # 570
    yaw(-48) # -45
    db.straight(175)
    pd.action_back.run_angle(-300, 360)
    db.settings(150)
    wait(250)
    db.straight(-200)
    db.settings(default_speed)
    db.straight(-60)
    yaw(0)
    db.settings(600, 900)
    db.straight(-650)

    print("Fahrt5 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()
    print(pd.timer.time())

    # db.straight(180)
    # yaw(80, max_velocity=turn_velocity)
    # db.straight(545)
    # yaw(45, max_velocity=turn_velocity)
    # db.straight(140) #200
    # pd.action_back.run_angle(-300, 360)
    # db.straight(-200)
    # yaw(80)
    # db.settings(300)
    # db.straight(-600)
    # db.straight(290) #240
    # db.straight(-40)
    # db.settings(900, 900)
    # db.straight(40)
    # db.settings(default_speed, 500)
    # db.straight(-400)
    # yaw(90)
    # db.straight(-800)
    





if __name__ == "__main__":
    pd = PupDevices()
    pd.hub.speaker.beep(duration=200)
    for element in drive3(pd): pass