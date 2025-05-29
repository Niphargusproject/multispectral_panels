""" 3D SPECTRAL turntable script"""
""" led tests """

import time
import sys
import os


""" Fixed stuff """


uv_365 = ('0x15 0x05')  # switch two uv leds at the same time!
uv_385 = ('0x15 0x10') 
uv_405 = ('0x15 0x40')

blue_425 = ('0x15 0x02')
blue_445 = ('0x15 0x08')
blue_460 = ('0x15 0x20')
green_530 = ('0x15 0x80')

green_570 = ('0x14 0x01')
yellow_590 = ('0x14 0x04')
red_620 = ('0x14 0x10')
red_670 = ('0x14 0x40')

ir_730 = ('0x14 0x02')
ir_850 = ('0x14 0x08')
ir_950 = ('0x14 0x20')
white_4000K = ('0x14 0x80')


panels_left= ('0x20','0x21','0x22','0x23')
panels_right= ('0x24','0x25','0x26','0x27')
leds = (uv_365,uv_385,uv_405,blue_425,blue_445,blue_460,green_530,green_570,yellow_590,red_620,red_670,ir_730,ir_850,ir_950,white_4000K)

""" Function """

def init_panel():
# initialisation of the 8 MCP23017 (all out)    
    for panel in panels_left:
        os.system ('sudo i2cset -y 1 ' + panel +' 0x00 0x00')
  #      time.sleep(0.1)
        os.system ('sudo i2cset -y 1 ' + panel +' 0x01 0x00')
  #      time.sleep(0.1)
    for panel in panels_right:
        os.system ('sudo i2cset -y 1 ' + panel +' 0x00 0x00')
  #      time.sleep(0.1)
        os.system ('sudo i2cset -y 1 ' + panel +' 0x01 0x00')
 #       time.sleep(0.1)

    

def switch_off_panel():
# initialisation of the 8 MCP23017 (all out)    
    for panel in panels_left:
        os.system ('sudo i2cset -y 1 ' + panel +' 0x14 0x00')
 #       time.sleep(0.1)
        os.system ('sudo i2cset -y 1 ' + panel +' 0x15 0x00')
 #       time.sleep(0.1)
    for panel in panels_right:
        os.system ('sudo i2cset -y 1 ' + panel +' 0x14 0x00')
 #       time.sleep(0.1)
        os.system ('sudo i2cset -y 1 ' + panel +' 0x15 0x00')
 #       time.sleep(0.1)



def switch_led_photogram(led):
    for panel in panels_left:
        os.system ('sudo i2cset -y 1 '+ panel +' '+ led)
 #       time.sleep(0.1)
    for panel in panels_right:
        os.system ('sudo i2cset -y 1 '+ panel +' '+ led)
#        time.sleep(0.1)



""" switch off all leds """
init_panel()
switch_off_panel()


""" main loop """

for led in leds:
    switch_led_photogram(led)
    time.sleep(0.1) # turn 10
    switch_off_panel()    
