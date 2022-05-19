import time
import board
import adafruit_scd4x
 
def init():
    i2c = board.I2C()
    scd4x = adafruit_scd4x.SCD4X(i2c)
    scd4x.start_periodic_measurement()
    return scd4x

def sampleCo2(scd4x):
    return  scd4x.CO2

def sampleHumidity(scd4x):
    return  scd4x.relative_humidity

def sampleTemperature(scd4x):
    return  scd4x.temperature