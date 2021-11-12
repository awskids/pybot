#########################################################################
# TASK DESCRIPTION
# Make a circle around a floor square
# - Have your robot traverse a circle shape on the floor
# - that touches all four sides of a floor square
#########################################################################
task="task4"

#########################################################################
# Build: "Driving Base 1"
# * Front is opposite the ball, however motors are reversed
# * Motor forward is -1
#########################################################################
from math import *
build_direction=-1
driving_base=11.3
speed=25*build_direction
unit='cm'
wheel_circumference = 5.6 * pi # standard small Spike Prime set wheels <---- default value

#########################################################################
# Configuration
#########################################################################
from spike import MotorPair

diameter=59 # Challenge variable
motor_pair = MotorPair('D', 'C') # left motor, right motor
motor_pair.set_motor_rotation(amount=wheel_circumference, unit='cm') # <---- default value


#########################################################################
# Functions
#########################################################################

# steering units versus diameter
lookup_units_from_cm = {
    177: 10,
    95: 20,
    59: 30,
    42: 40,
    32: 50,
    31: 51,
    30: 53, # close but not accurate (short)
    29: 55,
    23.5: 60,
    20: 70,
    14.5: 80,
    14: 81,
    12.5: 90,
    10.5: 99,    # why is this not the wheel base?
    0: 100
}

# Using a model derived via regression from experimental circumference measurements
# NOTE: residual errors can lead to varying diameters.
# BENEFIT: can use any diameter and an approximate arc can be followed
# RESULTS: when diameter has error, it magnifies error in arc length
def drawArc(diameter_cm, percentOfCircle):
    # for "driving base1"
    circumference = pi * diameter_cm
    distance = abs(percentOfCircle) * circumference / 100

    # start by looking up known values, then if not found use a linear equation
    if diameter_cm in lookup_units_from_cm:
        steeringunits = lookup_units_from_cm[diameter_cm]
    else:
        steeringunits = (2000/diameter_cm - 10) # has errors that increase with larger diameters

    steeringunits *= build_direction

    if percentOfCircle < 0:
        steeringunits *= -1

    print('distance', distance, 'steering', steeringunits)
    steeringunits = int(steeringunits)
    motor_pair.move(amount=distance, unit=unit, steering=steeringunits, speed=speed)


#########################################################################
# Perform movement
#########################################################################
def traverseCircle():
    drawArc(diameter, 100)
    return

traverseCircle()


#########################################################################
# Challenge: register the robot with a square prior to drawing circle
#
# Position A - start midpoint on the squares edge.
# Position B - start at edge of square, pointed to end of same side.
# Position C - start at center of square.
# Position D - start at edge of square, pointed to opposite corner.
#########################################################################

#########################################################################
# Position A Solution
# 1. place robot at midpoint on a squares edge.
# 2. configure diameter to be equal to square edge length.
# 3. traverse circle
#########################################################################

#########################################################################
# Position B Solution
# 1. place robot at edge of square, pointed to end of same side.
# 2. configure diameter to be equal to square edge length.
# 3. drive straight for a distance = radius
# 4. traverse circle
#########################################################################

#########################################################################
# Position C Solution
# 1. place robot at start at center of square.
# 2. configure diameter to be equal to square edge length.
# 3. drive straight for a distance = radius
# 4. turn 90 degrees
# 5. traverse circle
#########################################################################

#########################################################################
# Position D Solution #1
# 1. place robot at edge of square, pointed to opposite corner.
# 2. configure diameter to be equal to square edge length.
# 3. calculate distance from corner to square center.
# 4. drive straight for a distance = calculated in step 3 + radius
# 5. turn 90 degrees
# 6. traverse circle
#########################################################################

#########################################################################
# Position D Solution #2
# 1. place robot at edge of square, pointed to opposite corner.
# 2. configure diameter to be equal to square edge length.
# 3. calculate distance from corner to closest point on circle.
# 4. drive straight for a distance = calculated in step 3
# 5. turn 90 degrees
# 6. traverse circle
#########################################################################

#########################################################################
# Other alternatives
# A. approximate circle by forming a polygon
#    (NOTE: more smaller turns/segments can approach higher accuracy)
#
# B. increase accuracy through the use of gyros/accelerometers
#    (evaluate completeness of circle traversal)
#
#    https://www.vexforum.com/t/make-the-robot-go-a-circle/2742/2
#    https://www.fllcasts.com/tutorials/1341-how-our-LEGO-ev3-robots-make-turns
#
#########################################################################