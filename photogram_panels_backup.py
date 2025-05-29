""" 3D SPECTRAL PHOTOGRAMMETRY script"""

""" SHUTTER TIMES """

uv_365_shutter = ('2')  # switch two uv leds at the same time!
uv_385_shutter = ('1') 
uv_405_shutter = ('1')

blue_425_shutter = ('1')
blue_445_shutter = ('1')
blue_460_shutter = ('1')
green_530_shutter = ('1')

green_570_shutter = ('1')
yellow_590_shutter  = ('1')
red_620_shutter  = ('1')
red_670_shutter  = ('1')

ir_730_shutter  = ('1')
ir_850_shutter  = ('1')
ir_950_shutter  = ('1')
white_4000K_shutter  = ('1')





""" LEDS ADRESSES """

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




import time
import sys
import os



leds = (uv_365,uv_385,uv_405,blue_425,blue_445,blue_460,green_530,green_570,yellow_590,red_620,red_670,ir_730,ir_850,ir_950,white_4000K)
shutters = (uv_365_shutter,uv_385_shutter,uv_405_shutter,blue_425_shutter,blue_445_shutter,blue_460_shutter,green_530_shutter,green_570_shutter,yellow_590_shutter,red_620_shutter,red_670_shutter,ir_730_shutter,ir_850_shutter,ir_950_shutter,white_4000K_shutter)
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

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]
    
def take_photo(shutter):
 
    os.system ('sudo gphoto2 --set-config shutterspeed=' + shutter)
    os.system ('sudo gphoto2 --capture-image')
    

""" switch off all leds """
init_panel()
switch_off_panel()


""" main loop """

for led, shutter in zip(leds, shutters):
    switch_led_photogram(led)
    time.sleep(1) # turn 10
    take_photo(shutter)
    time.sleep(0.1) # turn 10
    switch_off_panel()    
