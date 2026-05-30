import machine
import utime

led_onboard = machine.Pin("LED", machine.Pin.OUT)


led_onboard.value(1)
utime.sleep(2)
led_onboard.value(0)
