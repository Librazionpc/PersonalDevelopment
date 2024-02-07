from picozero import pico_led, RGBLED, Pot
from time import sleep

pico_led.on()
rgb = RGBLED(2, 3, 4)
dial = Pot(2)

# def happy():
#     rgb.color = (0, 255, 0) # Green
# 
# def good():
#     rgb.color = (75, 255, 0) # Yellow-green
# 
# def okay():
#     rgb.color = (255, 150, 0) # Yellow
# 
# def unsure():
#     rgb.color = (255, 25, 0) # Orange
# 
# def unhappy():
#     rgb.color = (255, 0, 0) # Red
# 
# i = 0
# while True:
#     mood = dial.value * 100 # turning to a percentage
#     print(mood)
#     if mood < 20:
#         print("Happy")
#         happy()
#     elif mood < 40:
#         good()
#     elif mood < 60:
#         okay()
#     elif mood < 80:
#         unsure()
#     else:
#         unhappy()
#     sleep(0.1)
#     i += 1

rgb.off
pico_led.off()