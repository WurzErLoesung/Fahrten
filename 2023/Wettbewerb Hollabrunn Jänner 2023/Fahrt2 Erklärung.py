# Bei Fragen und Problemen an Simon Unger wenden
# Fahrt ist zuständig für POWER ENGINE und TOY FACTORY

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until
from spike.control import Timer as SpikeTimer
from math import *

class Ports:
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'

class Color:
    BLACK = "black"

class BrakeStopAction:
    BRAKE = "brake"
    HOLD = "hold"
    COAST = "coast"

CM = "cm"

# Schreibt "Ready" in die Konsole am Laptop
print("Ready")
# Stellt den Drucksensor ein, damit ich mit der Variable force darauf zugreifen kann. Argument: Port 'D'
force = ForceSensor(Ports.D)
# Wartet bis der Drucksensor gedrückt wird, danach noch eine halbe Sekunde um die Hand wegzugeben
wait_until(force.is_pressed)
wait_for_seconds(0.5)

# Eine Funktion, die die Energieeinheiten abwirft. Dadurch muss ich später nur noch dropEnergy() eingeben
def dropEnergy():
    action_motor.start(-8)
    wait_for_seconds(4.5)
    action_motor.stop()

# Eine Funktion, die zurückschreibt (mit True oder False), ob ich mit beiden Farbsensorn auf Schwarz stehe
def on_black_line():
    return color_left.get_color() == Color.BLACK and color_right.get_color() == Color.BLACK

# 
def relative_yaw(target_yaw: int):
    yaw(current_yaw + target_yaw)

# Funktion, die den Roboter zu einer Gradzahl dreht
def yaw(target_yaw: int):
    # Falls die Gradzahl positiv ist, dreht er sich nach Rechts, ist sie negativ, nach links
    drive.start(100 * (min(1, max(MotionSensor.get_yaw_angle() - target_yaw, -1))), 10)
    # Wartet, bis der Roboter bei der richtigen Gradzahl steht
    wait_until(MotionSensor.get_yaw_angle, target_value=target_yaw)
    # Stoppt den Roboter
    drive.stop()
    # Wartet eine Zehntel Sekunde
    wait_for_seconds(0.1)
    # Gibt die aktuelle Gradzahl des Roboters zurück
    return MotionSensor.get_yaw_angle()

# Speichert den Programmierstein, damit ich darauf zugreifen kann
hub = PrimeHub()
# Selbes mit dem Gyro-Sensor
MotionSensor = hub.motion_sensor
# Resetet die Gradzahl des Gyrosensors
MotionSensor.reset_yaw_angle()
# Selbes mit dem Motor-Paar
drive = MotorPair(Ports.B, Ports.F)
# Selbes mit dem manuellen Roboter
action_motor = Motor(Ports.C)
# Selbes mit den Farbsensor
color_left = ColorSensor(Ports.E)
color_right = ColorSensor(Ports.A)
# Setzt die Stop-Art auf plötzliches Stoppen mit Blockierung der Reifen
drive.set_stop_action(BrakeStopAction.HOLD)

# VAR INITIALIZATION
start_yaw = MotionSensor.get_yaw_angle()
current_yaw = start_yaw
# Adjust robots default speed
default_speed = 50
# Adjust how far the Robot moves out of HOMEZONE
way_out_home = 50
# Adjust the steering out of HOMEZONE
steering_out_home = -7
# Adjust how far the robot moves back after standing on black line
back_after_black = -10
# Adjust yaw for aligning on black line
yaw_align_black = 45
# Adjust way back after POWER ENGINE
back_after_power = -15
# Adjust alignment yaw for TOY FACTORY
yaw_toy_factory = -35
# Adjust way to TOY FACTORY
way_toy_factory = -20
# Adjust way back for TOY FACTORY
back_toy_factory = 3


# Drive to POWER ENGINE
# setzt Standardgeschwindigkeit
drive.set_default_speed(default_speed)
# leichte Drehung, um Ungenauigkeiten beim Starten auszugleichen
current_yaw = yaw(2)
# Fährt mit einer Drehung nach Rechts aus der Homezone raus
drive.move(way_out_home, "cm", steering_out_home)
# Dreht sich wieder parallel zur Startposition
current_yaw = yaw(0)
# Fährt bis zu schwarzer Linie
drive.start()
wait_until(on_black_line)
drive.stop()

# Align linear to POWER ENGINE
# Fährt ein wenig zurück
drive.move(back_after_black)
# Dreht sich ein wenig nach Rechts
current_yaw = yaw(yaw_align_black)
# Fährt, bis der Roboter mit dem linken Farbsensor auf der schwarzen Linie steht
drive.start()
wait_until(color_left.get_color, target_value=Color.BLACK)
# Fährt relativ zur Geschwindigkeit noch ein wenig weiter
wait_for_seconds(max(0, 0.7 - (default_speed/100)))
drive.stop()
# Dreht sich Richtung Kraftwerk-Aufgabe
current_yaw = yaw(-90)

# Activate POWER ENGINE
# Fährt zum Kraftwerk, bis er vorne auf der schwarzen Linie steht -> Löst Kraftwerk aus
drive.start()
wait_until(on_black_line)
wait_for_seconds(1)
drive.stop()
wait_for_seconds(0.25)

# Align for TOY FACTORY
# Fährt ein wenig zurück
drive.move(back_after_power)
# Richtet sich für Spielzeugfabrik aus
current_yaw = yaw(yaw_toy_factory)
# Fährt zu SPielzeiugfabrik und ein Stück zurück, um sich gut auszurichten
drive.move(way_toy_factory)
drive.move(back_toy_factory)

# Activate TOY FACTORYs
dropEnergy()

# Drive Back to HOMEZONE
# Fährt zurück zu schwarzer Linie
drive.start()
wait_until(color_left.get_color, target_value="black")
drive.stop()
# Richtet sich aus in Richtung Homezone
current_yaw = yaw(5)
# Fährt zurück in die Homezone mit leichter Drehung, bis der Drucksensor gedrückt wird
drive.start(2, -default_speed)

wait_until(force.is_pressed)
drive.stop()