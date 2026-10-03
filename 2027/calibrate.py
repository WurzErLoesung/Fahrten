"""Kalibrierung und Genauigkeitsmessung.

Bedienung (CENTER wird NICHT benutzt - das ist die Stopp-Taste):
    LEFT   = naechster Test
    RIGHT  = Test starten / weiter
    CENTER = Programm beenden

Reihenfolge:
    1. wheel_diameter()    - Strecke ausmessen, Raddurchmesser korrigieren
    2. axle_track()        - Achsabstand ueber die IMU korrigieren
    3. turn_accuracy()     - Drehgenauigkeit messen
    4. straight_accuracy() - Streckengenauigkeit messen

Die Werte aus Test 1 und 2 in pupdevices.py eintragen
(WHEEL_DIAMETER / AXLE_TRACK) und unten spiegeln.
"""

from pybricks.parameters import Button, Color, Stop
from pybricks.tools import StopWatch, run_task, wait

from pupdevices import PupDevices
from yaw import Yaw

VERSION = 3
print("calibrate.py Version", VERSION, "startet...")

pd = PupDevices()
db = pd.drive_base
hub = pd.hub
# Reihenfolge wie im Originalprojekt (F=CCW, B=normal): right zuerst.
yaw = Yaw(hub, pd.right_motor, pd.left_motor)

# Aktuelle Werte aus pupdevices.py - hier spiegeln!
WHEEL_DIAMETER = 62.3
AXLE_TRACK = 159.7


def wait_for_imu():
    print("Warte auf IMU...")
    hub.light.on(Color.ORANGE)
    try:
        while not hub.imu.ready():
            wait(50)
    except AttributeError:
        # Aeltere Firmware kennt imu.ready() nicht.
        wait(2000)
    hub.light.on(Color.GREEN)
    print("IMU bereit.")


def wait_for_go():
    """Wartet auf RIGHT. CENTER wird bewusst nicht abgefragt."""
    while hub.buttons.pressed():
        wait(10)
    while Button.RIGHT not in hub.buttons.pressed():
        wait(10)
    while hub.buttons.pressed():
        wait(10)


# ----------------------------------------------------------------------
# 1. Raddurchmesser
# ----------------------------------------------------------------------


def wheel_diameter(target=1000, speed=300):
    """Faehrt geradeaus. Danach die reale Strecke mit dem Massband messen."""
    print("--- Raddurchmesser ---")
    print("Roboter an eine Markierung stellen, dann RIGHT.")
    wait_for_go()

    wait_for_imu()
    db.use_gyro(True)
    db.settings(straight_speed=speed)
    db.straight(target, then=Stop.HOLD)
    wait(300)

    print("Soll:", target, "mm")
    print("Jetzt die reale Strecke messen.")
    print("Neuer Wert = %d * real / %d" % (WHEEL_DIAMETER, target))
    print("Beispiel: real 980 ->", round(WHEEL_DIAMETER * 980 / target, 2))


# ----------------------------------------------------------------------
# 2. Achsabstand
# ----------------------------------------------------------------------


def axle_track(rotations=10, speed=200):
    """Dreht n volle Umdrehungen ohne Gyro und misst den Fehler per IMU.

    Der Achsabstand beeinflusst nur DriveBase.turn(), nicht Yaw
    (Yaw regelt direkt auf die IMU).
    """
    print("--- Achsabstand ---")
    print("Freie Flaeche, dann RIGHT.")
    wait_for_go()

    wait_for_imu()
    db.use_gyro(False)
    db.settings(turn_rate=speed)
    hub.imu.reset_heading(0)

    target = 360 * rotations
    db.turn(target, then=Stop.HOLD)
    wait(500)

    real = hub.imu.heading()
    print("Soll:", target, "Grad")
    print("Ist :", round(real, 2), "Grad")

    if real:
        print("Vorschlag Achsabstand:", round(AXLE_TRACK * real / target, 2), "mm")
        print("(dreht er zu wenig, wird der Wert kleiner)")

    db.use_gyro(True)


# ----------------------------------------------------------------------
# 3. Drehgenauigkeit
# ----------------------------------------------------------------------


def turn_accuracy(angles=(90, -90, 180, 45, 0), settle_ms=150):
    """Faehrt absolute Kurse an und misst jeweils den Restfehler."""
    print("--- Drehgenauigkeit ---")
    print("Freie Flaeche, dann RIGHT.")
    wait_for_go()

    wait_for_imu()
    db.use_gyro(True)
    hub.imu.reset_heading(0)

    errors = []
    watch = StopWatch()

    for target in angles:
        watch.reset()
        db.stop()
        run_task(yaw(target))
        wait(settle_ms)

        error = (target - hub.imu.heading() + 180) % 360 - 180
        errors.append(error)
        print("Ziel %6.1f  Fehler %6.2f  Dauer %4d ms"
              % (target, error, watch.time()))

    worst = max(abs(e) for e in errors)
    mean = sum(abs(e) for e in errors) / len(errors)
    print("Mittlerer Fehler:", round(mean, 2), "Grad")
    print("Groesster Fehler:", round(worst, 2), "Grad")

    if worst > 2:
        print("HINWEIS: grosser Fehler. Pruefe die Dauer-Spalte - liegt sie")
        print("bei ~3000 ms, lief die Drehung in den Timeout und wurde in")
        print("einer Zufallsposition abgebrochen (zu wenig Drehmoment,")
        print("Untergrund zu griffig oder min_velocity zu niedrig).")


# ----------------------------------------------------------------------
# 4. Streckengenauigkeit
# ----------------------------------------------------------------------


def straight_accuracy(distance=500, repeats=5, speed=400, settle_ms=150):
    """Faehrt hin und zurueck und vergleicht Encoder-Soll mit Encoder-Ist."""
    print("--- Streckengenauigkeit ---")
    print("Freie Bahn von", distance, "mm, dann RIGHT.")
    wait_for_go()

    wait_for_imu()
    db.use_gyro(True)
    db.settings(straight_speed=speed)
    hub.imu.reset_heading(0)

    errors = []
    for i in range(repeats):
        db.reset()
        db.straight(distance, then=Stop.HOLD)
        wait(settle_ms)
        error = distance - db.distance()
        errors.append(error)
        print("Lauf %d  Fehler %6.2f mm  Drift %5.2f Grad"
              % (i + 1, error, hub.imu.heading()))

        db.straight(-distance, then=Stop.HOLD)
        wait(settle_ms)

    mean = sum(abs(e) for e in errors) / len(errors)
    print("Mittlerer Encoder-Fehler:", round(mean, 2), "mm")
    print("ACHTUNG: das misst nur den Regelfehler, nicht den Schlupf.")
    print("Fuer den echten Fehler die Endposition nachmessen.")


# ----------------------------------------------------------------------
# Menue
# ----------------------------------------------------------------------

TESTS = (
    ("Raddurchmesser", wheel_diameter),
    ("Achsabstand", axle_track),
    ("Drehgenauigkeit", turn_accuracy),
    ("Streckengenauigkeit", straight_accuracy),
)


def menu():
    index = 0
    hub.display.number(1)
    print("LEFT = naechster Test, RIGHT = starten, CENTER = beenden")
    print("1:", TESTS[0][0])

    while True:
        pressed = hub.buttons.pressed()

        if Button.LEFT in pressed:
            index = (index + 1) % len(TESTS)
            hub.display.number(index + 1)
            print(str(index + 1) + ":", TESTS[index][0])
            while hub.buttons.pressed():
                wait(10)

        elif Button.RIGHT in pressed:
            while hub.buttons.pressed():
                wait(10)
            TESTS[index][1]()
            print("--- fertig ---")
            print(str(index + 1) + ":", TESTS[index][0])

        wait(20)


if __name__ == "__main__":
    print(hub.system.name(), hub.battery.voltage(), "mV")
    hub.speaker.beep()
    hub.light.on(Color.BLUE)
    menu()