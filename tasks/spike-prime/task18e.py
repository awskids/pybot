#########################################################################
# TASK DESCRIPTION
# - Follow the line
# * build has one color sensor
# * assume track identified with a wide color line
# * CAUTION: sensor too low will always return white.
#########################################################################
task="task18e"

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
increment = 5

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
# *. move forward while continuously find target color
# *. @DetectOffPath
# *. QuickCheck - test in direction of steering first (10 degree)+/-
#    - if find, then go in that direction.
#########################################################################

def scan_in_place(greedy = False):
    motor_pair.start(100*build_direction, speed=speed)
    color_sensor.wait_until_color(target_color)
    motor_pair.stop()
    return

def move_until_offpath(start_vector):
    print(task, 'move_until', 'start')
    motor_pair.start(0,speed=speed)
    color_sensor.wait_for_new_color()
    motor_pair.stop()
    print(task, 'move_until', 'stop')
    return

def quick_check():
    print(task, 'quick_check', 'start')
    # if find vector, then True else False
    turn(increment)
    utime.sleep(0.1)
    color_right = color_sensor.get_color()
    if color_right == target_color:
        print(task, 'quick_check', 'color_right')
        return True

    turn(-2*increment)
    utime.sleep(0.1)
    color_left = color_sensor.get_color()
    if color_left == target_color:
        print(task, 'quick_check', 'color_left')
        return True

    print(task, 'quick_check', 'failed')
    return False

def greedy_scan():
    print(task, 'greedy_scan', 'started')
    scan_in_place(True)
    print(task, 'greedy_scan', 'done')
    return

#########################################################################
# Perform movement
#########################################################################
greedy_scan()
print(task, 'oriented')

while True:
    move_until_offpath(0)
    print(task, 'went off path')

    if not quick_check():
        greedy_scan()


