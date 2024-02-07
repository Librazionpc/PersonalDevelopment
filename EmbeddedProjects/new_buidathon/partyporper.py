from picozero import pico_led, RGBLED
from time import sleep
pico_led.on()

red1 = RGBLED(9, 10, 11)
red1.color = (255, 0, 0)
red2 = RGBLED(4, 5, 6)
red2.color = (255, 0, 255)
    


