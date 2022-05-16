import paho.mqtt.client as mqtt

def connect():
    c = mqtt.Client("LEOPI")
    c.connect("54.196.159.162", 1883)
    return c

def publishData(c, topicName, data):
    print("sending data to: " + "LEODataF22/"+topicName)
    c.publish("LEODataF22/"+topicName, data) 
