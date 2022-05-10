import paho.mqtt.client as mqtt
from flask import Flask

app = Flask(__name__)
print("start life")
def messageFunction (client, userdata, message):
    topic = str(message.topic)
    message = str(message.payload.decode("utf-8"))
    print(topic +":" + message)
     
ourClient = mqtt.Client("LEOFlaskF22")
ourClient.connect("test.mosquitto.org", 1883)
ourClient.subscribe("LEODataF22")
ourClient.on_message = messageFunction # Attach the messageFunction to subscription
ourClient.loop_start() # Start the MQTT client
print("life life ")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"