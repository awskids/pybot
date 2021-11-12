#########################################################################
# TASK DESCRIPTION
# ping-pong, use two touch sensors in a chasm
# bump sensor #1 on front
# bump sensor #2 on back
#########################################################################
task="task14"

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
simulate_second_sensor = True # since kit comes with only one sensor it may be needed to simulate

#########################################################################
# Configuration
#########################################################################
from spike import MotorPair, ForceSensor

motor_pair = MotorPair('D', 'C') # left, right motors
motor_pair.set_motor_rotation(amount=wheel_circumference, unit=unit) # <---- default value
bump1 = ForceSensor('B') # Initialize the Force Sensor

if not simulate_second_sensor:
    bump2 = ForceSensor('A') # Initialize the Force Sensor

base_radius = driving_base / 2
base_circumference = 2 * pi * base_radius

print(task, 'starting')




#########################################################################
# Perform movement
#########################################################################

def go_forward_till_bump():
    motor_pair.start(steering=0, speed=speed)

    isRunning = True

    while (isRunning):
        if bump1.is_pressed():
            isRunning = False
            print(task, 'bumped into something!')

    motor_pair.stop()


def go_backward_till_bump():
    motor_pair.start(steering=0, speed=-1*speed)

    isRunning = True

    if not simulate_second_sensor:
        while (isRunning):
            if bump2.is_pressed():
                isRunning = False
                print(task, 'bumped into something!')
    else:
        import utime
        utime.sleep(1)
        motor_pair.stop()


loop = 0
while True:
    if loop % 2 == 0:
        go_forward_till_bump()
    else:
        go_backward_till_bump()
    loop +=1