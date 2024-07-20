import motor_pair
import hub
from hub import port
import time

motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
hub.motion_sensor.reset_yaw(0)


async def yaw(deg):
    deg = deg % 360
    time_limit = 3000
    start = time.ticks_ms()
    while True:
        current_yaw = (hub.motion_sensor.tilt_angles()[0]/10) % 360
        difference = deg - current_yaw


        if abs(difference) < 0.1:
            motor_pair.stop(motor_pair.PAIR_1)
            break

        if time.ticks_ms() - start > time_limit:
            print("Timeout")
            break


        if abs(difference) > 180:
            difference = (360 - abs(difference)) * -1 * (difference/abs(difference))
        
        direction = 1 if difference >= 0 else -1

        max_velocity = 300
        min_velocity = 20

        # higher values = higher average speed
        speed_potency = 3

        velocity = round(min_velocity + (max_velocity - min_velocity) * (abs(difference) / 180) ** (1 / speed_potency))


        motor_pair.move_tank(motor_pair.PAIR_1, velocity * direction, velocity * direction * -1)
    motor_pair.stop(motor_pair.PAIR_1)
    print("Gyro-Sensor: " + str(hub.motion_sensor.tilt_angles()[0]/10))


yaw(-90)
yaw(123)
yaw(0)

