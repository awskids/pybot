#########################################################################
# TASK DESCRIPTION
# Fourleaf clover
#
#########################################################################
task="task7"

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
segment=60
speed=35*build_direction

#########################################################################
# Configuration
#########################################################################

from spike import MotorPair

motor_pair = MotorPair('D', 'C') # left motor, right motor
motor_pair.set_motor_rotation(amount=wheel_circumference, unit='cm') # <---- default value

base_radius = driving_base / 2
base_circumference = 2 * pi * base_radius

diameter = segment/2

#########################################################################
# Copied from Task5 (reusable library)
#########################################################################
def turn(degrees):
    arc = (build_direction*degrees/360) * base_circumference
    steeringunits=100 # rotate in place
    motor_pair.move(amount=arc, unit=unit, steering=steeringunits, speed=speed)
    return

#########################################################################
# Copied from Task4 (reusable library)
#########################################################################
lookup_units_from_cm = {
    177: 10, 95: 20, 60: 30, 42: 40, 32: 50, 31: 51, 30: 53, 29: 55, 23.5: 60, 20: 70, 14.5: 80, 14: 81, 12.5: 90, 10.5: 99, 0: 100
}

def drawArc(diameter_cm, percentOfCircle):
    circumference = pi * diameter_cm
    distance = abs(percentOfCircle) * circumference / 100

    if diameter_cm in lookup_units_from_cm:
        steeringunits = lookup_units_from_cm[diameter_cm]
    else:
        steeringunits = (2000/diameter_cm - 10)

    steeringunits *= build_direction

    if percentOfCircle < 0:
        steeringunits *= -1

    print('distance', distance, 'steering', steeringunits)
    steeringunits = int(steeringunits)
    motor_pair.move(amount=distance, unit=unit, steering=steeringunits, speed=speed)

#########################################################################
# Details
# *. four(4) overlapping circles
#########################################################################

def StartAtPositionA():
    drawArc(diameter, 50)
    drawArc(diameter, -100)
    turn(-90)
    drawArc(diameter, 100)
    drawArc(diameter, -100)
    turn(90)
    drawArc(diameter, 50)
    return

def StartAtPositionB():
    drawArc(diameter, 100)
    drawArc(diameter, -100)
    turn(-90)
    drawArc(diameter, 100)
    drawArc(diameter, -100)
    turn(90) # reset position


# StartAtPositionA()
StartAtPositionB()

#########################################################################
# References
#########################################################################
# https://www.pngfind.com/freepng/four-leaf-clover-png/
#########################################################################
