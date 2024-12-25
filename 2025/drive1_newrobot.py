from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task


hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")

# Motoren initialisieren
left_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, positive_direction=Direction.CLOCKWISE)

action_front = Motor(Port.C)
action_back = Motor(Port.A)

ultra = UltrasonicSensor(Port.E)
color = ColorSensor(Port.D)

#DriveBase initialisieren
wheel_diameter = 56 
axle_track = 113 
drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
drive_base.use_gyro(True)


watch = StopWatch()

hub.speaker.beep()

drive_base.settings(250)

#für Roboter weiß

#arm hochheben
action_front.run_angle(200, -110) #200, -110

#zu der/die/das Kaktus
drive_base.turn(-4.5) #-4,5
drive_base.straight(590) #590
drive_base.settings(950) #950
action_back.run_angle(200, -170) #200, -170

#zu 1. Schrimm & Koralle
drive_base.straight(-200) #-200
drive_base.turn(75) #75
drive_base.straight(200) #200

#2. Schrims
drive_base.turn(-30) #30
drive_base.straight(195) #before 180
drive_base.turn(35) #35
drive_base.straight(70) #70

#zu Karotte
drive_base.turn(-124)#before -120
drive_base.straight(120) #120
action_back.run_angle(200, 190) #200, 190
drive_base.straight(-60) #-55
action_back.run_angle(200, -80) #200, -80
action_front.run_angle(200, -50) #200, -50
drive_base.straight(206) #200
action_back.run_angle(200, -90) #200, -90

#zu Anglerfisch
drive_base.turn(-3) # before 10
drive_base.straight(400) #before 441.35
drive_base.straight(25) #25

drive_base.straight(-20) # bleibt somit nicht mehr hängen beim Anglerfisch

#eingesammelte Sachen abstellen
drive_base.turn(13) #13
drive_base.straight(255) #300
drive_base.turn(-10.5) #-10.5

#zum Korallenriff
drive_base.settings(150)
drive_base.straight(240) #170
#drive_base.settings(250)
wait(300) #300
action_front.run_angle(800, 150) #800, 150
action_front.run_angle(100, -160) #100,-180

#zum Anker
drive_base.straight(-120) #100
drive_base.turn(-34) #before 34
action_back.run_angle(80, 79) #before 80,78
drive_base.straight(-40) #-45
drive_base.turn(-19) #-17
drive_base.straight(-60) #60

#Anker hoch
action_back.run_angle(200, -90) #200, -90

#alles einsammeln
drive_base.turn(50) #30
drive_base.straight(270) #270
drive_base.turn(-25) #-30
drive_base.straight(120) #80
drive_base.turn(-57) #-50
drive_base.straight(20)
drive_base.settings(700)
drive_base.curve(600, 65)

print("Fahrt 1 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
watch.reset()