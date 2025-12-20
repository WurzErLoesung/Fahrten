from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color
from pybricks.tools import StopWatch, run_task, wait

from pupdevices import PupDevices

# ========================================
# IMPORTS - Automatisch mit Fehlerbehandlung
# ========================================
try:
    from brush_new.brush_async import brush_new

    BRUSH_AVAILABLE = True
except ImportError:
    brush_new = None
    BRUSH_AVAILABLE = False

try:
    from drive_across_new.drive_across_new import drive_across_new

    DRIVE_AVAILABLE = True
except ImportError:
    drive_across_new = None
    DRIVE_AVAILABLE = False

try:
    from forum_new.forum_new_new import forum_new_new

    FORUM_AVAILABLE = True
except ImportError:
    forum_new_new = None
    FORUM_AVAILABLE = False

try:
    from ship.ship import ship

    SHIP_AVAILABLE = True
except ImportError:
    ship = None
    SHIP_AVAILABLE = False

try:
    from stonehenge.stonehenge import stonehenge

    STONEHENGE_AVAILABLE = True
except ImportError:
    stonehenge = None
    STONEHENGE_AVAILABLE = False

try:
    from trolley.trolley import trolley

    TROLLEY_AVAILABLE = True
except ImportError:
    trolley = None
    TROLLEY_AVAILABLE = False

try:
    from crane.crane import crane

    CRANE_AVAILABLE = True
except ImportError:
    crane = None
    CRANE_AVAILABLE = False

# ========================================
# HARDWARE INITIALISIERUNG
# ========================================
hub = PrimeHub()
pd = PupDevices()

print(f"\n{'='*40}")
print(f"System: {hub.system.name()}")
print(f"Batterie: {hub.battery.voltage()} mV")
print(f"Strom: {hub.battery.current()} mA")
print(f"{'='*40}\n")

if hub.battery.voltage() < 7500:
    print("⚠️  WARNUNG: Batterie niedrig!")
    for _ in range(3):
        hub.speaker.beep(200, 100)
        wait(100)

# ========================================
# FARBDEFINITIONEN - Hier anpassen!
# ========================================
Color.MAGENTA = Color(h=333, s=75, v=78)
Color.RED = Color(h=355, s=86, v=90)
Color.BLUE = Color(h=214, s=89, v=82)
Color.GREEN = Color(h=158, s=75, v=45)
Color.YELLOW = Color(h=52, s=59, v=100)
Color.WHITE = Color(h=0, s=0, v=100)
Color.NONE = Color(h=0, s=0, v=0)
Color.BLACK = Color(h=170, s=20, v=36)

colors = list(pd.color.detectable_colors())
colors.extend(
    [
        Color.MAGENTA,
        Color.RED,
        Color.BLUE,
        Color.GREEN,
        Color.YELLOW,
        Color.WHITE,
        Color.NONE,
        Color.BLACK,
    ]
)
pd.color.detectable_colors(colors)

# ========================================
# MISSION-ZUORDNUNG - NUR DIESE ZEILEN ÄNDERN!
# ========================================
# Format: Farbe: (Funktion, Countdown-Sekunden, Name)
MISSIONS = {
    Color.BLUE: (brush_new, 5, "Brush"),  # alt
    Color.YELLOW: (drive_across_new, 5, "Drive Across"),
    Color.WHITE: (forum_new_new, 10, "Forum"),  # alt
    Color.MAGENTA: (ship, 4, "Ship"),  # alt
    Color.GREEN: (crane, 3, "Crane"),  # alt
    Color.RED: (trolley, 5, "Trolley"),  # alt
    Color.BLACK: (stonehenge, 5, "Stonehenge"),  # alt
}

# ========================================
# HILFSFUNKTIONEN
# ========================================
timer = StopWatch()


def check_color(sensor_color):
    return sensor_color is None or pd.color.color() == sensor_color


def play_countdown(sec, sensor_color=None, skip_sound=False):
    timer.reset()
    if sec == 0:
        return check_color(sensor_color)

    while timer.time() < max(0, sec - 3) * 1000:
        if Button.LEFT in hub.buttons.pressed():
            skip_sound = True
            break
        if not check_color(sensor_color):
            return False
        wait(100)

    if not skip_sound:
        for _ in range(3):
            hub.speaker.beep(370, 250)
            wait(500)

    if not check_color(sensor_color):
        return False

    if not skip_sound:
        hub.speaker.beep(740, 500)
    wait(250)
    return check_color(sensor_color)


def play_mission_found():
    for _ in range(3):
        hub.speaker.beep(523, 100)
        wait(100)


def play_mission_finished():
    hub.speaker.beep(523, 100)
    hub.speaker.beep(370, 500)


def stop_all_motors():
    try:
        pd.drive_base.stop()
    except:
        pass
    for motor_name in ["action_back", "action_front", "action_left", "action_right"]:
        try:
            motor = getattr(pd, motor_name, None)
            if motor:
                motor.stop()
        except:
            pass


# ========================================
# MISSION STARTEN
# ========================================
def start_mission(sensor_color, override_countdown=None):
    if sensor_color not in MISSIONS:
        return

    mission_func, default_countdown, name = MISSIONS[sensor_color]

    if mission_func is None:
        print(f"❌ {name} nicht verfügbar!")
        hub.speaker.beep(200, 500)
        wait(1000)
        return

    use_countdown = (
        override_countdown if override_countdown is not None else default_countdown
    )

    if use_countdown > 0:
        play_mission_found()

    print(f"\n{'='*40}")
    print(f"Mission: {name}")
    print(f"Farbe: {sensor_color}")
    print(f"Countdown: {use_countdown}s")
    print(f"{'='*40}\n")

    if not play_countdown(use_countdown, sensor_color, skip_sound=(use_countdown == 0)):
        print("Countdown abgebrochen")
        hub.light.on(Color.ORANGE)
        wait(500)
        return

    mission_timer = StopWatch()

    try:
        # Prüfe ob async (brush_new verwendet run_task)
        if name == "Brush":
            print(f"Starte {name} (async)...")
            run_task(mission_func(pd))
        else:
            print(f"Starte {name}...")
            mission_gen = mission_func(pd)

            for step in mission_gen:
                if not check_color(sensor_color):
                    color_lost = True
                    for i in range(10):
                        if check_color(sensor_color):
                            color_lost = False
                            break
                        wait(10)

                    if color_lost:
                        print(f"ABBRUCH: Farbe verloren!")
                        hub.speaker.beep(200, 300)
                        break

        elapsed = mission_timer.time() / 1000
        print(f"\n✅ {name} fertig in {elapsed:.1f}s")

    except StopIteration:
        elapsed = mission_timer.time() / 1000
        print(f"\n✅ {name} fertig in {elapsed:.1f}s")

    except Exception as e:
        print(f"\n❌ FEHLER in {name}: {e}")
        hub.speaker.beep(200, 1000)
        wait(1000)

    finally:
        stop_all_motors()

    play_mission_finished()
    hub.light.on(Color(h=0, s=100, v=100))


# ========================================
# HAUPTSCHLEIFE
# ========================================
def main_loop():
    print("Verfügbare Missionen:")
    print(f"{'='*40}")
    for color, (func, countdown, name) in MISSIONS.items():
        status = "✓" if func is not None else "✗"
        print(f"  {status} {name:15s} - {color}")
    print(f"{'='*40}\n")
    print("RIGHT Button: Modus wechseln")
    print("LEFT Button: Countdown abbrechen\n")
    hub.speaker.beep()

    waiting = True
    active_color = None
    mission_active = False

    while True:
        hub.light.on(
            Color(h=120, s=100, v=100) if not waiting else Color(h=0, s=100, v=100)
        )

        if Button.RIGHT in hub.buttons.pressed():
            waiting = not waiting
            hub.speaker.beep(400 if waiting else 600, 100)
            wait(250)

        if not waiting:
            active_color = pd.color.color()
            if active_color != Color.NONE and active_color in MISSIONS:
                start_mission(active_color, override_countdown=0)
            else:
                hub.light.on(Color(h=0, s=100, v=100))
                wait(1000)
            wait(100)
            waiting = True
            continue

        found_color = pd.color.color()

        if found_color != active_color:
            mission_active = False
            timer.reset()
            active_color = found_color
            continue

        if not mission_active and timer.time() > 1000:
            if active_color != Color.NONE and active_color in MISSIONS:
                mission_active = True
                start_mission(active_color)
                mission_active = False
        else:
            wait(100)


# ========================================
# PROGRAMMSTART
# ========================================
if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\nProgramm beendet")
    except Exception as e:
        print(f"\nFEHLER: {e}")
        hub.speaker.beep(200, 2000)
    finally:
        stop_all_motors()
