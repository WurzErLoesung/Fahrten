from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
from pupdevices import PupDevices
from yaw import Yaw


hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")

watch = StopWatch()

hub.speaker.beep()

def drive1(pd):
    #DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(250, 500)
    yaw = Yaw(hub, pd.left_motor, pd.right_motor)
    yield True

    # für Roboter weiß

    # arm hochheben
    pd.action_front.run_angle(200, -110) #200, -110
    yield True

    # zu der/die/das Kaktus
    pd.drive_base.turn(4.6) #-4,5
    pd.drive_base.straight(-590) #590
    yaw.reset(-45)
    pd.drive_base.settings(950) #950
    pd.action_back.run_angle(200, 170) #200, -170

    # zu 1. Schrimm & Koralle
    pd.drive_base.straight(200) #-200
    yield True
    yaw(20)
    yield True
    pd.drive_base.straight(-180) #200
    yield True

    # 2. Schrims
    yaw(5)
    yield True
    pd.drive_base.straight(-185) #before 180
    yield True
    yaw(30)
    yield True
    pd.drive_base.straight(-75) #-70
    yield True

    # zu Karotte
    yaw(-90)
    yield True
    pd.drive_base.straight(-120) #120
    yield True
    pd.action_back.run_angle(200, -190) #200, 190
    yaw(-90)
    yield True
    pd.drive_base.settings(400, 200)
    pd.drive_base.straight(65) #-55
    pd.drive_base.settings(950, 500)
    yield True
    pd.action_back.run_angle(200, 80) #200, -80
    yield True
    pd.action_front.run_angle(200, -50) #200, -50
    yield True
    pd.drive_base.straight(-50)
    yaw(-90)
    pd.drive_base.straight(-186) #200
    yield True
    pd.action_back.run_angle(200, 90) #200, -90
    yield True

    # zu Anglerfisch
    yaw(-93)
    yield True
    pd.drive_base.straight(-370) #before 441.35
    yield True
    pd.drive_base.straight(-25) #25
    yield True

    pd.drive_base.straight(20) # bleibt somit nicht mehr hängen beim Anglerfisch
    yield True

    # eingesammelte Sachen abstellen
    yaw(-80)
    yield True
    pd.drive_base.straight(-255) #300
    yield True
    yaw(-90)
    yield True

    # zum Korallenriff
    pd.drive_base.settings(150)
    yield True
    pd.drive_base.straight(-240) #170
    yield True
    #pd.drive_base.settings(250)
    wait(300) #300
    pd.action_front.run_angle(800, 150) #800, 150
    yield True
    pd.action_front.run_angle(100, -160) #100,-180
    yield True

    # zum Anker
    """
    pd.drive_base.straight(110) #100
    yield True
    yaw(-110)
    yield True
    pd.action_back.run_angle(80, -79) #before 80,78
    yield True
    pd.drive_base.straight(55) #-45
    yield True
    yaw(-130)
    yield True
    pd.drive_base.straight(60) #60
    yield True

    # Anker hoch
    pd.action_back.run_angle(200, 90) #200, -90
    yield True

    # alles einsammeln
    yaw(-100)
    yield True
    pd.drive_base.straight(-275) #270
    """

    #additional
    pd.drive_base.straight(-45)

    yield True
    yaw(-140)
    yield True
    pd.drive_base.straight(-105) #-110 bei Anker
    yield True
    yaw(-170)
    yield True
    pd.drive_base.straight(-20)
    yield True
    pd.drive_base.settings(700)
    yield True
    pd.drive_base.curve(-600, 65)
    yield False

    print("Fahrt 1 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()


if __name__ == "__main__":
    for element in drive1(PupDevices()): pass
