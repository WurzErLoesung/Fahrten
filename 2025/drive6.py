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
drive_base.use_gyro(False)
drive_base.settings(straight_speed=900, straight_acceleration=500, turn_rate=60)
StopWatch = watch
hub.speaker.beep()

# Boat
drive_base.straight(-5)
drive_base.straight(240)
drive_base.turn(-28)
drive_base.straight(125)
drive_base.turn(-17)
drive_base.straight(20)
drive_base.turn(10)

# Lift Boat
action_front.run_angle(500, -960)

# Yeet Boat
drive_base.settings(straight_acceleration=5000)
drive_base.straight(-200)
drive_base.settings(straight_acceleration=500)

drive_base.turn(-20)
drive_base.straight(250)
drive_base.turn(50)
drive_base.straight(200)
drive_base.turn(50)
drive_base.straight(250)
action_front.run_angle(500, 960)
drive_base.settings(straight_speed=500)
drive_base.straight(-15)
drive_base.settings(straight_speed=900)

#drive to whales
drive_base.straight(-180)
drive_base.turn(92)
drive_base.straight(-90)

# solve whales
action_back.run_angle(1500, -590)
action_back.run_angle(200, -530)

# drive to end
wait(500)
drive_base.straight(30)
wait(1000)
drive_base.straight(100)
action_back.run_angle(1500, 390)
drive_base.turn(90)
drive_base.straight(50)
drive_base.turn(65)
drive_base.straight(700)

# end
action_front.run_angle(500, -960)

print("Fahrt 6 hat " + str(watch.time()/1000) + " Sekunden gedauert.")
watch.reset()
