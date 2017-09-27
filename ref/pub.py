import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("connected with result code "+str(rc))

def on_publish(client, packet, mid):
    print("published")

def on_disconnect(client, userdata, rc):
    print("disconnected")

client=mqtt.Client()
# client.username_pw_set("gprado", password="m3x1c0")
client.on_connect = on_connect
client.username_pw_set("user51", password="jrKVAYMk")
client.on_publish = on_publish
client.on_disconnnect = on_disconnect
client.connect("202.50.209.80", 1883, 60)
client.loop_start()
client.publish("myTopic1", "0")
client.disconnect()
client.loop_stop()
