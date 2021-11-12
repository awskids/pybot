#########################################################################
# TASK DESCRIPTION
# move forward one floor space and stop
# typically 30.48 cm (centimeters) or 12 inches
#########################################################################
task="task1"

#########################################################################
# Build: "Driving Base 1"
# * Front is opposite the ball, however motors are reversed
# * Motor forward is -1
#########################################################################
from math import *
build_direction=-1
distance_cm=30.48 #cm in 12 inches.
driving_base=11.3
speed=20*build_direction
wheel_circumference = 5.6 * pi # standard small Spike Prime set wheels <---- default value

#########################################################################
# Configuration
#########################################################################
from spike import MotorPair

print(task, 'starting')

try:
    motor_pair = MotorPair('D', 'C') # left, right
    motor_pair.set_motor_rotation(amount=wheel_circumference, unit='cm') # <---- default value
    motor_pair.set_stop_action(action='brake')
except Exception as e:
    print(task, 'there was an error setting up motors', str(e))

#########################################################################
# Perform movement
#########################################################################
try:
    print(task, 'move', 'start')
    motor_pair.move(amount=distance_cm, unit='cm', steering=0, speed=speed)
    print(task, 'move', 'done')
except Exception as e:
    print(task, 'there was an error moving', str(e))

#########################################################################
# Alternative #1 (use inches for dimension)
# motor_pair.move(amount=12.0, unit='in', steering=0, speed=speed)

#########################################################################
# Alternative #2 (use movetank)
# motor_pair.move_tank(amount=distance_cm, unit='cm', left_speed=speed, right_speed=speed)

#########################################################################
# Alternative #3 (asynchronous)
# from spike import Motor
# import time

# left_motor = Motor('D')
# right_motor = Motor('C')

# print(task, 'alt3', 'move', 'start')

# # remember, the motors are facing opposite directions
# left_motor.start(speed=-1*speed)
# right_motor.start(speed=speed)

# # how to I determine how long run to run?
# time.sleep(3)

# left_motor.stop()
# right_motor.stop()
# print(task, 'alt3', 'move', 'done')



