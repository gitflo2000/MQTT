import paho.mqtt.client as mqtt
BROKER_ADDRESS = "broker.hivemq.com"
PORT = 1883
client = mqtt.Client()
client.connect(BROKER_ADDRESS, PORT, 60)

client.publish("my/temperatur", "25 C")
client.disconnect()