import VEML7700
import SCD41
import time
import Servo

rate = 1
counter = 0
#Sensors
servo = Servo.init()
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


def eval():
  if(co2 < 450):
    servo.servo_angle(0)
  if(co2 >= 600): #half open
    servo.servo_angle(90)
  if(co2 > 800): #full open
    servo.servo_angle(180)


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


  if(counter >= 120):
    printSamples()
    eval()
  else:
    print("calibrating sensors")