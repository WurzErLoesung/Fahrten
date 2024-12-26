from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from action_arc import action_arc

hub = PrimeHub()
# Motoren initialisieren 
left_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE) 
right_motor = Motor(Port.F, positive_direction=Direction.CLOCKWISE)

action_front = Motor(Port.C)
action_back = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)

ultra = UltrasonicSensor(Port.E)
color = ColorSensor(Port.D)
watch = StopWatch()

#DriveBase initialisieren
wheel_diameter = 56
axle_track = 113
drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
drive_base.use_gyro(True)
drive_base.settings(straight_speed=900, straight_acceleration=500, turn_rate=100)
StopWatch = watch
hub.speaker.beep()

# Dreizack
drive_base.straight(-360)
drive_base.turn(20)
drive_base.straight(-130)
drive_base.turn(-20)
drive_base.straight(-75)
drive_base.turn(-8)
drive_base.straight(-25)
drive_base.turn(-8)
drive_base.straight(-500)
action_back.run_time(500, 2500)
action_back.run_angle(50, -240)
drive_base.straight(150)
drive_base.turn(90)
drive_base.straight(400)

print("Fahrt 4 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
watch.reset()