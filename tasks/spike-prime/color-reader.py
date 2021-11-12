from spike import ColorSensor
import utime

color_sensor = ColorSensor('A')


while True:
    color = color_sensor.get_color()
    print('Found color', color)
    utime.sleep(1)