#Raspberry Pi + Grove Switch + Grove Relay

import time
import grovepi
# Connect the Grove Switch to digital port D3
# SIG,NC,VCC,GND

#Input
dth = 2
light =2
rotary = 0

#Output
relay = 8
led = 4
buzzer = 7


grovepi.pinMode(dth,"INPUT")
grovepi.pinMode(light,"INPUT")
grovepi.pinMode(rotary,"INPUT")


grovepi.pinMode(relay,"OUTPUT")
grovepi.pinMode(led,"OUTPUT")
grovepi.pinMode(buzzer,"OUTPUT")



while True:
    try:
        if grovepi.digitalRead(switch):
            grovepi.digitalWrite(relay,1)
        else:
            grovepi.digitalWrite(relay,0)
            time.sleep(.05)
    except KeyboardInterrupt:
        grovepi.digitalWrite(relay,0)
        break
    except IOError:
        print "Error"
