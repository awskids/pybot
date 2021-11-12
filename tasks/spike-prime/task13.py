#########################################################################
# TASK DESCRIPTION
# circle until hit - then traverse a square
#########################################################################
task="task13"

#########################################################################
# Build: "Driving Base 1"
# * Front is opposite the ball, however motors are reversed
# * Motor forward is -1
# + add force sensor to front of driving base
#########################################################################
from math import *
build_direction=-1
driving_base=11.3
unit='cm'
speed=40*build_direction
wheel_circumference = 5.6 * pi # standard small Spike Prime set wheels <---- default value

#########################################################################
# Configuration
#########################################################################
from spike import MotorPair, ForceSensor

motor_pair = MotorPair('D', 'C') # left, right motors
motor_pair.set_motor_rotation(amount=wheel_circumference, unit=unit) # <---- default value
bump = ForceSensor('B') # Initialize the Force Sensor

base_radius = driving_base / 2
base_circumference = 2 * pi * base_radius

print(task, 'starting')

#########################################################################
# Copied from Task5 (reusable library)
#########################################################################
def turn(degrees):
    arc = (build_direction*degrees/360) * base_circumference
    steeringunits=100 # rotate in place
    motor_pair.move(amount=arc, unit=unit, steering=steeringunits, speed=speed)
    return

#########################################################################
# Perform movement
#########################################################################

print(task, 'circle-move', 'start')

print(task, 'enter into an endless circle until bumped')
motor_pair.start(steering=build_direction*53, speed=speed) # about 1 ft diameter

isRunning = True

while (isRunning):
    if bump.is_pressed():
        isRunning = False
        print(task, 'bumped into something!')

motor_pair.stop()
print(task, 'circle-move', 'stop')

def moveSideOfSquare(distance):
    motor_pair.move(amount=distance, unit=unit, steering=0, speed=speed)

print(task, 'square-move', 'start')

for count in range(4):
    turn(90)
    print(task, 'square-move', 'side')
    moveSideOfSquare(30)

print(task, 'square-move', 'done')

