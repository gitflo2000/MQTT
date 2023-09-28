import paho.mqtt.client as mqtt

TOPIC = "home/tutorial/PubSubDemo"
BROKER_ADDRESS = "broker.hivemq.com"
PORT = 1883
QOS = 1

if __name__ == "__main__":
    client = mqtt.Client()

    LAST_WILL = "Verbindung beendet!"
    client.will_set(TOPIC, LAST_WILL, qos=QOS, retain=False)

    client.connect(BROKER_ADDRESS, PORT)
    print("Connected to MQTT Broker: " + BROKER_ADDRESS)

    DATA = "{TEST_DATA}"
    client.publish(TOPIC, DATA, qos=QOS)

    client.loop()