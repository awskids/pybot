# Pybot - Python Robot Challenges

Companion python code for teachers to move beyond LowCode logic development.

> Goal is to progress from task 1 to the end.

## Basic Platform Movement

Task|Description|Difficulty
----|-----------|----------
1| [MOVE FORWARD ONE BLOCK](./tasks/instructions/task1.md)|standard
2| [MAKE A SQUARE](./tasks/instructions/task2.md)|standard
3| [MAKE AN EQUILATERAL TRIANGLE](./tasks/instructions/task3.md)|standard
4| [MAKE A CIRCLE AROUND A FLOOR SQUARE](./tasks/instructions/task4.md)|challenge
5| [MAKE A STAR](./tasks/instructions/task5.md)|challenge
6| [INFINITY SYMBOL](./tasks/instructions/task6.md)|difficult
7| [FOUR LEAF CLOVER](./tasks/instructions/task7.md)|difficult
8| [SPIRAL](./tasks/instructions/task8.md)|difficult

## FORCE SENSEOR

Task|Description|Difficulty
----|-----------|----------
9| [MOVE FORWARD UNTIL BUMPED, THEN STOP](./tasks/instructions/task9.md)|standard
10| [MOVE FORWARD UNTIL BUMPED, STOP, THEN REVERSE](./tasks/instructions/task10.md)|standard
11| [MOVE FORWARD - BUMP OBJECT - BOUNCE BACK X4](./tasks/instructions/task11.md)|standard
12| [RUMBA - MOVE FORWARD - HIT OBJECT - BOUNCE BACK - TURN 90 DEGREES - FOREVER LOOP](./tasks/instructions/task12.md)|standard
13| [CIRCLE UNTIL HIT - THEN SQUARE](./tasks/instructions/task13.md)|challenge
14| [PING - PONG - TWO TOUCH SENSORS](./tasks/instructions/task14.md)|standard

## COLOR SENSOR / LIGHT SENSOR

Task|Description|Difficulty
----|-----------|----------
15| [MOVE FORWARD - STOP AT LINE](./tasks/instructions/task15.md)|standard
16| [MOVE FORWARD - STOP AT SECOND LINE](./tasks/instructions/task16.md)|standard
17| [STAY INSIDE THE TRACK](./tasks/instructions/task17.md)|standard
18| [FOLLOW THE LINE](./tasks/instructions/task18.md)|challenge
19| [RACETRACK](./tasks/instructions/task19.md)|difficult

## ULTRASONIC SENSOR

Task|Description
----|-----------
20|STOP 25CM FROM AN OBJECT
21|FOLLOW THE LEADER - MOVE FORWARD THE ROBOT FOLLOWS YOU. STOP THE ROBOT STOPS

## GESTURES, DISPLAY, SOUND, & BUTTONS

Task|Description
----|-----------
22|DOUBLETAPPED, FREEFALL, NONE, SHAKE, and TAPPED
23|Smiley face
24|Sounds
25|Buttons

## How to add flair ?

1. do the task both `forward` and `backward`
2. add a dance move at waypoints along the journey
3. display progress of task
4. display remaining time until task completion
5. add a pencil/marker to robot and draw the path
6. reuse code from a library
7. identify the accuracy of your bot, i.e. how close to the exact waypoints did your bot reach over multiple runs?
8. use centimeters
9. complete task with fastest time
10. when approaching waypoint use speaker
11. how big of a shape can you make?
12. change the style of turning
13. handle errors

## Spike Details

### sensor accuracy

a full rotation around the yaw axis is short by 4/7 degress per rotation

rotate left 360 degress results in gyro saying 4/7 degrees
==> yaw sensor says its not fully rotated.
==> actually the device is fully rotated.
==> therefore yaw sensor is under representing actual rotation.

rotate right 360 degress results in gyro saying -4/-7 degrees
==> yaw sensor is under representing rotation.

if rotate 3 times in same direction, the errors are additive
==> error ends up growing, 3*error ==> 3*4/7 ==> 12/21 degrees of error