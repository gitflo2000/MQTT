import paho.mqtt.client as mqtt
import time
BROKER_ADDRESS = "broker.hivemq.com"
PORT = 1883

# a callback function
def on_message_temperature(client, userdata, msg):
    print('Received a new temperature data ', msg.payload.decode('utf-8'))


def on_message_humidity(client, userdata, msg):
    print('Received a new humidity data ', str(msg.payload.decode('utf-8')))


client = mqtt.Client("greenhouse_server_123")
client.message_callback_add('greenhouse/temperature', on_message_temperature)
client.message_callback_add('greenhouse/humidity', on_message_humidity)

client.connect(BROKER_ADDRESS, PORT)
# start a new thread
client.loop_start()
client.subscribe("greenhouse/#")

while True:
    time.sleep(6)
    # do something you like