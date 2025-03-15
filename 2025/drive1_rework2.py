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
    default_speed = 300 # 250
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(default_speed, 400)
    pd.action_front.run_angle(300, -10)
    db = pd.drive_base
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)
    watch = StopWatch()
    yield True

    # unknown ocean creature (der/die/das Kaktopus)
    db.straight(-170) # -170
    yield True
    yaw(-45)
    yield True
    db.straight(-481)
    db.straight(400)

    # collect stuff in front of big whale
    yaw(-25) # -27 before # -25
    db.straight(-400)
    yaw(45)
    db.straight(-200)
    db.straight(210) # 200 # 230

    # do the small wales
    yaw(-28) # -31 # -26 # -30 # -29 # -28
    # db.straight(-20) # not here before
    # db.straight(-10)
    pd.action_front.run_angle(400, 135)
    pd.action_front.run_angle(100, 20)
    db.straight(-110) # -110 before # -90 # -80
    yaw(-17) # -20 before # -10 # -18
    db.straight(110) # 130 # 120
    pd.action_front.run_angle(-400, 220)
    wait(250)

    # get the carrot
    yaw(-109) # -110
    db.settings(150)  
    db.straight(180) # 180
    db.settings(default_speed)
    db.straight(-160) # -160

    # anglerfish
    yaw(-55)
    db.straight(-240) # -240
    yaw(-91)
    db.straight(-600)

    # anker
    yaw(-110) # -110
    db.straight(290)
    yaw(-90) # -90
    db.straight(-250)
    yaw(-120)
    db.straight(-150)

    # ocean probe and coral reef
    db.settings(100)
    yaw(-95)
    db.straight(-250)
    db.straight(30)
    pd.action_back.run_angle(800, -200)
    # db.straight(-30)
    pd.action_back.run_angle(800, 200)
    db.settings(default_speed)

    # Shark
    db.straight(-90)
    yaw(-55)
    pd.action_front.run_angle(800, 190)

    # Diver(in)
    pd.action_front.run_angle(100, -100)
    # db.straight(50)
    yaw(-86) # -85,5
    db.straight(-40) # -40
    pd.action_front.run_angle(200, 90)
    pd.action_front.run_angle(200, -90)

    # Collect remaining stuff and get da fuq outta here
    pd.action_front.run_angle(100, -50)
    db.straight(120) #before 100
    yaw(-155) #148
    db.straight(-850)
    
    print("Fahrt1 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()
    print(pd.timer.time())



if __name__ == "__main__":
    pd = PupDevices()
    pd.hub.speaker.beep(duration=200)
    for element in drive1(pd): pass