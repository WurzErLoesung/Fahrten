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
    pd.drive_base.settings(700, 500) #700, 500
    yaw = Yaw(hub, pd.right_motor, pd.left_motor, min_velocity=100, max_velocity=500, acceleration=600) #100, 500, 600
    
    # Zu Trolley fahren und aufheben
    pd.drive_base.straight(20)
    yaw(-19)
    pd.drive_base.straight(700) 
    yaw(-63)
    pd.drive_base.straight(145) 
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
    yaw(-90)
    pd.drive_base.straight(455)
    
    yaw(-104)
    pd.drive_base.straight(260)
    yaw(180)
    pd.drive_base.straight(40)
    
    pd.action_left.run_angle(100, -50)
    pd.drive_base.straight(-50)
    pd.action_right.run_angle(800, 2850)
    pd.drive_base.straight(80)
    pd.drive_base.straight(-60) 
    pd.action_right.run_angle(800, -3000, wait=False)
    
    yaw(-90)
    pd.drive_base.straight(145) #150
    yaw(-180)
    pd.drive_base.straight(30)
    
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
