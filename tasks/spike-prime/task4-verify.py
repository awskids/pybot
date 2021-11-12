#########################################################################
# TASK DESCRIPTION
# Make a circle around a floor square
# - Have your robot traverse a circle shape on the floor
# - that touches all four sides of a floor square
#########################################################################
task="task4-verify"

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
motor_pair.set_stop_action(action="hold") # other options are "brake" / "coast"
# Setting the "stop" action does not take immediate effect on the motors.
# The setting will be saved and used whenever stop() is called or when one of the move methods has completed without being interrupted.

from spike import PrimeHub# verify
primehub = PrimeHub()            # verify

#########################################################################
# Functions
#########################################################################

# steering units versus diameter
lookup_units_from_cm = {
    177: 10,
    95: 20,
    59: 30, # produces a more reliable circle
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
def traverseCircle(turn_right = True):
    primehub.motion_sensor.reset_yaw_angle() #verify

    # hidden feature for improving model
    import hub as hiddenhub
    hiddenhub.motion.align_to_model(nsamples=100, callback=None)


    if turn_right:
        drawArc(diameter, 100)
    else:
        drawArc(diameter, -1 * 100) # turn left

    angle = primehub.motion_sensor.get_yaw_angle() 
    normalized_angle = angle
    if not turn_right:
        normalized_angle = normalized_angle * -1
    
    print('after a full turn, yaw sensor shows an angle:', normalized_angle) 
    print('through experimentation, yaw angle may be 4-7 degrees off after a full turn\n\n')

    arclength = normalized_angle * ( pi / 180) * diameter/2
    if arclength < 0:
        print('If yaw is accurate, the robot did not complete the circle, it was short by', arclength, unit)
    elif arclength > 0:
        print('If yaw is accurate, the robot over rotated.  it exceeded the circle by', arclength, unit)
    else:
        print('If yaw is accurate, a perfect circle was made.  CONGRATULATIONS!!!')
    return

traverseCircle(turn_right = True)
# traverseCircle(turn_right = False)


#########################################################################
# Challenge: operate the bot at different speeds.
#    Is the bot more accurate moving slow or fast?
#
#########################################################################

#########################################################################
# Challenge: draw small, medium, and large circles.
#    Is the bot more accurate with small, medium, or large circles?
#
#########################################################################

#########################################################################
# Challenge: modify code to perform a SemiCircle
#How do you verify a SemiCircle with the gyros?
#
#########################################################################

