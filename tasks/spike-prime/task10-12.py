#########################################################################
# TASK DESCRIPTION
# move forward until bumped, then reverse and try another direction
#########################################################################
task="task10-12"

#########################################################################
# Build: "Driving Base 1"
# * Front is opposite the ball, however motors are reversed
# * Motor forward is -1
# + add force sensor to front of driving base
#########################################################################
import utime, random
from math import *

build_direction=-1
distance_cm=30.48 #cms in 12 inches.
driving_base=11.3
unit='cm'
speed=40*build_direction
wheel_circumference = 5.6 * pi # standard small Spike Prime set wheels <---- default value
start_with_backup = True

#########################################################################
# Configuration
#########################################################################
from spike import MotorPair, ForceSensor

motor_pair = MotorPair('D', 'C') # left, right motors
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

def backup():
    motor_pair.start(steering=0, speed=-1*speed)
    utime.sleep(1)
    motor_pair.stop()

def go_forward_till_obstacle():
    motor_pair.start(steering=0, speed=speed)

    isRunning = True

    while (isRunning):
        if bump.is_pressed():
            isRunning = False
            print(task, 'bumped into something!')

    motor_pair.stop()
    print(task, 'move', 'stop')
    return

print(task, 'move', 'start')
if start_with_backup:
    backup()

def setNewRandomPath():
    new_direction = random.randint(0, 360)
    # print('new_direction =>', new_direction)
    turn(new_direction)

def task10(): 
    task="task10"
    go_forward_till_obstacle()
    backup()

def task11():
    task="task11"
    for count in range(4):
        go_forward_till_obstacle()
        backup()

def task12():
    task="task12"
    while True:
        go_forward_till_obstacle()
        backup()
        turn(90)

def explore():
    task="explore"
    while True:
        go_forward_till_obstacle()
        backup()
        setNewRandomPath()

task10()
# task11()
# task12()
# explore()