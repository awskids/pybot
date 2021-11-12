##########################################################
# TASK DESCRIPTION
# Make an Equilateral Triangle
# -Have your robot traverse a equilateral triangle
# -on the floor, using right hand turns
#
# NOTE: inner angle of equilateral triangle = 60 degrees
# NOTE: outer angle of equilateral triangle = 180 - 60 = 120 degrees
##########################################################
task="task3"

##########################################################
# Build: "Driving Base 1"
# * Front is opposite the ball, however motors are reversed
# * Motor forward is -1
##########################################################
from math import *
build_direction=-1
driving_base=11.3
segment_length=30.48
speed=20*build_direction
unit='cm'
wheel_circumference = 5.6 * pi # standard small Spike Prime set wheels <---- default value

##########################################################
# Configuration
##########################################################
from spike import MotorPair

base_radius = driving_base / 2
base_circumference = 2 * pi * base_radius
print(task, 'base_circumference', base_circumference)

motor_pair = MotorPair('D', 'C') # left motor, right motor
motor_pair.set_motor_rotation(amount=wheel_circumference, unit=unit) # <---- default value

##########################################################
# Functions
##########################################################

def degreesToUnits(degrees):
    arc = (degrees/360) * base_circumference
    steeringunits=100# TODO: rotate like a tank
    return steeringunits, arc

def moveSegment(distance):
    motor_pair.move(amount=distance, unit=unit, steering=0, speed=speed)
    return

def turnRightAtWaypoint():
    steeringunits, arc = degreesToUnits(build_direction*120)
    print(task, steeringunits, arc)
    motor_pair.move(amount=arc, unit=unit, steering=steeringunits, speed=speed)
    return

##########################################################
# Perform movement
##########################################################
def traverseTriangle(): # explicitly cover each segment
    moveSegment(segment_length)
    turnRightAtWaypoint()
    moveSegment(segment_length)
    turnRightAtWaypoint()
    moveSegment(segment_length)
    turnRightAtWaypoint()
    return

traverseTriangle()
