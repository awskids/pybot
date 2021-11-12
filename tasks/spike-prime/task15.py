#########################################################################
# TASK DESCRIPTION
# Move forward, stop at line
#########################################################################
task="task15"

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
line_color = 'red'
start_with_backup = True

#########################################################################
# Configuration
#########################################################################
from spike import MotorPair, ColorSensor

motor_pair = MotorPair('D', 'C') # left, right motors
motor_pair.set_motor_rotation(amount=wheel_circumference, unit=unit) # <---- default value
color_sensor = ColorSensor('A')

base_radius = driving_base / 2
base_circumference = 2 * pi * base_radius

print(task, 'starting')


#########################################################################
# Perform movement
#########################################################################

if start_with_backup:
    motor_pair.move(amount=50, steering=0, speed=-1*speed)

motor_pair.start(0,speed=speed)
color_sensor.wait_until_color(line_color)
motor_pair.stop()