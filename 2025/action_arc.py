from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
from umath import sin, cos, pi

hub = PrimeHub()

def action_arc(drive_base, direction: int, action_motor, action_distance_per_rotation: int,  radius: int, angle: int, velocity: int, starting_angle: int = 0):

    """
    Moves any forklift like structure in an arc like motion
    
    :param drive_base: An drive base object using Spike Prime Drivebase (distances in mm)
    :param direction: 1 for forward and -1 for backward (regarding the drive base)
    :param action_motor: The action motor used for powering the forklift structure
    :param action_distance_per_rotation: The distance the forklift moves per rotation of action motor (negative values for negative rotation)
    :param radius: The radius of the arc in mm
    :param angle: The final angle of the arc motion
    :param velocity: Degrees of the arc motion per second
    :param starting_angle: The angle the arc motion starts at
    """
    
    # Calculates the time it takes for the whole arc to retrieve an bijective relation between time and angle
    # Converts all the angles to radiants for compatibility with cos and sin
    t_max = angle * 1000 / velocity
    angle = 2 * pi * ((angle - starting_angle) / 360)
    starting_angle = 2 * pi * (starting_angle / 360)

    # Using stopwatch for time measurement to calculate delta x and y
    s = StopWatch()
    x_prev = 0.0
    y_prev = 0.0
    t_prev = 0.0
    while (t:=s.time()) < t_max:
        # Calculate current expected angle phi using bijection between time and angle
        phi = angle * (t / t_max)
        
        # Calculate expected x and y for that angle to calculate delta x and y afterwards
        x, y = radius * cos(starting_angle + phi), radius * sin(starting_angle + phi)
        dt = (t - t_prev) / 1000
        dx = (x - x_prev) / dt
        dy = (y - y_prev) / dt
        
        # Calculate speed using dx and dy and start all motors with their respective speed
        vx = dx * direction
        vy = dy * (360 / action_distance_per_rotation)
        action_motor.run(vy)
        drive_base.drive(vx, 0)

        # Store all values for next delta calculation
        t_prev = t
        x_prev = x
        y_prev = y
        wait(1)

    drive_base.stop()
    action_motor.stop()
        
if __name__ == "__main__":
    action_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
    mleft = Motor(Port.B)
    mright = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
    drive_base = DriveBase(mleft, mright, 56, 113)
    
    action_motor.run_angle(500, 250)
    
    # action_arc(280, 70, 30)
    action_arc(drive_base, -1, action_motor, 20, 182, 90, 30, 20)    

    action_motor.run_angle(500, -460)


