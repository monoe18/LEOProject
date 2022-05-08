import VEML7700
import SCD41
import time

on = False
rate = 1

_scd41 = None
_veml7700 = None

co2 = None
temperature = None
humidity = None
lux = None
light = None

def setup():
  _scd41 = SCD41.init()
  _veml7700 = VEML7700.init()
  on = True

def loop():
  while(on):
  #sample CO2
    co2 = SCD41.sampleCo2(_scd41)
  #sample Temperature
    temperature = SCD41.sampleTemperature(_scd41)
  #sample Humanity
    humidity = SCD41.sampleHumidity(_scd41)
    
  #sample Light and Lux
    light, lux = VEML7700.sampleLight(_veml7700)

    time.sleep(rate)


