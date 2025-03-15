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

def drive1(pd):
    #DriveBase initialisieren
    default_speed = 600 # 250
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(default_speed, 400)
    pd.action_front.run_angle(300, -10)
    db = pd.drive_base
    yaw = Yaw(hub, pd.left_motor, pd.right_motor, max_velocity=500)
    watch = StopWatch()
    yield True

    # unknown ocean creature (der/die/das Kaktopus)
    db.straight(-170) # -170
    yield True
    yaw(-45)
    yield True
    db.straight(-481)
    yield True
    db.straight(400)
    yield True

    # collect stuff in front of big whale
    yaw(-25) # -27 before # -25
    yield True
    db.straight(-400)
    yield True
    yaw(45)
    yield True
    db.straight(-200)
    yield True
    db.straight(180) # 200 # 230
    yield True

    # get the carrot
    yaw(-97) # -110
    yield True
    db.settings(150)  
    db.straight(120) # 180
    yield True
    db.settings(default_speed)
    db.straight(-210) # -160
    yield True

    # anglerfish
    yaw(-58)
    yield True
    db.straight(-155) # -240
    yield True
    yaw(-91, max_velocity=200)
    yield True
    db.straight(-580)
    yield True

    # anker
    yaw(-110) # -110
    yield True
    db.straight(300)
    yaw(-90) # -90
    db.straight(-250)
    yield True
    yaw(-120)
    yield True
    db.straight(-160)
    yield True

    # ocean probe and coral reef
    db.settings(100)
    yaw(-95)
    yield True
    db.straight(-245)
    yield True
    db.straight(25)
    yield True
    # yaw(-90)
    pd.action_back.run_angle(800, -200)
    yield True
    # db.straight(-30)
    pd.action_back.run_angle(800, 200)
    yield True

    # Shark
    # yaw(-95)
    db.settings(default_speed)
    db.straight(-90)
    yield True
    yaw(-57)
    yield True
    pd.action_front.run_angle(800, 190)
    yield True

    # Diver(in)
    pd.action_front.run_angle(100, -150)
    yield True
    # db.straight(50)
    yaw(-87) # -85,5
    yield True
    db.straight(-35) # -40
    
    yield True
    yaw(-89)
    yield True
    pd.action_front.run_angle(200, 90)
    wait(250)
    pd.action_front.run_angle(200, -90)

    # Collect remaining stuff and get da fuq outta here
    # pd.action_front.run_angle(120, -50)
    yield True
    db.straight(130)
    yield True
    yaw(-148, max_velocity=300)
    yield True
    # db.curve(-1500, -70)
    db.straight(-900)
    # db.straight(120) #before 100
    # yaw(-155) #148
    # db.straight(-850)
    
    print("Fahrt1 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    yield False


if __name__ == "__main__":
    pd = PupDevices()
    pd.hub.speaker.beep(duration=200)
    for element in drive1(pd): pass