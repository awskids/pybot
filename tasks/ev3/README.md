# ev3 direct

TODO: how to tell which version of Pybricks is being run?
TODO: accuracy of turns is not great, how to improve?

## Assumptions

using Pybricks 2.0
https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3


## Documentation

https://pybricks.com/ev3-micropython/robotics.html
https://pybricks.com/

### Sdcard instructions

https://education.lego.com/en-us/product-resources/mindstorms-ev3/teacher-resources/python-for-ev3

### WIP

```python
print ("right wheel should have moved one full rotation")
test_motor.run_target(500, 360)

feed_motor.run_until_stalled(120, duty_limit=50)
feed_motor.run_angle(450, -200)

belt_motor.run(-500)

belt_motor.reset_angle(0)

arm_motor.run_angle(ARM_MOTOR_SPEED, 30, wait=False)

angle = wheel.angle()
```

robot.settings(straight_speed=speed, turn_rate=speed/10) # turn slow to avoid slippage?

# Parameters:	
# straight_speed (speed: mm/s) – Speed of the robot during straight().
# straight_acceleration (linear acceleration: mm/s/s) – Acceleration and deceleration of the robot at the start and end of straight().
# turn_rate (rotational speed: deg/s) – Turn rate of the robot during turn().
# turn_acceleration (rotational acceleration: deg/s/s) – Angular acceleration and deceleration of the robot at the start and end of turn().

