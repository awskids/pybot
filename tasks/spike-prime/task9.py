#########################################################################
# TASK DESCRIPTION
# move forward until bumped, then stop
#########################################################################
task="task9"

#########################################################################
# Build: "Driving Base 1"
# * Front is opposite the ball, however motors are reversed
# * Motor forward is -1
# + add force sensor to front of driving base
#########################################################################
from math import *
build_direction=-1
distance_cm=30.48 #cms in 12 inches.
driving_base=11.3
speed=40*build_direction
wheel_circumference = 5.6 * pi # standard small Spike Prime set wheels <---- default value

#########################################################################
# Configuration
#########################################################################
from spike import MotorPair, ForceSensor

motor_pair = MotorPair('D', 'C') # left, right motors
bump = ForceSensor('B') # Initialize the Force Sensor

print(task, 'starting')

#########################################################################
# Perform movement
#########################################################################

print(task, 'move', 'start')
motor_pair.start(steering=0, speed=speed)

isRunning = True

while (isRunning):
    if bump.is_pressed():
        isRunning = False
        print(task, 'bumped into something!')

motor_pair.stop()
print(task, 'move', 'stop')
