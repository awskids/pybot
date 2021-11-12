# Topics

## Coordinate System

A cartesian coordinate system which has its origin at the footprint of the robot.
It describes the position of the robot regarding the World-coordinates.

## Sync vs Async methods

Most operations are synchronous (sync).  This means that when they are invoked that they don't return until complete.

Start is asynchronous (async).  This means you will invoke it and the function will return immediately.  You have to evaluate when the action is done to your satisfaction.

## Turn Experiment

determine the meaning of steering units

![view](./images/TurnExperiment.png)

Plotted experimental data on a graph & derived a formula describing steeringunits from "turning diameter".

> steeringunits = (2000/diameter_cm - 10)

![view](./images/RegressionWithError.png)

## Find fiducial

![view](./images/GridSearch.png)

![view](./images/RandomWalk.png)

## Calculating Path

1. Center of Wheelbase
2. From a wheel

### Correction for offset writing implement

Markers added to your Spike Prime are commonly placed center line (left/right) and at the front of the Driving base.

Define paths for the marker.
If the marker is always down, then turns become very difficult to calculate.

With elevation control on the writing implement, your robot can reposition itself to handle discontinuous shapes, i.e. 90 degree agles.



## Modes of Driving

1. move - manage two motors as a single vector
2. move_tank - command two motors differently but at the same time.
3. individual motors

## Methods of Turning

1. pivot on a wheel (interior angle)
2. stop and rotate at center of base
3. arc

### pivot on a wheel

#### Example turning 1

```python
  from spike import Motor
  left_motor = Motor('D')
  right_motor = Motor('C')
  rotations=distance_cm/wheel_circumference
  left_motor.run_for_rotations(rotations, speed=speed) # SYNC
  right_motor.run_for_rotations(rotations, speed=speed) # SYNC
```

#### Example turning 2

```python
  from spike import Motor
  left_motor = Motor('D')
  right_motor = Motor('C')
  seconds=1
  left_motor.run_for_seconds(seconds, speed=speed) # SYNC
  right_motor.run_for_seconds(seconds, speed=speed) # SYNC
```

## Code Reuse

Spike App provides a limited execution environment for Python.
It currently only supports a single file per project.

Code Reuse will be limited to Class and function definitions within you single project file.
