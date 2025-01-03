from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
from pupdevices import PupDevices


hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")

watch = StopWatch()

hub.speaker.beep()

def drive1(pd):
    #DriveBase initialisieren
    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(250)
    yield True

    # für Roboter weiß

    # arm hochheben
    pd.action_front.run_angle(200, -110) #200, -110
    yield True

    # zu der/die/das Kaktus
    #pd.drive_base.turn(4.5) #-4,5
    yield True
    pd.drive_base.straight(-590) #590
    yield True
    pd.drive_base.settings(950) #950
    yield True
    pd.action_back.run_angle(200, -170) #200, -170
    yield True

    # zu 1. Schrimm & Koralle
    pd.drive_base.straight(200) #-200
    yield True
    pd.drive_base.turn(-75) #75
    yield True
    pd.drive_base.straight(-200) #200
    yield True

    # 2. Schrims
    pd.drive_base.turn(30) #30
    yield True
    pd.drive_base.straight(-195) #before 180
    yield True
    pd.drive_base.turn(-35) #35
    yield True
    pd.drive_base.straight(-70) #70
    yield True

    # zu Karotte
    pd.drive_base.turn(124) #before -120
    yield True
    pd.drive_base.straight(-120) #120
    yield True
    pd.action_back.run_angle(200, 190) #200, 190
    yield True
    pd.drive_base.straight(60) #-55
    yield True
    pd.action_back.run_angle(200, -80) #200, -80
    yield True
    pd.action_front.run_angle(200, -50) #200, -50
    yield True
    pd.drive_base.straight(-206) #200
    yield True
    pd.action_back.run_angle(200, -90) #200, -90
    yield True

    # zu Anglerfisch
    pd.drive_base.turn(3) # before 10
    yield True
    pd.drive_base.straight(-400) #before 441.35
    yield True
    pd.drive_base.straight(-25) #25
    yield True

    pd.drive_base.straight(20) # bleibt somit nicht mehr hängen beim Anglerfisch
    yield True

    # eingesammelte Sachen abstellen
    pd.drive_base.turn(-13) #13
    yield True
    pd.drive_base.straight(-255) #300
    yield True
    pd.drive_base.turn(10.5) #-10.5
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
    pd.drive_base.straight(120) #100
    yield True
    pd.drive_base.turn(34) #before 34
    yield True
    pd.action_back.run_angle(80, 79) #before 80,78
    yield True
    pd.drive_base.straight(40) #-45
    yield True
    pd.drive_base.turn(19) #-17
    yield True
    pd.drive_base.straight(60) #60
    yield True

    # Anker hoch
    pd.action_back.run_angle(200, -90) #200, -90
    yield True

    # alles einsammeln
    pd.drive_base.turn(-50) #30
    yield True
    pd.drive_base.straight(-270) #270
    yield True
    pd.drive_base.turn(25) #-30
    yield True
    pd.drive_base.straight(-120) #80
    yield True
    pd.drive_base.turn(57) #-50
    yield True
    pd.drive_base.straight(-20)
    yield True
    pd.drive_base.settings(700)
    yield True
    pd.drive_base.curve(600, 65)
    yield False

    print("Fahrt 1 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()


if __name__ == "__main__":
    for element in drive1(PupDevices()): pass
