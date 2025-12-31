from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color
from pybricks.tools import StopWatch, run_task, multitask, wait
from pybricks.pupdevices import Motor

from pupdevices import PupDevices

# ========================================
# MODULE IMPORTS
# ========================================

# Format: 
# try: from (folder.file) import (function)
# except ImportError: (function) = None

try: from brush_new.brush_async import brush_new
except ImportError: brush_new = None

try: from drive_across_new.drive_across_new import drive_across_new
except ImportError: drive_across_new = None

try: from forum_new.forum_new_new import forum_new_new
except ImportError: forum_new_new = None

try: from ship.ship import ship
except ImportError: ship = None

try: from stonehenge.stonehenge import stonehenge
except ImportError: stonehenge = None

try: from trolley.trolley import trolley
except ImportError: trolley = None

try: from crane.crane import crane
except ImportError: crane = None

# ========================================
# COLOR ASIGNMENT
# ========================================

mission_colors = [
    Color.MAGENTA := Color(h=333, s=75, v=78),
    Color.RED := Color(h=355, s=86, v=90),
    Color.BLUE := Color(h=214, s=89, v=82),
    Color.GREEN := Color(h=158, s=75, v=45),
    Color.YELLOW := Color(h=52, s=59, v=100),
    Color.WHITE := Color(h=0, s=0, v=100),
    Color.NONE := Color(h=0, s=0, v=0),
    Color.BLACK := Color(h=170, s=20, v=36)
]


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
# HARDWARE INITIALISATION
# ========================================

hub = PrimeHub()
pd = PupDevices()
timer = StopWatch()

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
    return sensor_color is None or await pd.color.color() == sensor_color

async def is_module_mounted(module_color, pd):
    if module_color is None: return False
    color = await pd.color.color()  
    if color != module_color:
        for i in range(20):
            check = await check_color(module_color, pd) 
            if check: return True
            await wait(10)
        return False

async def module_halt(module_color, pd):
    while ( await is_module_mounted(module_color, pd) ): await wait(200)
    return False

async def play_countdown(seconds: int):
    timer.reset()
    if seconds <= 0: return

    buffer = max(0, seconds - 3) * 1000
    if timer.time() < buffer: await wait(buffer)

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

async def play_starting_sounds(seconds: int):
    if seconds <= 0: return
    else: 
        await mission_identified()
        await multitask(play_countdown(seconds), await_button_press(Button.LEFT), race=True)

async def await_button_press(button: Button)
    while not button in hub.buttons.pressed(): pass
    return True

def stop_all_motors():
    try: pd.drive_base.stop()
    except: pass
    for attr in dir(pd).values():
        try: if isinstance(attr, Motor): attr.stop()
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
    mission, default_countdown, name = MISSIONS[sensor_color][0]
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
        print(f"Countdown: {use_countdown}s")
        print(f"{'='*40}\n")
    
    # Run countdown
    result = await multitask(play_starting_sounds(countdown), module_halt(sensor_color, pd), race=True)
    if False in result: 
        print("Countdown abgebrochen")
        hub.light.on(Color.ORANGE)
        wait(500)
        return False

    mission_timer = StopWatch()
    try:

        # Run mission
        print(f"Starte {name}...")
        result = await multitask(mission(pd), module_halt(sensor_color, pd), race=True)
        
        # Result
        if result[1] == False:
            print(f"ABBRUCH: Farbe verloren!")
            await hub.speaker.beep(200, 300)
            break
        elapsed = mission_timer.time() / 1000
        print(f"\n✅ {name} fertig in {elapsed:.1f}s")

    except Exception as e:
        print(f"\n❌ FEHLER in {name}: {e}")
        await hub.speaker.beep(200, 1000)
        await wait(1000)

    finally:
        stop_all_motors()

    await play_mission_finished()
    await hub.light.on(Color(h=0, s=100, v=100))
    return True

# ========================================
# HAUPTSCHLEIFE
# ========================================
def main_loop():
    waiting = True
    active_color = None
    mission_active = False
    print_available_missions()

    while True:
        hub.light.on( Color(h=120, s=100, v=100) if not waiting else Color(h=0, s=100, v=100))
        
        if Button.RIGHT in hub.buttons.pressed():
            waiting = not waiting
            hub.speaker.beep(400 if waiting else 600, 100)
            wait(250)
        

        color = pd.color.color()
        if color != active_color:
            mission_active = False
            timer.reset()
            active_color = found_color
        
        elif waiting and (mission_active or timer.time() > 1000): 
            wait(100)

        elif active_color != Color.NONE and active_color in MISSIONS:
            mission_active = True
            start_mission(active_color)
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
    except Exception as e:
        print(f"\nFEHLER: {e}")
        hub.speaker.beep(200, 2000)
    finally:
        stop_all_motors()
