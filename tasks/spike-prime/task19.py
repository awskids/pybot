#########################################################################
# TASK DESCRIPTION
# - Stay inside the track
# * build has one color sensor
# * assume track identified with different color lines
#########################################################################
task="task17"

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
line_color1 = 'yellow'
line_color2 = 'red'
start_color1 = 'green'
start_color2 = 'blue'
start_with_backup = False

#########################################################################
# Configuration
#########################################################################
from spike import MotorPair, ColorSensor
import utime

motor_pair = MotorPair('D', 'C') # left, right motors
motor_pair.set_motor_rotation(amount=wheel_circumference, unit=unit) # <---- default value
color_sensor = ColorSensor('A')

base_radius = driving_base / 2
base_circumference = 2 * pi * base_radius

left_line_color = line_color1
right_line_color = line_color2
start_color = start_color1
end_color = start_color2

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

def switch_direction():
    global start_color, end_color, left_line_color, right_line_color
    print('switch_direction')
    turn(180)

    if start_color == start_color1:
        start_color = start_color2
        end_color = start_color1        
        left_line_color = line_color2
        right_line_color = line_color1
    else:
        start_color = start_color1
        end_color = start_color2
        left_line_color = line_color1
        right_line_color = line_color2      

def move_to_gate():
    global start_color, end_color, left_line_color, right_line_color
    print('move_to_gate')
    keep_moving = True

    motor_pair.start(0,speed=speed)

    while keep_moving:
        color = color_sensor.get_color()
        print('found color', color)
        
        utime.sleep(0.1) # don't make too big, otherwise easy to miss a line

        if color == start_color1:
            start_color = start_color1
            end_color = start_color2
            left_line_color = line_color1
            right_line_color = line_color2
            keep_moving = False
        elif color == start_color2:
            start_color = start_color2
            end_color = start_color1        
            left_line_color = line_color2
            right_line_color = line_color1
            keep_moving = False


def move_along_path():
    QUICK_TURN = 35

    print(task,'move_to_line','start')
    motor_pair.start(0,speed=speed)

    keep_moving = True

    while keep_moving:
        color = color_sensor.get_color()
        print('found color', color)

        if color == left_line_color:
            print('turn right')
            turn(QUICK_TURN)
            motor_pair.start(0,speed=speed)
            # keep_moving = False

        elif color == right_line_color:
            print('turn left')
            turn(-1*QUICK_TURN)
            motor_pair.start(0,speed=speed)

        elif color == end_color:
            keep_moving = False

        utime.sleep(0.1) # don't make too big, otherwise easy to miss a line

    motor_pair.stop()
    print(task,'move_to_line','done')



if start_with_backup:
    motor_pair.move(amount=10, steering=0, speed=-1*speed)

# detect path entry: blue/green

move_to_gate()
move_along_path()
switch_direction()
move_along_path()
