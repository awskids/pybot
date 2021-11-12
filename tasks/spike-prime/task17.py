#########################################################################
# TASK DESCRIPTION
# - Stay inside the track
# * build has one color sensor
# * assume track identified with different color lines
#########################################################################
task="task17-alt"

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
speed=30*build_direction
wheel_circumference = 5.6 * pi # standard small Spike Prime set wheels <---- default value
left_line_color = 'yellow'
right_line_color = 'red'
start_with_backup = False

#########################################################################
# Configuration
#########################################################################
from spike import MotorPair, ColorSensor
import utime

motor_pair = MotorPair('D', 'C') # left, right motors
color_sensor = ColorSensor('A')

base_radius = driving_base / 2
base_circumference = 2 * pi * base_radius

print(task, 'starting')

#########################################################################
# Copied from Task5 (reusable library)
#########################################################################
def turn(degrees):
    arc = (build_direction*degrees/360) * base_circumference
    steeringunits=100 # rotate in place
    motor_pair.move(amount=arc, unit=unit, steering=steeringunits, speed=speed)
    return

#########################################################################
# Perform movement
#########################################################################

def move_to_line():
    current_direction = 0
    QUICK_TURN = 55
    DECELERATE_TURN = 4

    print(task,'move_to_line','start')
    motor_pair.start(current_direction,speed=speed)

    keep_moving = True

    while keep_moving:
        if current_direction > 2:
            current_direction -= DECELERATE_TURN
            # motor_pair.start(current_direction,speed=speed)
        elif current_direction < -2:
            current_direction += DECELERATE_TURN
            # motor_pair.start(current_direction,speed=speed)

        color = color_sensor.get_color()
        print('found color', color, 'direction', current_direction)
        utime.sleep(0.1) # don't make too big, otherwise easy to miss a line

        if color == left_line_color:
            print('turn right')
            current_direction = QUICK_TURN * build_direction
            turn(45)
            motor_pair.start(0,speed=speed)
            # motor_pair.start(current_direction,speed=speed)
            # keep_moving = False

        if color == right_line_color:
            print('turn left')
            current_direction = -1 * QUICK_TURN * build_direction
            turn(-45)
            motor_pair.start(0,speed=speed)
            # motor_pair.start(current_direction,speed=speed)
            # keep_moving = False

    motor_pair.stop()
    print(task,'move_to_line','done')



if start_with_backup:
    motor_pair.move(amount=10, steering=0, speed=-1*speed)

move_to_line()
# move_beyond_line()
# move_to_line()

