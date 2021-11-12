#!/usr/bin/env pybricks-micropython

#########################################################################
# TASK DESCRIPTION
# Make a circle around a floor square
# - Have your robot traverse a circle shape on the floor
# - that touches all four sides of a floor square
#########################################################################
task="task4"

##########################################################
# Build: "EV3"
# * Front is opposite the ball
# * TODO: Motor forward is (-1/1) ?
##########################################################
from math import *
build_direction=1
driving_base=119
diameter=59
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
from pybricks.tools import wait

ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track=driving_base)
robot.settings(straight_speed=speed, turn_rate=turn_rate)

##########################################################
# Functions
##########################################################
def drawArc(diameter_cm, degrees):
    global speed, turn_rate
    robot.reset() # reset angle
    current_angle = 0

    # robot.drive(drive_speed=speed, turn_rate=turn_rate) # TODO: this signature as per docs does match device!
    robot.drive(speed=speed, turn_rate=turn_rate)

    # test that have reach angle
    while current_angle < degrees:
      wait(1)
      current_angle = robot.angle()

    robot.stop()
    return

##########################################################
# Perform movement
##########################################################
def traverseCircle():
    drawArc(diameter, 360)
    return

traverseCircle()
