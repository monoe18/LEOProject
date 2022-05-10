import paho.mqtt.client as mqtt
ourClient = mqtt.Client("LEOPI")
ourClient.connect("test","mosquitto.org", 1883)
ourClient.publish("Data", "ThisIsATest") 