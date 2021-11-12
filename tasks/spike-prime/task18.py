#########################################################################
# TASK DESCRIPTION
# - Follow the line
# * build has one color sensor
# * assume track identified with a wide color line
# * CAUTION: sensor too low will always return white.
#########################################################################
task="task18"

#########################################################################
# Build: "Driving Base 1"
# * Front is opposite the ball, however motors are reversed
# * Motor forward is -1
# + add force sensor to front of driving base
#########################################################################
from math import *
build_direction=-1
driving_base=11.3
unit='cm'
speed=10*build_direction
wheel_circumference = 5.6 * pi # standard small Spike Prime set wheels <---- default value

#########################################################################
# Configuration
#########################################################################
from spike import MotorPair, ColorSensor
import utime

motor_pair = MotorPair('D', 'C') # left, right motors

motor_pair.set_stop_action(action='coast')
motor_pair.set_motor_rotation(amount=wheel_circumference, unit=unit) # <---- default value
color_sensor = ColorSensor('A')

base_radius = driving_base / 2
base_circumference = 2 * pi * base_radius

target_color = 'black'
increment = 10

#########################################################################
# Copied from Task5 (reusable library)
#########################################################################
def turn(degrees):
    arc = (build_direction*degrees/360) * base_circumference
    steeringunits=100 # rotate in place
    motor_pair.move(amount=arc, unit=unit, steering=steeringunits, speed=speed)
    return

#########################################################################
# Details
# *. Scan point for a vector
# *. - rotate in place, sampling colors.
# *. - take first positive detection.
# *. move forward while continuously find target color
# *. @DetectOffPath
# *. QuickCheck - test in direction of steering first (10 degree)+/-
#    - if find, then go in that direction.
#########################################################################

def scan_in_place(greedy = False):
    vectors = []

    current_vector = 0
    while current_vector <= 360:
        turn(increment)
        # print('current_vector', current_vector)

        utime.sleep(0.1) # TODO: do we need to wait?
        current_color = color_sensor.get_color()

        if current_color == target_color:
            print('found target_color', current_vector)
            adjusted_vector = current_vector
            if adjusted_vector > 180:
                adjusted_vector = adjusted_vector - 360 # normalize
            vector = [adjusted_vector, abs(adjusted_vector)]
            vectors.append(vector)
            if greedy:
                break

        current_vector += increment
    return vectors

def move_until_offpath(start_vector):
    print(task, 'move_until', 'start')
    keep_moving = True

    turn(start_vector)
    motor_pair.start(0,speed=speed)

    while keep_moving:
        utime.sleep(0.1)
        color = color_sensor.get_color()

        if not color == target_color: # off path
            print('found color', color)
            keep_moving = False

    motor_pair.stop()
    print(task, 'move_until', 'stop')
    return

def quick_check():
    # if find vector, then True else False
    turn(increment)
    utime.sleep(0.1)
    color_right = color_sensor.get_color()
    if color_right == target_color:
        return True

    turn(-2*increment)
    utime.sleep(0.1)
    color_left = color_sensor.get_color()
    if color_left == target_color:
        return True

    return False

def greedy_scan():
    print('greedy_scan started')
    vector = scan_in_place(True)
    print('greedy_scan', 'vector', vector)
    return 0


#########################################################################
# Perform movement
#########################################################################

vector = greedy_scan()
print('initial vector', vector)

while True:
    move_until_offpath(vector)
    print('went off path')

    if not quick_check():
        vector = greedy_scan()

