from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color
from pybricks.tools import StopWatch, run_task, multitask, wait
from pybricks.pupdevices import Motor

from pupdevices import PupDevices

CompetitionMode = False

# ========================================
# MODULE IMPORTS
# ========================================

# Format: 
# try: from (folder.file) import (function)
# except ImportError: (function) = None

try: from artifact.async_artifact import artifact
except ImportError: artifact = None

try: from brush.async_brush import brush
except ImportError: brush = None

try: from crane.async_crane import crane
except ImportError: crane = None

try: from drive_across.async_drive_across import drive_across
except ImportError: drive_across

try: from forum.async_forum import forum
except ImportError: forum = None

try: from ship.async_ship import ship
except ImportError: ship = None

try: from stonehenge.async_stonehenge import stonehenge
except ImportError: stonehenge = None

# ========================================
# COLOR ASIGNMENT
# ========================================

Color.MAGENTA = Color(h=336, s=76, v=78)
Color.RED = Color(h=354, s=86, v=84)
Color.BLUE = Color(h=215, s=91, v=81)
Color.GREEN = Color(h=158, s=78, v=56)
Color.YELLOW = Color(h=48, s=61, v=100)
Color.WHITE = Color(h=0, s=0, v=100)
Color.NONE = Color(h=0, s=0, v=0)
Color.BLACK = Color(h=204, s=25, v=26)

mission_colors = [
    Color.MAGENTA,
    Color.RED,
    Color.BLUE,
    Color.GREEN,
    Color.YELLOW,
    Color.WHITE,
    Color.NONE,
    Color.BLACK
]

# Format: Farbe: (Funktion, Countdown-Sekunden, Name)
MISSIONS = {
    Color.RED: (artifact, 2, "Artifact"),  # passt
    Color.BLUE: (brush, 5, "Brush"),  # passt
    Color.GREEN: (crane, 3, "Crane"),  # passt
    Color.YELLOW: (drive_across, 2, "Drive Across"), # passt
    Color.WHITE: (forum, 5, "Forum"),  # passt
    Color.MAGENTA: (ship, 2, "Ship"),  # passt
    Color.BLACK: (stonehenge, 5, "Stonehenge"),  # passt
}

# ========================================
# HARDWARE INITIALISATION
# ========================================

hub = PrimeHub()
pd = PupDevices()
timer = StopWatch()
competition_timer = StopWatch()
competition_timer.pause()
competition_timer.reset()

competition_seconds = 150

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

colors = list(pd.color.detectable_colors())
colors.extend(mission_colors)
pd.color.detectable_colors(colors)

# ========================================
# HELPER FUNCTIONS
# ========================================

async def check_color(sensor_color, pd):
    color = await pd.color.color() 
    return sensor_color is None or color == sensor_color

async def is_module_mounted(module_color, pd):
    if module_color is None: return False
    color = await pd.color.color()  
    if color != module_color:
        for i in range(20):
            check = await check_color(module_color, pd) 
            if check: return True
            await wait(10)
        return False
    return True

async def module_halt(module_color, pd):
    check = await is_module_mounted(module_color, pd)  
    while check: 
        await wait(200)
        check = await is_module_mounted(module_color, pd)  
    return False

async def play_countdown(seconds: int):
    timer.reset()
    timer.resume()
    if seconds <= 0: return

    buffer = max(0, seconds - 3) * 1000
    if timer.time() < buffer: await wait(buffer - timer.time())

    for _ in range(3):
        await hub.speaker.beep(370, 250)
        await wait(500)

    await hub.speaker.beep(740, 500)
    await wait(250)

async def play_mission_identified():
    for _ in range(3):
        await hub.speaker.beep(523, 100)
        await wait(100)

async def play_mission_success():
    await hub.speaker.beep(523, 100)
    await hub.speaker.beep(370, 500)

async def await_buttons_pressed(*buttons):
    while not any([ button in hub.buttons.pressed() for button in buttons ]): await wait(20)
    return True

async def await_competition_time():
    while competition_timer.time() < competition_seconds * 1000: await wait(20)
    raise SystemExit

async def await_color_change(pd, active_color):
    while ( await pd.color.color() ) == active_color: 
        await wait(100)

async def play_starting_sounds(seconds: int):
    if seconds <= 0: return
    else: 
        await play_mission_identified()
        await multitask(play_countdown(seconds), await_buttons_pressed(Button.LEFT), await_competition_time(), race=True)

def stop_all_motors():
    try: pd.drive_base.stop()
    except: pass
    for attr in dir(pd):
        try: 
            if isinstance(getattr(pd, attr), Motor): getattr(pd, attr).stop()
        except: pass

def print_available_missions():
    print("Verfügbare Missionen:")
    print(f"{'='*40}")
    for color, (func, countdown, name) in MISSIONS.items():
        status = "✓" if func is not None else "✗"
        print(f"  {status} {name:15s} - {color}")
    print(f"{'='*40}\n")
    print("RIGHT Button: Modus wechseln")
    print("LEFT Button: Countdown abbrechen\n")
    hub.speaker.beep()


# ========================================
# MISSION STARTEN
# ========================================
async def run_mission(sensor_color, custom_countdown=None):

    # Identify mission and countdown duration
    if sensor_color not in MISSIONS: return False
    mission, default_countdown, name = MISSIONS[sensor_color]
    if mission is None:
        print(f"❌ {name} nicht verfügbar!")
        await hub.speaker.beep(200, 500)
        await wait(1000)
        return False
    else: 
        countdown = custom_countdown if custom_countdown is not None else default_countdown
        print(f"\n{'='*40}")
        print(f"Mission: {name}")
        print(f"Farbe: {sensor_color}")
        print(f"Countdown: {countdown}s")
        print(f"{'='*40}\n")
    
    # Run countdown
    result = await multitask(play_starting_sounds(countdown), module_halt(sensor_color, pd), await_competition_time(), race=True)
    if False in result: 
        print("Countdown abgebrochen")
        hub.light.on(Color.ORANGE)
        await play_mission_success()
        wait(500)
        return False

    mission_timer = StopWatch()
    try:

        # Run mission
        print(f"Starte {name}...")
        result = await multitask(mission(pd), module_halt(sensor_color, pd), await_competition_time(), race=True)
        
        # Result
        if result[1] == False:
            print(f"ABBRUCH: Farbe verloren!")
            await hub.speaker.beep(200, 300)
            
        elapsed = mission_timer.time() / 1000
        print(f"\n✅ {name} fertig in {elapsed:.1f}s")

    except Exception as e:
        print(f"\n❌ FEHLER in {name}: {e}")
        await hub.speaker.beep(200, 1000)
        await wait(1000)

    finally:
        stop_all_motors()

    await play_mission_success()
    hub.light.on(Color(h=0, s=100, v=100))
    return True

# ========================================
# HAUPTSCHLEIFE
# ========================================
def main_loop():
    comp_timer_active = False
    waiting = not CompetitionMode
    active_color = Color.NONE
    mission_active = False
    print_available_missions()

    while True:
        hub.light.on(Color(h=0, s=100, v=100))
        
        if Button.RIGHT in hub.buttons.pressed():
            waiting = not waiting
            hub.speaker.beep(400 if waiting else 600, 100)

        color = pd.color.color()
        if color != active_color:
            mission_active = False
            timer.reset()
            active_color = color
        
        elif waiting and (mission_active or timer.time() < 1000): 
            wait(100)

        elif not waiting:
            hub.light.on(Color(h=120, s=100, v=100))
            wait(500)
            run_task(await_buttons_pressed(Button.LEFT, Button.RIGHT))
            if Button.LEFT in hub.buttons.pressed():
                competition_timer.resume()
                active_color = pd.color.color()
                print(f"Wettbewerbs-Timer gestartet: {competition_seconds} Sekunden")
                run_task(run_mission(active_color, custom_countdown=0))
                run_task(await_color_change(pd, active_color))
            waiting = True
            hub.light.on(Color(h=0, s=100, v=100))
            hub.speaker.beep(400 if waiting else 600, 100)
            wait(500)

        elif active_color != Color.NONE and active_color in MISSIONS:
            mission_active = True
            run_task(run_mission(active_color))
            run_task(await_color_change(pd, active_color))
            mission_active = False

        else: wait(100)

# ========================================
# PROGRAMMSTART
# ========================================
if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\nProgramm beendet")
    except SystemExit: 
        stop_all_motors()
        run_task(play_mission_success())
    except Exception as e:
        print(f"\nFEHLER: {e}")
        hub.speaker.beep(200, 2000)
        stop_all_motors()
        raise e
    finally:
        stop_all_motors()
