import paho.mqtt.client as mqtt
from flask import Flask

#Testing with Flask server but doesn't support live data. Doesn't work with current state of the system.
#The subscribing client currently exists on the AWS server environment
MQTT_TOPIC = [("LEODataF22/Temperature",0),("LEODataF22/Humidity",0),("LEODataF22/Light",0),("LEODataF22/Co2",0),("LEODataF22/Lux",0)]
temperature = 0
humidity = 0
light = 0
Co2 = 0
lux = 0

app = Flask(__name__)
print("start life")
def messageFunction (client, userdata, message):
    if(str(message.topic) == "LEODataF22/Temperature"):
        global temperature 
        temperature = message.payload.decode("utf-8")
    elif (str(message.topic) == "LEODataF22/Humidity"):
        global humidity
        humidity = message.payload.decode("utf-8")
    elif (str(message.topic) == "LEODataF22/Light"):
        global light
        light = message.payload.decode("utf-8")
    elif (str(message.topic) == "LEODataF22/Co2"):
        global Co2
        Co2 = message.payload.decode("utf-8")
    elif (str(message.topic) == "LEODataF22/Lux"):
        global lux
        lux = message.payload.decode("utf-8")
    print(message.payload.decode("utf-8"))
    
     
ourClient = mqtt.Client("LEOFlaskF22")
ourClient.connect("test.mosquitto.org", 1883)
ourClient.subscribe(MQTT_TOPIC)

ourClient.on_message = messageFunction # Attach the messageFunction to subscription
ourClient.loop_start() # Start the MQTT client
print("life life ")

@app.route("/")
def hello_world():
    return "<p>"+ "Temp: " + str(temperature) + "</p> \n<p>"+ "Humi: " + str(humidity) + "</p> \n<p>"+ "Light: "  + str(light) + "</p> \n<p>"+ "Lux: " + str(lux) + "</p> \n<p>"+ "Co2: " + str(Co2) + "</p> \n"