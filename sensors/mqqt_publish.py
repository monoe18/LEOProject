import paho.mqtt.publish as publish

publish.single("PlantHealth/temperature", "Hello", hostname="192.168.87.51")
print("Done")
 