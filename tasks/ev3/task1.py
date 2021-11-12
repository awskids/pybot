#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

from math import *

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

distance_cm=30.48
driving_base = 119 # distance between the wheels in mm
wheel_diameter = 55.5 # diameter of the wheels in mm
wheel_circumference = wheel_diameter * pi # 3.14159

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track=driving_base)

robot.settings(straight_speed=100)
# Parameters:	
# straight_speed (speed: mm/s) – Speed of the robot during straight().
# straight_acceleration (linear acceleration: mm/s/s) – Acceleration and deceleration of the robot at the start and end of straight().
# turn_rate (rotational speed: deg/s) – Turn rate of the robot during turn().
# turn_acceleration (rotational acceleration: deg/s/s) – Angular acceleration and deceleration of the robot at the start and end of turn().


# Go forward distance
robot.straight(distance_cm*10) #parameter is distance in mm
ev3.speaker.beep()


# build_direction=-1
# speed=20*build_direction
# wheel_circumference = 5.6 * pi # standard small Spike Prime set wheels <---- default value
