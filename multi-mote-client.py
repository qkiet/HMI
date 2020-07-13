import logging
import paho.mqtt.client as mqtt
import time
import sys

import socket

HOST = ['aaaa::212:7402:2:202', 'aaaa::212:7403:3:303', 'aaaa::212:7404:4:404']  # Standard loopback interface address (localhost)

PORT = 3000        # Port to listen on (non-privileged ports are > 1023)



USERNAME  = 'tuannv'
KEY       = 'aio_vCRp50VNZfCzjGLQou8mf9mjBltj'

ADAFRUIT_SERVER    = 'io.adafruit.com'
ADAFRUIT_PORT      = 1883

PATH      = USERNAME + '/feeds/Light'

def on_connect(client, userdata, flags, rc):
    print('Connected!')
    client.subscribe(PATH)
    print('Subscribed to path {0}'.format(PATH))

def on_disconnect(client, userdata, rc):
    print('Disconnected!')

def on_message(client, userdata, msg):
    cmd = msg.payload.decode('utf-8')
    s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    print('Received on {0}: {1}'.format(msg.topic, cmd))
    if (int(cmd[0]) == 2): #findout which address
        destination_index = 0
    elif (int(cmd[0]) == 3):
        destination_index = 1
    elif (int(cmd[0]) == 4):
        destination_index = 2
    if (cmd[2:] == "ON"):
        send_data = "led_on"
    elif (cmd[2:] == "OFF"):
        send_data = "led_off"

    s.connect((HOST[destination_index], PORT))
    print(destination_index)
    print(send_data)
    s.sendall(send_data.encode())
    sys.stdout.flush()
    s.close()

client = mqtt.Client()
client.username_pw_set(USERNAME, KEY)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.connect(ADAFRUIT_SERVER, port=ADAFRUIT_PORT)
client.loop_forever()
