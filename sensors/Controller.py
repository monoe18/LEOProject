import VEML7700
import SCD41
import time
import Servo
import RPi.GPIO as GPIO


LED_PIN = 22
rate = 1
counter = 0

#Sensors
servo = Servo.init()
scd41 = SCD41.init()
veml7700= VEML7700.init()

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW) 

on = True
co2 = 0
temperature = 0
humidity = 0
lux = 0
light = 0

def printSamples():
  print("Light: \t" , light)
  print("Lux: \t", lux)
  print("Temperature: \t", temperature)
  print("Co2: \t", co2)
  print("Humidity: \t" , humidity)
  print("#########################################################################")


def eval():
  if(lux <= 300):
    Servo.servo_angle(0,servo)
  elif(lux <= 600 and lux > 300):
    Servo.servo_angle(90,servo)
  elif(lux > 600): 
    Servo.servo_angle(180,servo)

  if(co2 >= 700):
    GPIO.output(LED_PIN, GPIO.HIGH)
  else:
     GPIO.output(LED_PIN, GPIO.LOW)

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


  if(counter >= 10):
    printSamples()
    eval()
  else:
    print("calibrating sensors")

