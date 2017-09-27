import time
import grovepi
import pub
import paho.mqtt.client as mqtt

# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND
button = 3

grovepi.pinMode(button,"INPUT")
client=mqtt.Client()
client.username_pw_set("user51", password="jrKVAYMk")
client.on_connect = pub.on_connect
client.on_publish = pub.on_publish
client.on_disconnnect = pub.on_disconnect
client.connect("202.50.209.80", 1883, 60)

while True:
    try:
        button_status = grovepi.digitalRead(button)
        #if button_status:
        print(grovepi.digitalRead(button))
        client.loop_start()
        client.publish("myTopic21", button_status, 0)
        #client.disconnect()
        client.loop_stop()
        time.sleep(.2)

    except IOError:
        print ("Error")
