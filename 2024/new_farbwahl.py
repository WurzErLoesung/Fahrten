from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from yaw import Yaw
from action_arc import action_arc
from drive1_rework import drive1
from drive2 import drive2
from drive3 import drive3
from drive4 import drive4
from drive5_1 import drive5_1
from drive5_2 import drive5_2
from drive6 import drive6
from pupdevices import PupDevices

hub = PrimeHub()
pd = PupDevices()
# Initialize DriveBase
yaw = Yaw(hub, pd.left_motor, pd.right_motor)

Color.MAGENTA = Color(h=348, s=91, v=40)
Color.RED = Color(h=352, s=97, v=51)
Color.BLUE = Color(h=215, s=98, v=31)
Color.GREEN = Color(h=157, s=93, v=27)
Color.YELLOW = Color(h=52, s=79, v=70)
Color.WHITE = Color(h=118, s=13, v=75)
Color.NONE = Color(h=0, s=0, v=0)
#
#my_colors = (Color.BLUE, Color.MAGENTA, Color.RED, Color.YELLOW, Color.WHITE, Color.NONE)
#pd.color.detectable_colors(my_colors) 

colors = list(pd.color.detectable_colors()) 
colors.append(Color.MAGENTA)
colors.append(Color.RED)
colors.append(Color.BLUE)
colors.append(Color.GREEN)
colors.append(Color.YELLOW)
colors.append(Color.WHITE)
colors.append(Color.NONE)
pd.color.detectable_colors(colors)

# Timer Initialization
timer = StopWatch()
global_timer = StopWatch()
fahrten = {}

# Check color helper function
def check_color(sensor_color):
    return sensor_color is None or pd.color.color() == sensor_color

# Countdown and color-checking function
def play_countdown(sec, sensor_color=None, skip_start_sound=False):
    timer.reset()
    if sec == 0:
        return check_color(sensor_color)
    
    while timer.time() < max(0, sec - 3) * 1000:
        if Button.LEFT in hub.buttons.pressed():
            skip_start_sound = True
            break
        if not check_color(sensor_color):
            return False
        wait(100)
    
    if not skip_start_sound:
        for _ in range(3):
            hub.speaker.beep(370, 250)
            wait(500)
    
    if not check_color(sensor_color):
        return False
    
    if not skip_start_sound: hub.speaker.beep(740, 500)
    wait(250)
    return check_color(sensor_color)

# Fahrt decorator
def Fahrt(sensor_color, countdown, debug=False, *args, **kwargs):
    def fahrt_decorator(original_fahrt):
        def fahrt_wrapper(override_countdown=None):
            # Use overridden countdown if specified
            use_countdown = override_countdown if override_countdown is not None else countdown
            if not play_countdown(use_countdown, sensor_color):
                yield False
                return
            
            for step in original_fahrt(*args, **kwargs):
                yield step
        
        fahrten[sensor_color] = fahrt_wrapper
        return fahrt_wrapper
    
    return fahrt_decorator

# Define Fahrt1 with the Fahrt decorator
@Fahrt(sensor_color=Color.RED, countdown=5, debug=False)
def Fahrt1():
    for element in drive1(pd): yield element

@Fahrt(sensor_color=Color.YELLOW, countdown=5, debug=False)
def Fahrt2_3():
    for element in drive2(pd): yield element
    wait(3000)
    for element in drive3(pd): yield element

@Fahrt(sensor_color=Color.WHITE, countdown=10, debug=False)
def Fahrt4():
    for element in drive4(pd): yield element

@Fahrt(sensor_color=Color.MAGENTA, countdown=4, debug=False)
def Fahrt5_1():
    for element in drive5_1(pd): yield element
    
# @Fahrt(sensor_color=Color.GREEN, countdown=6, debug=False)
@Fahrt(sensor_color=Color.GREEN, countdown=3, debug=False)
def Fahrt5_2():
    # for element in drive5_2(pd): yield element
    for element in drive5_2(pd): yield element

@Fahrt(sensor_color=Color.BLUE, countdown=5, debug=False)
def Fahrt6():
    for element in drive6(pd): yield element



# Play sound functions
def play_fahrt_finished():
    hub.speaker.beep(523, 100)
    hub.speaker.beep(370, 500)

def play_fahrt_found():
    hub.speaker.beep(523, 100)
    wait(100)
    hub.speaker.beep(523, 100)
    wait(100)
    hub.speaker.beep(523, 100)

# Start a Fahrt (drive) based on color detection
def start_fahrt(sensor_color, countdown=None):
    if sensor_color in fahrten:
        if countdown is None or countdown > 0: play_fahrt_found()
        print(f"Starting Fahrt {sensor_color}")
        fahrt = fahrten[sensor_color](countdown)
        
        while True:
            try:
                if not check_color(sensor_color): 
                    for i in range(10):
                        if check_color(sensor_color): break
                        wait(10)
                    else:
                        print(pd.color.hsv(), pd.color.color())
                        break
                next(fahrt)
            except StopIteration:
                break

        pd.drive_base.stop()
        pd.action_back.stop()
        pd.action_front.stop()
        play_fahrt_finished()
        hub.light.on(Color(h=0, s=100, v=100)) # Wait before ending

# Main loop for color detection and Fahrt initiation
print(hub.system.name())
fahrt_active = False
waiting = False
active_color = None
while True:
    hub.light.on(Color(h=120, s=100, v=100) if not waiting else Color(h=0, s=100, v=100))
    if Button.RIGHT in hub.buttons.pressed(): 
        waiting = not waiting
        wait(250)
    
    if not waiting:
        active_color = pd.color.color()
        
        if active_color != Color.NONE: 
            start_fahrt(active_color, 0)
        else:
            hub.light.on(Color(h=0, s=100, v=100))
            wait(1000)
        wait(100)
        waiting = True
        continue

    found_color = pd.color.color()
    if found_color != active_color:
        fahrt_active = False
        timer.reset()
        active_color = found_color
        continue

    if not fahrt_active and timer.time() > 1000:
        fahrt_active = True
        start_fahrt(found_color)
    else: wait(100)
