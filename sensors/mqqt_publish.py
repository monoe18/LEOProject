from random import randint
from time import sleep
import time
import paho.mqtt.publish as publish

while True:
    time.sleep(1)
    value = randint(0, 10)
    publish.single("group07/test", value , hostname="3.73.44.177", port=1883, auth={'username':"group07", 'password':"raspberry"})
    print(value)
 