from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Initialize Motors
left_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, positive_direction=Direction.CLOCKWISE)
action_front = Motor(Port.C)
action_back = Motor(Port.A)

# Initialize Sensors
ultra = UltrasonicSensor(Port.E)
color = ColorSensor(Port.D)

# Initialize DriveBase
wheel_diameter = 56
axle_track = 113
drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# Timer Initialization
timer = StopWatch()
global_timer = StopWatch()
fahrten = {}

# Check color helper function
def check_color(sensor_color):
    print(color.color())
    print(sensor_color)
    print(color.color() == sensor_color)
    return sensor_color is None or color.color() == sensor_color

# Countdown and color-checking function
def play_countdown(sec, sensor_color=None):
    timer.reset()
    if sec == 0:
        return check_color(sensor_color)
    
    while timer.time() < max(0, sec - 3) * 1000:
        if not check_color(sensor_color):
            return False
        wait(100)
    
    for _ in range(3):
        hub.speaker.beep(370, 250)
        wait(500)
    
    if not check_color(sensor_color):
        return False
    
    hub.speaker.beep(740, 500)
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
@Fahrt(sensor_color=Color.RED, countdown=3, debug=False)
def Fahrt1():
    drive_base.straight(200)
    yield




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
        play_fahrt_found()
        fahrt = fahrten[sensor_color](countdown)
        
        while True:
            try:
                next(fahrt)
            except StopIteration:
                break

        drive_base.stop()
        action_back.stop()
        action_front.stop()
        play_fahrt_finished()
        hub.light.on(Color(h=0, s=100, v=100)) # Wait before ending

# Main loop for color detection and Fahrt initiation
fahrt_active = False
waiting = True
active_color = None
while True:
    if Button.RIGHT in hub.buttons.pressed():
        waiting = not waiting
        hub.light.on(Color(h=120, s=100, v=100) if not waiting else Color(h=0, s=100, v=100))
    
    if not waiting:
        active_color = color.color()
        
        if active_color is not None:
            start_fahrt(active_color, 5)
        else:
            hub.light.on(Color(h=0, s=100, v=100))
        
        wait(100)
        continue

    found_color = color.color()
    if found_color != active_color:
        fahrt_active = False
        timer.reset()
        active_color = found_color
        continue

    if not fahrt_active and timer.time() > 1000:
        fahrt_active = True
        start_fahrt(found_color)
    else:
        wait(100)
