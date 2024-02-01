from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import *
from math import *
from sys import exit

hub = PrimeHub()
hub.speaker.set_volume(100)
drive_right = Motor ("A")
drive_left = Motor ("E")
drive = MotorPair('E', 'A')
action_front = Motor ("D")
action_back = Motor('B')
gyro = hub.motion_sensor
color_sensor = ColorSensor ("C")
timer = Timer()

# Bevorzugt Roboter BLAU

fahrten = {}
def BeforeFahrt():
    gyro.reset_yaw_angle()
    drive.set_default_speed(75)
    drive.set_stop_action("coast")
    action_back.set_default_speed(75)
    action_front.set_default_speed(75)

def check_color(color):
    return color == None or color_sensor.get_color() == color

def play_countdown(sec, color = None):
    timer.reset()
    if sec == 0:
        return check_color(color)

    while timer.now() < max(0, sec-3):
        if not check_color(color):
            return False
        wait_for_seconds(0.1)

    for _ in range(3):
        hub.speaker.beep(84, 0.25)
        wait_for_seconds(0.5)
        if not check_color(color):
            return False

    hub.speaker.beep(96, 0.5)
    wait_for_seconds(0.25)
    return check_color(color)

# Fahrt Decorator
def Fahrt(color, countdown, debug, *args, **kwargs):
    def fahrt_decorator(original_fahrt):
        if debug:
            BeforeFahrt()
            fahrt = original_fahrt(*args, **kwargs)
            loop = True
            while loop:
                loop = next(fahrt)
            exit()
        def fahrt_wrapper(override_countdown = None):
            use_countdown = countdown
            if override_countdown != None:
                use_countdown = override_countdown
            if not play_countdown(use_countdown, color):
                yield False
                return
            BeforeFahrt()
            for x in original_fahrt(*args, **kwargs):
                yield x
        fahrten[color] = fahrt_wrapper
        return original_fahrt
    return fahrt_decorator


###########
# Fahrt 1 #
###########
@Fahrt(color="white", countdown=5, debug=False)
def Fahrt1():
    #Ausrichtung:
    # x = 9.5 Rechter Reifen Mitte
    # y = Bande
    # t = ~9-10sec
    gyro.reset_yaw_angle()

    def yaw(target_yaw: int = 0):
        direction = min(1, max(-1, gyro.get_yaw_angle() - target_yaw))# Wählt für alle Gradzahlen unter dem target_yaw -1, für alle Zahlen darüber +1 aus
        steering = 100 * direction                                    # Volle Kanne nach links oder nach rechts (100 oder -100)
        drive.start(steering, 20)                                    # Langsam, aber stark in Richtung drehen
        wait_until(gyro.get_yaw_angle, equal_to, target_yaw)            # Wartet, bis die Richtung 0° ist
        drive.stop()

    #Funktion fürs Drehen aus der aus der aktuellen Position um eine Anzahl an Grad
    def relative_yaw(yaw_step: int):
        yaw(gyro.get_yaw_angle() + yaw_step)
    action_front = Motor('D')

    drive.move(45, speed=70, steering=-6)
    drive.move(-14, speed=30)
    yield True
    drive.move(10, steering=100)
    action_front.run_for_seconds(0.5, speed=100)
    yield True
    yaw(35)
    # drive.move(-10, steering=100, speed=60)
    drive.move(-31, speed=60) # -28.5 davor
    yaw(130)
    yield True

    drive.move(1.2,"seconds", 0, -35)
    # drive.move(1, "cm", 0, 15)
    yield True
    relative_yaw(5)
    wait_for_seconds(0.1)
    yield True
    relative_yaw(21)
    drive.move(2,"seconds", 20, 100)
    yield False

###########
# Fahrt 2 #
###########
@Fahrt(color="yellow", countdown=3, debug=False, orange_scene=True)
@Fahrt(color="red", countdown=3, debug=False, orange_scene=False)
def Fahrt2(orange_scene):
    #Ausrichtung 1 (Am Anfang von der Fahrt)
    #Rote Base
    #Gelbe Wand oben
    #L eingehängt
    #NPCs mit Rücken nach OBEN und Kopf nach SÜDEN
    #Schacht-Piston einmal ganz zurück ziehen
    #x-Achse West-Ost, y-Achse Süd-Nord
    #Räder nach Norden
    #mitte vom linken Rad: x=2, y=10,5


    #Ausrichtung 2 (In der Mitte von der Fahrt)
    #Rote Base
    #Gelbe Wand oben
    #L ausgehängt
    #NPCs mit Rücken nach OBEN und Kopf nach SÜDEN
    #Schacht-Piston einmal ganz zurück ziehen
    #x-Achse West-Ost, y-Achse Süd-Nord
    #Räder nach Norden
    #Mitte des rechten Rades: x = 14, y = 10.5
    #NPC-Yeeter 3000 mit Desinfektionsmittel einschmieren

    def yaw(target_yaw: int = 0, speed=15):
        direction = min(1, max(-1, (gyro.get_yaw_angle() - target_yaw + 180) % 360 - 180))# Wählt für alle Gradzahlen unter dem target_yaw -1, für alle Zahlen darüber +1 aus
        steering = 100*direction
        drive.start(steering, speed=speed)
        wait_until(gyro.get_yaw_angle, equal_to, target_yaw)
        drive.stop()

    def relative_yaw(yaw_step: int):
        yaw(gyro.get_yaw_angle() + yaw_step)

    def drop_figure():
        action_front.run_for_seconds(0.7 ,speed=100)
        wait_for_seconds(0.2)
        action_front.run_for_seconds(0.7 ,speed=-100)
        wait_for_seconds(0.2)

    gyro.reset_yaw_angle()

    drive.set_stop_action("hold")
    drive.set_default_speed(75) #Standard Schnelligkeit 75%

    # 3d Kino
    # drive.move(26,steering=44, speed=100) #Fährt zum Drachen
    # drive.move(9, steering=-100, speed=80) #Löst den Drachen aus
    # drive.move(-15, speed=100)

    # Echtes 3d Kino
    yaw(-22)
    drive.move(23)
    yaw(10)
    drive.move(-30)
    yield True

    play_countdown(8)
    yield True

    gyro.reset_yaw_angle()

    # Drives to Popcorn and drops spectator
    drive.move(30, steering = -11, speed=70)
    yaw()
    drop_figure()
    yield True

    # Drives to Scene Switch and activates it
    drive.move(34, steering=11)
    yaw(-45)
    drive.move(9, speed=40)
    drive.move(-6)
    yaw(-45)
    yield True

    # Drops spectator and activates Scene Switch if orange scene should be activated
    drop_figure()
    if orange_scene:
        # yaw(-45)
        drive.move(9, speed=40)
        drive.move(-5)
    # else:
    #    drive.move(-4.5)
    yield True

    # Moves towards skateboard and drops spectator
    drive.move(-3)
    yaw(35)
    drive.move(13, steering=-40)
    yaw(89)
    drop_figure()
    yield True
    action_back.start(speed=-100)

    # Moves towards Intensive Adventure
    yaw(95)
    drive.move(50, steering=2)
    yaw(38)
    action_back.stop()
    drive.move(20)
    yaw(88)
    #drive.move(-2)
    yield True

    # Activates Intensive Adventure
    action_back.run_for_rotations(8)
    yield True
    action_back.start(speed=-100)

    # Moves towards Light Show and pushes it up, but still in yellow zone
    drive.move(-4)
    yaw()
    drive.move(-24, speed=50)
    action_back.stop()
    action_back.run_for_rotations(10)
    yield True
    action_back.start(speed=-100)

    # Moves towards museum and drops spectator
    drive.move(12, speed=40)
    yaw(20)
    drop_figure()
    yield True

    # Moves back to Light Show and pushes it up into blue zone
    yaw(5)
    action_back.stop()
    drive.move(-15,speed=40)
    action_back.run_for_rotations(10)
    yield True

    # Moves away, drops spectator next to Light Show and moves towards AR
    drive.move(10)
    yaw(-160)
    drive.move(12)
    drop_figure()
    yield True

    # Solves AR
    drive.move(-18)
    yaw(-90)
    yield True
    drive.move(-8)
    yaw(-50)
    yield True
    drive.move(2)
    yaw(-45)
    yield True
    drive.move(-10, steering=-15)
    drive.move(-7)
    yaw(-90)
    yield True

    # Drops last NPC and moves back to base
    drive.move(-30) # -35 before
    yaw()
    yield True
    drive.move(9)
    yaw(45)
    yield True
    drive.move(2)
    drop_figure()
    yield True
    yaw(-15)
    yield True
    drive.move(-80, speed=100)
    yield False

###########
# Fahrt 3 #
###########
@Fahrt(color="green", countdown=3, debug=False)
def Fahrt3():
    #Ausrichtung:
    # linke Ecke mit Aufsatz
    # Zeit= ~18 sec.

    gyro.reset_yaw_angle()

    def yaw(target_yaw: int = 0):
        direction = min(1, max(-1, (gyro.get_yaw_angle() - target_yaw + 180 * (1 if abs(gyro.get_yaw_angle() - target_yaw) >= 180 else -1)) % 360 - 180))# Wählt für alle Gradzahlen unter dem target_yaw -1, für alle Zahlen darüber +1 aus
        steering = 100 * direction                                    # Volle Kanne nach links oder nach rechts (100 oder -100)
        drive.start(steering, 15)                                    # Langsam, aber stark in Richtung drehen
        wait_until(gyro.get_yaw_angle, equal_to, target_yaw)            # Wartet, bis die Richtung 0° ist
        drive.stop()

    def relative_yaw(yaw_step: int):
        yaw((gyro.get_yaw_angle() + yaw_step + 180) % 360 - 180)
    action_front = Motor('D')

    # Camera
    drive.move(-35, speed=100)
    yield True
    drive.move(29, steering=50) # 35 before
    yield True

    # Printer & Chicken
    yaw(-134) # -134 before
    yield True
    drive.move(46, speed=60)
    drive.start(speed=2)
    yield True
    action_front.run_for_rotations(-8, speed=100)
    drive.stop()
    drive.move(-2)
    yaw(120)
    yield True

    # Spectator & Returning to Home Zone
    drive.move(31) # 31 before
    yield True
    yaw(-19) # -17 before
    yield True
    drive.move(-27)
    yield True
    drive.move(10)
    action_back.run_for_rotations(0.5)
    yield True
    drive.move(75, speed=100)
    yield False

###########
# Fahrt 4 #
###########
@Fahrt(color="blue", countdown=5, debug=False)
def Fahrt4():
    #Ausrichtung:
    #blaue Base
    #x-Achse West-Ost, y-Achse Süd-Nord
    #Räder nach Norden
    #Mitte der Lauffläche des rechten Reifens auf x=-4, y=~2,5 (am besten mittels Bande [4 Teile] ausrichten)
    #Arm ganz oben

    def yaw(target_yaw: int = 0):
        direction = min(1, max(-1, gyro.get_yaw_angle() - target_yaw))
        steering = 100*direction
        drive.start(steering, 10)
        wait_until(gyro.get_yaw_angle, equal_to, target_yaw)
        drive.stop()

    def relative_yaw(yaw_step: int):
        yaw(gyro.get_yaw_angle() + yaw_step)

    gyro.reset_yaw_angle()

    action_front.set_default_speed(100)
    drive.set_stop_action("brake")


    drive.move(-18, speed=90)
    yaw(-42) # 43 before
    drive.move(-27, steering=2, speed=80)
    action_front.run_for_rotations(-3.1)
    drive.move(2)
    action_front.start()
    drive.move(25)
    action_front.stop()
    yield True

    yaw(-26)
    # action_front.run_for_rotations(2.3)
    action_front.start(speed=100)
    drive.move(-37, speed=100)
    action_front.stop()
    yaw(48)
    yield True
    drive.move(-28)
    action_back.run_for_rotations(1)
    action_front.run_for_rotations(-2)
    drive.move(15)
    yield True
    action_front.start(75)
    relative_yaw(-30)
    action_front.stop()
    yield True
    drive.move(-13)
    drive.move(20, steering=50)
    drive.move(-30, steering=-30)
    yaw(-90)
    yield True
    drive.move(-35)
    yaw(-45)
    drive.move(-16, steering=-5)
    drive.move(0.5)
    yield False


def play_fahrt_finished():
    hub.speaker.beep(90, 0.1)
    hub.speaker.beep(84, 0.5)

def play_fahrt_found():
    hub.speaker.beep(90, 0.1)
    wait_for_seconds(0.1)
    hub.speaker.beep(90, 0.1)
    wait_for_seconds(0.1)
    hub.speaker.beep(90, 0.1)

def start_fahrt(color, countdown = None):
    if color in fahrten:
        play_fahrt_found()
        fahrt = fahrten[color](countdown)
        loop = True
        while loop:
            loop = next(fahrt)
            if color_sensor.get_color() != active_color:
                break
        drive.stop()
        action_back.stop()
        action_front.stop()
        play_fahrt_finished()

hub.right_button.wait_until_pressed()
#wait_for_seconds(1)
fahrt_active = True
active_color = color_sensor.get_color()
if active_color != None:
    start_fahrt(active_color, 0)
while True:
    found_color = color_sensor.get_color()
    if found_color != active_color:
        fahrt_active = False
        timer.reset()
        active_color = found_color
        continue
    if not fahrt_active and timer.now() > 1:
        fahrt_active = True
        start_fahrt(found_color)
    else:
        wait_for_seconds(0.1)
