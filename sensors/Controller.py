import VEML7700
import SCD41
import time

on = False
rate = 1
counter = 0
#Sensors
scd41 = None
veml7700= None

co2 = None
temperature = None
humidity = None
lux = None
light = None

def printSamples():
  print("Light: " , light)
  print("Lux: ", lux)
  print("Temperature: ", temperature)
  print("Co2: ", co2)
  print("Humidity: " , humidity)

while(on):
  #sample CO2
  co2 = SCD41.sampleCo2(scd41)
  #sample Temperature
  temperature = SCD41.sampleTemperature(scd41)
  #sample Humanity
  humidity = SCD41.sampleHumidity(scd41)
  #sample Light and Lux
  light, lux = VEML7700.sampleLight(veml7700)
  counter += 1

  time.sleep(rate)
  printSamples()
  
  if(counter == 1000):
    on = False