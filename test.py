from gpiozero import LED
from time import sleep

led = LED(25)

led.on()   # Turn on LED
sleep(2)   # Wait for 2 seconds
led.off()  # Turn off LED
sleep(2)   # Wait for 2 seconds to observe the result
