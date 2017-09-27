import paho.mqtt.client as mqtt

from grovepi import *
import time

led = 4
pinMode(led,"OUTPUT")

def on_connect(client, userdata, flags, rc):
    print("result"+str(rc))
    client.subscribe("myTopic21")
def on_message(client, userdata, msg):
    print(str(msg.payload))
          
client = mqtt.Client()
client.username_pw_set("user51", password="jrKVAYMk")
client.on_connect = on_connect
client.on_message = on_message
client.connect("202.50.209.80", 1883, 60)
client.loop_forever()
