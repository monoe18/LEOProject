import paho.mqtt.client as mqtt
from flask import Flask
MQTT_TOPIC = [("LEODataF22/Temperature"),("LEODataF22/Humidity"),("LEODataF22/Light"),("LEODataF22/Co2"),("LEODataF22/Lux")]
temperature = 0
humidity = 0
light = 0
Co2 = 0
lux = 0

app = Flask(__name__)
print("start life")
def messageFunction (client, userdata, message):
    if(str(message.topic) == "LEODataF22/Temperature"):
        temperature = message.payload.decode("utf-8")
    elif (str(message.topic) == "LEODataF22/Humidity"):
        humidity = message.payload.decode("utf-8")
    elif (str(message.topic) == "LEODataF22/Light"):
        light = message.payload.decode("utf-8")
    elif (str(message.topic) == "LEODataF22/Co2"):
        Co2 = message.payload.decode("utf-8")
    elif (str(message.topic) == "LEODataF22/Lux"):
        lux = message.payload.decode("utf-8")
    
     
ourClient = mqtt.Client("LEOFlaskF22")
ourClient.connect("test.mosquitto.org", 1883)
ourClient.subscribe(MQTT_TOPIC)

ourClient.on_message = messageFunction # Attach the messageFunction to subscription
ourClient.loop_start() # Start the MQTT client
print("life life ")

@app.route("/")
def hello_world():
    return "<p>"+ "Temp: " + temperature + "</p> \n<p>"+ "Humi: " + humidity + "</p> \n<p>"+ "Light: "  + light + "</p> \n<p>"+ "Lux: " + lux + "</p> \n<p>"+ "Co2: " + Co2 + "</p> \n"