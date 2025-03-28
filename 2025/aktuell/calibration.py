from hub import light_matrix, motion_sensor, sound, button
import motor_pair, color_sensor, distance_sensor
import runloop

motor_pair.pair(0, 0, 4)

def calc_circumference(distances: list):
    return sum(distances) // len(distances)

def calc_angle_offset(angles: list):
    return sum(angles) // len(angles)

async def main():
    distances = []
    angles = []
    for i in range(5):
        await sound.beep(1000, 250, 100)
        while not button.pressed(2): pass
        await sound.beep(1200, 250, 100)
        await runloop.sleep_ms(500)
        d_prev = distance_sensor.distance(5)
        motion_sensor.reset_yaw(0)
        await motor_pair.move_for_degrees(0, -360, 0, velocity = 250 * (i + 1))
        distances.append(d_prev - distance_sensor.distance(5))
        angles.append(motion_sensor.tilt_angles()[0])
    print(distances)
    print(calc_circumference(distances))
    print(angles)
    print(calc_angle_offset(angles))

runloop.run(main())
