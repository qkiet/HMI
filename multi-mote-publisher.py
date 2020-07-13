import logging
import paho.mqtt.client as mqtt
import time
import sys

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
    print('Received on {0}: {1}'.format(msg.topic, cmd))
    if(cmd == "ON"):
    	s.sendall(b'led_on')
    elif(cmd == "OFF"):
    	s.sendall(b'led_off')
    sys.stdout.flush()

client = mqtt.Client()
client.username_pw_set(USERNAME, KEY)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.connect(ADAFRUIT_SERVER, port=ADAFRUIT_PORT)

print('Publishing a new message every 10 seconds (press Ctrl-C to quit)...')
while True:
    print("Turn light on mote 2")
    client.publish(PATH, "2_ON")
    time.sleep(5)
    print("Turn light off mote 2")
    client.publish(PATH, "2_OFF")
    time.sleep(5)
    print("Turn light on mote 3")
    client.publish(PATH, "3_ON")
    time.sleep(5)
    print("Turn light off mote 3")
    client.publish(PATH, "3_OFF")
    time.sleep(5)
    print("Turn light on mote 4")
    client.publish(PATH, "4_ON")
    time.sleep(5)
    print("Turn light off mote 4")
    client.publish(PATH, "4_OFF")
    time.sleep(5)
