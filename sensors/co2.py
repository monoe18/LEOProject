import time
import board
import adafruit_scd4x


def sampleCo2():
    i2c = board.I2C()
    scd4x = adafruit_scd4x.SCD4X(i2c)
    scd4x.start_periodic_measurement()
    if scd4x.data_ready:
    return  scd4x.CO2
