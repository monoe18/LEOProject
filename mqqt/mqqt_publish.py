import paho.mqtt.publish as publish
ourClient = mqtt.Client("LEOPI")
ourClient.connect("test","mosquitto.org", 1883)
ourClient.publish("Data", "ThisIsATest") 