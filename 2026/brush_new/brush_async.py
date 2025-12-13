from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask
from pupdevices import PupDevices
from yaw import Yaw


hub = PrimeHub()

print(f"{hub.system.name()}: {hub.battery.voltage()} mV")
print(f"{hub.system.name()}: {hub.battery.current()} mA")

watch = StopWatch()

hub.speaker.beep()

async def brush_new(pd):
    #DriveBase initialisieren

    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(950, 700)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor, min_velocity=50, max_velocity=500, acceleration=800)
    

    await pd.drive_base.straight(100)
    yaw(14.5)
    print(pd.hub.imu.heading())
    await pd.drive_base.straight(520)
    yaw(-90)
    await pd.drive_base.straight(150)
    
    await multitask(do_brush(pd), do_rest(pd))
    
    await pd.drive_base.straight(-110)
    yaw(20)
    await pd.drive_base.straight(-620)




    
    print("Fahrt hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()

async def do_brush(pd):
    await pd.action_left.run_angle(1000, -350)
    await pd.action_left.run_angle(800, 300)


async def do_rest(pd):
    await pd.action_right.run_angle(300, 260)
    await pd.action_right.run_angle(600, -970)
    await pd.action_right.run_angle(800, 450)

def test(pd):
    #DriveBase initialisieren

    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(200, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)


if __name__ == "__main__":
    run_task(brush_new(PupDevices()))
    #for element in brush_new(PupDevices()): pass
