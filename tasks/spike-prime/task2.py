##########################################################
# TASK DESCRIPTION
# Make a square
# - Have your robot traverse a square on the floor,
# - using right hand turns
##########################################################
task="task2"

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
motor_pair.set_stop_action(action='brake')

##########################################################
# Functions
##########################################################
def degreesToUnits(degrees):
    arc = (degrees/360) * base_circumference
    steeringunits=int((100.0*degrees)/180.0)
    steeringunits=100   # TODO: rotate like a tank
    return steeringunits, arc

def moveSegment(distance):
    motor_pair.move(amount=distance, unit=unit, steering=0, speed=speed)
    return

def turnRightAtWaypoint():
    steeringunits, arc = degreesToUnits(-90)
    print(task, 'steeringunits', steeringunits, 'arc', arc)
    motor_pair.move(amount=arc, unit=unit, steering=steeringunits, speed=speed)
    return

# def turnRightAtWaypointII():
  #from spike import PrimeHub
  #hub = PrimeHub()
  #hub.motion_sensor.reset_yaw_angle()
  #while hub.motion_sensor.get_yaw_angle()<90:
  #    motor_pair.start(100)
  #motor_pair.stop()

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

# Alternative, turn left.
# Alternative, make two non-overlapping squares.
