""" 3D SPECTRAL turntable script"""
""" led tests """


import anvil.server

anvil.server.connect("FAB74JM5CPC3VPWPRDE4XXQ3-L2P7QKFGTWGJGAHR")

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


leds = (uv_365,uv_385,uv_405,blue_425,blue_445,blue_460,green_530,green_570,yellow_590,red_620,red_670,ir_730,ir_850,ir_950,white_4000K)

""" Function """

def init_panel():
# initialisation of the 8 MCP23017 (all out)    

        os.system ('sudo i2cset -y 1 0x20 0x00 0x00')
        time.sleep(0.1)
        os.system ('sudo i2cset -y 1 0x20 0x01 0x00')
        time.sleep(0.1)

    

def switch_off_panel():
# initialisation of the 8 MCP23017 (all out)    

        os.system ('sudo i2cset -y 1 0x20 0x14 0x00')
        time.sleep(0.1)
        os.system ('sudo i2cset -y 1 0x20 0x15 0x00')
        time.sleep(0.1)
    



def switch_led_photogram(led):

        os.system ('sudo i2cset -y 1 0x20 ' + led)
        time.sleep(0.1)



""" switch off all leds """
init_panel()
switch_off_panel()


""" main loop """
@anvil.server.callable
def flash_leds():
    for led in leds:
        print("leds flashing!")
        switch_led_photogram(led)
        time.sleep(0.1) # turn 10
        switch_off_panel()    
        

anvil.server.wait_forever()