import VEML7700
import SCD41
import time

rate = 1
counter = 0
#Sensors
scd41 = SCD41.init()
veml7700= VEML7700.init()
on = True

co2 = None
temperature = None
humidity = None
lux = None
light = None

def printSamples():
  print("Light: \t" , light)
  print("Lux: \t", lux)
  print("Temperature: \t", temperature)
  print("Co2: \t", co2)
  print("Humidity: \t" , humidity)
  print("#########################################################################")

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