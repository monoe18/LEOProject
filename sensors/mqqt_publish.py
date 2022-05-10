import paho.mqtt.publish as publish

publish.single("PlantHealth/temperature", "Hello", hostname="localhost")
print("Done")
 