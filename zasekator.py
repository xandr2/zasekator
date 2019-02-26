# https://github.com/adafruit/micropython-adafruit-max7219
#
#
#
#

import machine
import utime

# init inputs and outputs
## pin for button or ir sensor
pin17 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)
# print(pin19.value())

## function set
#def debounce():
#def timer():

## variable set
inputState = 0
lastInputState = 1
lastDebounceTime = 0
debounceDelay = 10
showDelay = 10000
lastRun = 0
startRun = 0

#names = {"0":"noname", "36":"xandr", "7":"Maks"}
results = []

## pin for display or digits

while True:
	startReading = pin17.value()
	if startReading != lastInputState:
		lastDebounceTime = utime.ticks_ms()
	if utime.ticks_diff(utime.ticks_ms(), lastDebounceTime) > debounceDelay:
		if startReading != inputState:
			inputState = startReading
			if inputState == 0:
				print("inputState = 0")
				lastRun = utime.ticks_diff(utime.ticks_ms(), startRun)
				startRun = utime.ticks_ms()
				results.append(lastRun)
				while utime.ticks_diff(utime.ticks_ms(), startRun) < showDelay:
					print(lastRun)
					utime.sleep(0.2)
				print(results)
	lastInputState = startReading
	print(utime.ticks_diff(utime.ticks_ms(), startRun))
	utime.sleep(0.2)

# if intpin interrupted start timer
# utime.ticks_ms()
# and sent time to display until next interrupt
# after last interrupt show time for 15 sec


# TO DO:
# add RFID 
# add webserver
# add database for saving results
# add button for best time...
# add buttons for checking trace
#


