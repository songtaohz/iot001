


import grovepi
import grove_rgb_lcd

from grove_rgb_lcd import setRGB, setText, setText_norefresh
from time import sleep
from math import isnan
#import time


#Sensor Input
light =2    # Adc Port 2 - Light sensor
rotary = 0  # Adc Port 0 - Humidity temperature sensor
dht_port = 2 # DC Port 2 - Humidity temperature sensor
dht_type = 0 # use 0 for the blue-colored sensor and 1 for the white-colored sensor


#Output
relay = 8   # DC Port 8 - Relay
led = 4     # DC Port 4 - Led
buzzer = 7  # DC Port 7 - Buzzer



grovepi.pinMode(dht_port,"INPUT")
grovepi.pinMode(light,"INPUT")
grovepi.pinMode(rotary,"INPUT")


grovepi.pinMode(relay,"OUTPUT")
grovepi.pinMode(led,"OUTPUT")
grovepi.pinMode(buzzer,"OUTPUT")

# set orange as background color


#------------------------------------- ------------------------------------------#
grove_rgb_lcd.setRGB(205,31,0)



while True:
	try:

		[ temp,humi ] = grovepi.dht(dht_port,dht_type)
		print("Temperature is",temp,"C\tHumidity is", humi,"%")

		if isnan(temp) is True or isnan(humi) is True:
			raise TypeError('nan error')

		t = str(temp)
		h = str(humi)

		# instead of inserting a bunch of whitespace, we can just insert a \n
		# we're ensuring that if we get some strange strings on one line, the 2nd one won't be affected
		setText_norefresh("Temp:" + t + "C\n" + "Humidity :" + h + "%")

	except (IOError, TypeError) as e:
		print(str(e))
		# and since we got a type error
		# then reset the LCD's text
		setText("")

	except KeyboardInterrupt as e:
		print(str(e))
		# since we're exiting the program3
		# it's better to leave the LCD with a blank text
		setText("")
		break

	# wait some time before re-updating the LCD
	sleep(0.05)

# -------------------------------------------------------------------------------#
