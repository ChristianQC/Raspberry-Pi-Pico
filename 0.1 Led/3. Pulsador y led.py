from machine import Pin
import utime

led = machine.Pin(25,Pin.OUT)
pulsador = Pin(9,Pin.IN,Pin.PULL_UP)

while True:
    if pulsador.value() == False:
        led.value(1)
        utime.sleep(0.1)
    else:
        led.value(0)
        utime.sleep(0.1)
