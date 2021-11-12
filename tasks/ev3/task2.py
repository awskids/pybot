#!/usr/bin/env pybricks-micropython

##########################################################
# TASK DESCRIPTION
# Make a square
# - Have your robot traverse a square on the floor,
# - using right hand turns
##########################################################
task="task2"

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
wheel_circumference = wheel_diameter * pi # 3.14159

##########################################################
# Configuration
##########################################################
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track=driving_base)
robot.settings(straight_speed=speed, turn_rate=turn_rate) # turn slow to avoid slippage?

##########################################################
# Functions
##########################################################

def moveSegment(distance_cm):
  robot.straight(distance_cm*10) #parameter is distance in mm

def turnRightAtWaypoint():
  robot.turn(90) #parameter is angle in degrees

##########################################################
# Perform movement
##########################################################
def traverseSquare(): # explicitly cover each segment
    moveSegment(segment_length)
    turnRightAtWaypoint()
    moveSegment(segment_length)
    turnRightAtWaypoint()
    moveSegment(segment_length)
    turnRightAtWaypoint()
    moveSegment(segment_length)
    turnRightAtWaypoint()
    return

def traverseSquareII(): # use a loop
    for count in range(4):
        moveSegment(segment_length)
        turnRightAtWaypoint()

# choose one of the following two to run at a time.
traverseSquare()
# traverseSquareII()


