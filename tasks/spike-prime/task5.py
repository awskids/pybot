#########################################################################
# TASK DESCRIPTION
# Make a star
# - Have your robot traverse a 5 point star.
# - Alternative: traverse a 6 point star.
#########################################################################
task="task5"

#########################################################################
# Build: "Driving Base 1"
# * Front is opposite the ball, however motors are reversed
# * Motor forward is -1
#########################################################################
from math import *
build_direction=-1
driving_base=11.3
speed=35*build_direction
unit='cm'
wheel_circumference = 5.6 * pi # standard small Spike Prime set wheels <---- default value
segment=30


#########################################################################
# Configuration
#########################################################################
from spike import MotorPair

motor_pair = MotorPair('D', 'C') # left motor, right motor
motor_pair.set_motor_rotation(amount=wheel_circumference, unit='cm') # <---- default value

base_radius = driving_base / 2
base_circumference = 2 * pi * base_radius

#########################################################################
# Details
#########################################################################
#
# a five tip star has 36 degree tips.
#
# other useful equations:
# *. 180 - 36 = 144
# *. 144 / 2 = 72
# *. 90 - 72 = 18
#########################################################################


#########################################################################
# Calculate star_width
#
# 1. 1/2 square length = two sides of triangle (a,b)
# 2. angles are 18 degrees (a), 18 degrees (b), 144 degrees (c)
# 3. hypoteneuse = sqrt(b^2 + a^2 - 2ba·cos(C))
#    sqrt(2r^2 - 2r^2*cos(144))
#########################################################################

radius = segment/2
star_width = sqrt( 2*radius**2 - 2*radius**2*cos(144*pi/180))

#########################################################################
# Calculate tip_edge
#
# 1. 1/2 square length = two side of triangle (a,b)
# 2. known angle(s) are 54 degrees (a), 54 degrees (b), 72 degrees (c)
# 3. tip_spacing = hypoteneuse = sqrt(b^2 + a^2 - 2ba·cos(C))
#    sqrt(2r^2 - 2r^2*cos(72))
# 4. tip_edge = c·sin(A)/sin(C)
#########################################################################

tip_spacing = sqrt( 2*radius**2 - 2*radius**2*cos(72*pi/180))
tip_edge = tip_spacing * sin(36*pi/180)/sin(108*pi/180)
print('radius', radius, 'star_width', star_width, 'tip_edge', tip_edge)

#########################################################################
# Turn X degrees
#########################################################################
def turn(degrees):
    arc = (build_direction*degrees/360) * base_circumference
    steeringunits=100 # rotate in place
    motor_pair.move(amount=arc, unit=unit, steering=steeringunits, speed=speed)
    return

#########################################################################
# 10 Segment Method
#
# edge()
#*. traverse tip_edge
#*. turn 72 degrees (in position) left
#*. traverse tip_edge
#*. turn 144 degrees (in position) right
#
# invoke edge() 5 times
#########################################################################

def edge10Segments():
    motor_pair.move(amount=tip_edge, unit=unit, steering=0, speed=speed)
    turn(-72)
    motor_pair.move(amount=tip_edge, unit=unit, steering=0, speed=speed)
    turn(144)
    return

def traverse10SegmentMethod():
    for count in range(5):
        edge10Segments()

# traverse10SegmentMethod()

#########################################################################
# 5 Segment Method
#
# edge()
# *. traverse star_width
# *. turn 144 degrees (in position) right
#
# invoke edge() 5 times
#########################################################################

def traverse5SegmentMethod():
    for count in range(5):
        motor_pair.move(amount=star_width, unit=unit, steering=0, speed=speed)
        turn(144)

# traverse5SegmentMethod()

#########################################################################
# Challenge: register the robot with a square prior to drawing star
#
# Position A - start midpoint on the squares edge.
# Position B - opposite of star tip, center aligned on side of square, pointed along square side
# Position C - center of star/square, pointed at star tip
# Position D - corner of square, pointed at center of star
#########################################################################

#########################################################################
# Position A Solution
# 1. place robot at midpoint on square edge with star tip.
# 2. calculate star_width
# 3. turn right 72 degrees (at position)
# 4. draw star using either method (10 segment or 5 segment)
#########################################################################

#########################################################################
# Position B Solution
# 1. place robot at midpoint of square, on base, pointed along square side
# 2. traverse a 36 degree arc (diameter = square side)
# 3. turn right 72 degrees (at position)
# 4. draw star using either method (10 segment or 5 segment)
#########################################################################

#########################################################################
# Position C Solution
# 1. place robot at center of square pointed to tip of star.
# 2. travers 1/2 square length
# 3. turn right 90 + 72 degrees (at position)
# 4. draw star using either method (10 segment or 5 segment)
#########################################################################

#########################################################################
# Position D Solution
# 1. place robot at edge of square, pointed to opposite corner.
# 2. calculate distance from corner to square center.
# 3. drive straight for a distance = calculated in step 2
# 4. turn left 45 degrees (now aligned to a square)
# 5. pick a point, turn left/right 72 degrees in intervals
# 6. traverse star
#########################################################################

def SolutionA():
    turn(72)
    # traverse5SegmentMethod()
    traverse10SegmentMethod()
    turn(-72) # reset

SolutionA()

#########################################################################
# Challenge: traverse a 6 point star
#
# Options:
# 1. traverse two overlapping triangles, offset by 60 degrees
# 2. traverse 12 sided polygon
#########################################################################

def edge12Segments():
    motor_pair.move(amount=tip_edge, unit=unit, steering=0, speed=speed)
    turn(-60)
    motor_pair.move(amount=tip_edge, unit=unit, steering=0, speed=speed)
    turn(120)
    return

def traverse12SegmentMethod():
    for count in range(6):
        edge12Segments()

#########################################################################
# References
#########################################################################
# https://sciencing.com/geometry-fivepoint-star-4606571.html
# https://www.calculator.net/triangle-calculator.html
# 1° × π/180 = 0.01745rad
# 
# 6pt star, has 60 degree angles
# https://mathalino.com/reviewer/plane-geometry/area-of-regular-six-pointed-star
#########################################################################