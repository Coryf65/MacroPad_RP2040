import board
import digitalio
import time

# Setup the LED, uses the Red built in led
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True # turns on the led
    time.sleep(0.1)
    led.value = False # turn off
    time.sleep(0.5)