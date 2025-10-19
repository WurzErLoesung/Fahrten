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

def forum_new_new(pd):
    #DriveBase initialisieren

    pd.drive_base.use_gyro(True)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(700, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor, min_velocity=100, max_velocity=500, acceleration=600)

    # Zu Trolley fahren und aufheben
    pd.drive_base.straight(20)
    yaw(-21)
    pd.drive_base.straight(670) 
    yaw(-58)
    pd.drive_base.straight(150) 
    yaw(-90)
    pd.drive_base.straight(130)

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

    # Zu Forum fahren und abladen
    pd.drive_base.straight(-120)
    yaw(-87)
    pd.drive_base.straight(450)
    
    yaw(-105)
    pd.drive_base.straight(240)
    yaw(180)
    pd.drive_base.straight(90)
    
    pd.action_left.run_angle(100, -100)
    pd.drive_base.straight(-90)
    pd.action_right.run_angle(800, 2850)
    pd.drive_base.straight(50)
    pd.drive_base.straight(-80) 
    pd.action_right.run_angle(800, -3000, wait=False)
    
    yaw(-90)
    pd.drive_base.straight(125) #150
    yaw(-180)
    pd.drive_base.straight(40)
    
    yield False
    print("Fahrt hat " + str(watch.time()/1000) + " Sekunden gedauert.")
    watch.reset()

def test(pd):
    #DriveBase initialisieren

    pd.drive_base.use_gyro(False)
    pd.imu.reset_heading(0)
    pd.drive_base.settings(200, 500)
    yaw = Yaw(hub, pd.right_motor, pd.left_motor)
    yield True


if __name__ == "__main__":
    for element in forum_new_new(PupDevices()): pass
