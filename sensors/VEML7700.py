import time
import board
import busio
import adafruit_veml7700

def init():
    i2c = busio.I2C(board.SCL, board.SDA)
    veml7700 = adafruit_veml7700.VEML7700(i2c)
    return veml7700

def sampleLight(veml7700):
    return veml7700.light, veml7700.lux

