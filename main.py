from paho.mqtt import client as mqtt_client
from mongo_conf import get_total_votes
from influx_conf import count_people
from time import sleep

BROKER = 'BROKER'
PORT = 1883
BASE_TOPIC = 'aclearn/'
USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, usedata, flags, rc):
        if rc == 0:
            print('Conectado a Broker MQTT')
        else:
            print('La conexion al Broker ha fallado')

    client = mqtt_client.Client("some_id")
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client


def publish(client: mqtt_client):
    while True:
        client.publish(BASE_TOPIC + "votos", get_total_votes())
        client.publish(BASE_TOPIC + "ocupancia", count_people())
        sleep(60)


def run_publisher():
    client = connect_mqtt()
    publish(client)
    client.loop_forever()


if __name__ == "__main__":
    run_publisher()
