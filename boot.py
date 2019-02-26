#
# if intpin interrupted start timer
# utime.ticks_ms()
# and sent time to display until next interrupt
# after last interrupt show time for 10 sec
#
# TO DO:
# add hardware interrupt instead read pin status - done
# add RFID 
# add webserver
# add database for saving results
# add button for best time...
# add buttons for checking trace
#

import max7219
import utime
from machine import Pin, SPI

## variable set
interruptState = 0
sleepDelay = 5
showDelay = 10000
lastRun = 0
startRun = 0
#names = {"0":"noname", "36":"xandr", "7":"Maks"}
results = []

## function set
def lapRuns(p):
	global interruptState
	interruptState = 1
def addZero(digit):
	if int(digit) <= 9:
		digit = "0" + str(digit)
	return str(digit)
def showTimer(time):
	seconds,millis = divmod(time,1000)
	minutes,seconds = divmod(seconds,60)
	seconds = addZero(seconds)
	cOutput = str(seconds)+str(millis)
	display.fill(0)
	display.text(str(cOutput),0,0,1)
	if minutes > 0:
		position = (minutes * 8) - 1
		display.line(0,7,position,7,1)
	display.show()
#def debounce():

# init inputs and outputs
## pin for button or ir sensor
pin17 = Pin(17, Pin.IN, Pin.PULL_DOWN)
pin17.irq(trigger=Pin.IRQ_RISING, handler=lapRuns)
spi = SPI(-1, 10000000, miso=Pin(12), mosi=Pin(13), sck=Pin(14))
# display
display = max7219.Matrix8x8(spi, Pin(15), 4)
display.brightness(13)
# print(pin19.value())

# Main loop
while True:
	if interruptState == 1:
		#print("inputState = 0")
		lastRun = utime.ticks_diff(utime.ticks_ms(), startRun)
		startRun = utime.ticks_ms()
		results.append(lastRun)
		# avoid IRQ loop
		#state = disable_irq()
		interruptState = 0
		#enable_irq(state)
		while utime.ticks_diff(utime.ticks_ms(), startRun) < showDelay:
			#print(lastRun)
			showTimer(lastRun)
			utime.sleep_ms(sleepDelay)
		#print(results)
		interruptState = 0
	run = utime.ticks_diff(utime.ticks_ms(), startRun)
	#print(run)
	showTimer(run)
	#print(utime.ticks_diff(utime.ticks_ms(), startRun))
	utime.sleep_ms(sleepDelay)
