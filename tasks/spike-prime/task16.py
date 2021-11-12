#########################################################################
# TASK DESCRIPTION
# Move forward, stop at line
#########################################################################
task="task16"

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
speed=40*build_direction
wheel_circumference = 5.6 * pi # standard small Spike Prime set wheels <---- default value
line_color = 'red'             # color options 'black', 'violet', None, 'blue', 'cyan', 'green', 'yellow', 'red', 'white'
start_with_backup = True

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

print(task, 'starting')


#########################################################################
# Perform movement
#########################################################################

def move_to_line():
    print(task,'move_to_line','start')
    motor_pair.start(0,speed=speed)
    color_sensor.wait_until_color(line_color)
    print(task,'move_to_line','done')


def move_beyond_line():
    print(task,'move_beyond_line','start')
    color = color_sensor.get_color()
    while color == line_color:
        print('found color', color)
        utime.sleep(0.1) # don't make too big, otherwise easy to miss
        color = color_sensor.get_color()

    print(task,'move_beyond_line','done')

if start_with_backup:
    motor_pair.move(amount=50, steering=0, speed=-1*speed)

move_to_line()
move_beyond_line()
move_to_line()
motor_pair.stop()
