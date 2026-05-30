from machine import Pin
import time

greenled = Pin(0, Pin.OUT)
redled = Pin(1, Pin.OUT)

print("Green LED will now be turned on.")
greenled.toggle()
print("Red LED will now be turned on.")
redled.toggle()
print("run this again to turn the LEDs off")