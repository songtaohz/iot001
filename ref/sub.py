import paho.mqtt.client as mqtt

from grovepi import *
import time

led = 4
pinMode(led,"OUTPUT")
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client,userdata, flags, rc):
    print("connected with result code "+str(rc))
# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.
    client.subscribe("myTopic21")
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    print(str(msg.payload))
    if (str(msg.payload) == "0"):
        digitalWrite(led,0)		# Send LOW to switch off LED
        print ("LED OFF!")
    else:
        digitalWrite(led,1)		# Send HIGH to switch on LED
        print ("LED ON!")
        
client = mqtt.Client()
#client.username_pw_set("user51", password="jrKVAYMk")
client.on_connect = on_connect
client.on_message = on_message
#client.connect("202.50.209.80", 1883, 60)
client.connect("localhost")
client.loop_forever()
