from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, Matrix
from urandom import random
from pupdevices import PupDevices


hub = PrimeHub()

print(f"{hub.battery.voltage()/1000} Volt")

watch = StopWatch()

hub.speaker.beep()

left_motor = Motor(Port.B)
right_motor = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
action_front = Motor(Port.C)
action_back = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
imu = hub.imu
ultra = UltrasonicSensor(Port.E)
color = ColorSensor(Port.D)
timer = StopWatch()

while hub.battery.voltage() > 7750:
    left_motor.dc(100)
    right_motor.dc(100)
    action_front.dc(100)
    action_back.dc(100)
    _ = color.color()
    _ = ultra.distance()
    _ = imu.acceleration()
    print(f"{hub.battery.voltage()/1000} / 7.75 Volt")
    
    la = []
    for i in range(50):
        x = []
        for j in range(50):
            x.append(random() * 999999999)
        la.append(x)

    ma = Matrix(la)
    mb = ma.T
    _ = ma * mb
    _ * _ * ma
    _ = _ * mb


left_motor.stop()
right_motor.stop()
action_front.stop()
action_back.stop()

