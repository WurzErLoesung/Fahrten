from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
from pupdevices import PupDevices
from yaw import Yaw


hub = PrimeHub()

print(f"{hub.system.name()}: {hub.battery.voltage()} mV")
print(f"{hub.system.name()}: {hub.battery.current()} mA")

watch = StopWatch()

hub.speaker.beep()

def forum(pd):
    #DriveBase initialisieren

    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(200, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    yield True


    #pd.action_right.run_angle(1000, 3650, wait=False) #3700
    pd.drive_base.straight(20)
    yaw(-21)
    pd.drive_base.straight(580) #580
    yaw(-58)
    pd.drive_base.straight(140) 
    yaw(-90)
    pd.drive_base.straight(120) #115

    #yaw(-30)
    #pd.drive_base.straight(-20)
    #yaw(-50)
    #pd.drive_base.straight(-90, wait=False)
    #start = watch.time()
    #while not pd.drive_base.done():
        #if watch.time() - start > 1000:
            #pd.drive_base.stop()
    #yaw(-55)
    #pd.drive_base.straight(110)
    #yaw(0)

    yaw(0)
    pd.drive_base.straight(120)
    pd.action_right.run_angle(800, -1200)
    pd.drive_base.straight(-120)
    yaw(-90)
    pd.drive_base.straight(350)
    yaw(-60)
    pd.drive_base.straight(40)
    yaw(-90)
    pd.drive_base.straight(100)
    yaw(-110)
    pd.drive_base.straight(200)
    yaw(-180)

    pd.drive_base.straight(90)
    pd.action_left.run_angle(100, -50)
    pd.drive_base.straight(-80)
    pd.action_right.run_angle(800, 2850) #2850
    pd.drive_base.straight(50)
    pd.drive_base.straight(-80) #-70
    pd.action_right.run_angle(800, -3000, wait=False)
    yaw(-90)
    pd.drive_base.straight(145) #150
    yaw(-180)
    pd.drive_base.straight(40)



    yield False
    print("Fahrt hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    print(pd.timer.time())
    watch.reset()

def test(pd):
    #DriveBase initialisieren

    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(200, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    yield True


if __name__ == "__main__":
    for element in forum(PupDevices()): pass
    # for element in trolley(PupDevices()): pass