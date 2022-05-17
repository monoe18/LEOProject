import paho.mqtt.client as mqtt

def connect():
    c = mqtt.Client("LEOPI")
    c.connect("3.73.44.177", 1883)
    c.username_pw_set("group07", "raspberry")
    return c

def publishData(c, topicName, data):
    print("sending data to: " + "group07/"+topicName)
    c.publish("group07/"+topicName, data) 
