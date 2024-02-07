from picozero import pico_led, Switch, RGBLED, Speaker
from time import sleep
pico_led.on()

switch = Switch(14)
rgb = RGBLED(3, 1, 5)
speaker = Speaker(12)
def pop():
    print("Pop")
    rgb.color = (255, 0, 255)
    sleep(2)
    rgb.off()
    sleep(2)

    
def pop_different_color():
    print("Pop")
    rgb.color = (255, 0, 0)
    speaker.play(261, 1)
    sleep(2)
    speaker.play(293 , 1)
    sleep(2)
    rgb.color = (255, 255, 0)
    sleep(2)
    rgb.color = (0, 255, 0)
    sleep(2)
    rgb.off()
    sleep(2)
i = 0
while i < 10:
    if switch.is_closed:
        rgb.off()
    else:
        pop_different_color()
        i += 1
pico_led.off()