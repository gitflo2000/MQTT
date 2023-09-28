import paho.mqtt.client as mqtt
BROKER_ADDRESS = "broker.hivemq.com"
PORT = 1883
print("on_message")

def on_message(client, userdata, msg):
    print("my/temperatur")
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.connect(BROKER_ADDRESS, PORT, 60)
client.subscribe("my/temperatur")
client.on_message = on_message
client.loop_forever()