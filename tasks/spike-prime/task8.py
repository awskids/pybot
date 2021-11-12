#########################################################################
# TASK DESCRIPTION
# Spiral
#########################################################################
task="task8"

#########################################################################
# Build: "Driving Base 1"
# * Front is opposite the ball, however motors are reversed
# * Motor forward is -1
#########################################################################
from math import *
build_direction=-1
driving_base=11.3
unit='cm'
wheel_circumference = 5.6 * pi # standard small Spike Prime set wheels <---- default value
speed=35*build_direction

#########################################################################
# Configuration
#########################################################################
from spike import MotorPair

motor_pair = MotorPair('D', 'C') # left motor, right motor
motor_pair.set_motor_rotation(amount=wheel_circumference, unit='cm') # <---- default value

#########################################################################
# Details
# *. increase steering overtime, until can't turn anymore (steering=100)
#########################################################################

motor_pair.set_stop_action(action='coast')

current_steering = 10
segment_lenth = 10

while current_steering < 100:
    motor_pair.move(amount=segment_lenth, unit=unit, steering=current_steering, speed=speed)
    current_steering += 5

#########################################################################
# References
#########################################################################
# https://en.wikipedia.org/wiki/Spiral_optimization_algorithm#/media/File:Spiral_image_17.jpg
#########################################################################