from random import randint
from time import sleep
import time
import paho.mqtt.publish as publish

while True:
    time.sleep(1)
    value1 = randint(0, 50)
    publish.single("group07/Humidity", value1 , hostname="3.73.44.177", port=1883, auth={'username':"group07", 'password':"raspberry"})
    print("Humidity: ", value1)
    value2 = randint(0, 50)
    publish.single("group07/Temperature", value2 , hostname="3.73.44.177", port=1883, auth={'username':"group07", 'password':"raspberry"})
    print("Temperature: ", value2)
    value3 = randint(0, 50)
    publish.single("group07/C02", value3 , hostname="3.73.44.177", port=1883, auth={'username':"group07", 'password':"raspberry"})
    print("C02: ", value3)
    value4 = randint(0, 50)
    publish.single("group07/Lux", value4 , hostname="3.73.44.177", port=1883, auth={'username':"group07", 'password':"raspberry"})
    print("Lux: ", value4)
    value5 = randint(0, 50)
    publish.single("group07/Light", value5 , hostname="3.73.44.177", port=1883, auth={'username':"group07", 'password':"raspberry"})
    print("Light: ", value5)
 