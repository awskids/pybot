#!/usr/bin/env pybricks-micropython

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
# Build: "EV3"
# * Front is opposite the ball
# * TODO: Motor forward is (-1/1) ?
##########################################################
from math import *
build_direction=1
driving_base=119
segment_length=30.48
speed=20*build_direction*10 # in mm/s
turn_rate=speed/2
wheel_diameter = 55.5 # diameter of the wheels in mm
wheel_circumference = wheel_diameter * pi

##########################################################
# Configuration
##########################################################
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track=driving_base)
robot.settings(straight_speed=speed, turn_rate=turn_rate)

##########################################################
# Functions
##########################################################

def moveSegment(distance_cm):
    robot.straight(distance_cm*10)
    return

def turnRightAtWaypoint():
    turn = build_direction*120
    print(task, 'turn', turn)
    robot.turn(120) #parameter is angle in degrees
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
