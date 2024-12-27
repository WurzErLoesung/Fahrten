from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
from pupdevices import PupDevices

pd = PupDevices()


hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")

#DriveBase initialisieren
wheel_diameter = 56 
axle_track = 113 
drive_base = DriveBase(pd.left_motor, pd.right_motor, wheel_diameter, axle_track)
drive_base.use_gyro(True)


watch = StopWatch()

hub.speaker.beep()

def drive1():
    drive_base.settings(250)
    yield True

    # für Roboter weiß

    # arm hochheben
    pd.action_front.run_angle(200, -110) #200, -110
    yield True

    # zu der/die/das Kaktus
    drive_base.turn(-4.5) #-4,5
    yield True
    drive_base.straight(590) #590
    yield True
    drive_base.settings(950) #950
    yield True
    pd.action_back.run_angle(200, -170) #200, -170
    yield True

    # zu 1. Schrimm & Koralle
    drive_base.straight(-200) #-200
    yield True
    drive_base.turn(75) #75
    yield True
    drive_base.straight(200) #200
    yield True

    # 2. Schrims
    drive_base.turn(-30) #30
    yield True
    drive_base.straight(195) #before 180
    yield True
    drive_base.turn(35) #35
    yield True
    drive_base.straight(70) #70
    yield True

    # zu Karotte
    drive_base.turn(-124) #before -120
    yield True
    drive_base.straight(120) #120
    yield True
    pd.action_back.run_angle(200, 190) #200, 190
    yield True
    drive_base.straight(-60) #-55
    yield True
    pd.action_back.run_angle(200, -80) #200, -80
    yield True
    pd.action_front.run_angle(200, -50) #200, -50
    yield True
    drive_base.straight(206) #200
    yield True
    pd.action_back.run_angle(200, -90) #200, -90
    yield True

    # zu Anglerfisch
    drive_base.turn(-3) # before 10
    yield True
    drive_base.straight(400) #before 441.35
    yield True
    drive_base.straight(25) #25
    yield True

    drive_base.straight(-20) # bleibt somit nicht mehr hängen beim Anglerfisch
    yield True

    # eingesammelte Sachen abstellen
    drive_base.turn(13) #13
    yield True
    drive_base.straight(255) #300
    yield True
    drive_base.turn(-10.5) #-10.5
    yield True

    # zum Korallenriff
    drive_base.settings(150)
    yield True
    drive_base.straight(240) #170
    yield True
    #drive_base.settings(250)
    wait(300) #300
    pd.action_front.run_angle(800, 150) #800, 150
    yield True
    pd.action_front.run_angle(100, -160) #100,-180
    yield True

    # zum Anker
    drive_base.straight(-120) #100
    yield True
    drive_base.turn(-34) #before 34
    yield True
    pd.action_back.run_angle(80, 79) #before 80,78
    yield True
    drive_base.straight(-40) #-45
    yield True
    drive_base.turn(-19) #-17
    yield True
    drive_base.straight(-60) #60
    yield True

    # Anker hoch
    pd.action_back.run_angle(200, -90) #200, -90
    yield True

    # alles einsammeln
    drive_base.turn(50) #30
    yield True
    drive_base.straight(270) #270
    yield True
    drive_base.turn(-25) #-30
    yield True
    drive_base.straight(120) #80
    yield True
    drive_base.turn(-57) #-50
    yield True
    drive_base.straight(20)
    yield True
    drive_base.settings(700)
    yield True
    drive_base.curve(600, 65)
    yield False

    print("Fahrt 1 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()


if __name__ == "__main__":
    drive1()
