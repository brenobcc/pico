from machine import Pin # type: ignore
from time import sleep

led = Pin(25, Pin.OUT)

while True:
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)