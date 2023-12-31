import paho.mqtt.client as mqtt
BROKER_ADDRESS = "broker.hivemq.com"
PORT = 1883
# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test")

def on_message(client, userdata, msg):
  if msg.payload.decode() == "Hello world!":
    print("Yes!")
    client.disconnect()
    
client = mqtt.Client()
client.connect(BROKER_ADDRESS,PORT,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()