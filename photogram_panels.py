
degrees = 10 #define degrees turned between each picture

project_name = 'photogrametry_test'


""" SHUTTER TIMES """

uv_365_shutter = ('1')  # switch two uv leds at the same time!
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

panels_left= ('0x20','0x21','0x22','0x23')
panels_right= ('0x24','0x25','0x26','0x27')


""" Function """



import time
import sys
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT) # configure turntable pin out


steps = int((360/degrees))
turndelay = degrees*(0.168)  #empirical calibration


leds = (uv_365,uv_385,uv_405,blue_425,blue_445,blue_460,green_530,green_570,yellow_590,red_620,red_670,ir_730,ir_850,ir_950,white_4000K)
shutters = (uv_365_shutter,uv_385_shutter,uv_405_shutter,blue_425_shutter,blue_445_shutter,blue_460_shutter,green_530_shutter,green_570_shutter,yellow_590_shutter,red_620_shutter,red_670_shutter,ir_730_shutter,ir_850_shutter,ir_950_shutter,white_4000K_shutter)

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

def switch_led_photogram(led,panel_left,panel_right):

        os.system ('sudo i2cset -y 1 '+ panel_left +' '+ led)
 #       time.sleep(0.1)
        os.system ('sudo i2cset -y 1 '+ panel_right +' '+ led)
 #       time.sleep(0.1)


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]
    
    
# def take_photo(step,led):
    # deg = str(step * degrees)
    # os.system ('gphoto2 --set-config eosremoterelease=Immediate --set-config capturetarget=1 --wait-event=2s --set-config eosremoterelease="Release Full" --wait-event-and-download=5s --filename "/3Dspectral/%Y%m%d/' + project_name + '/%H%M%S - ' + deg +' deg ' + led + ' .cr2"')

    
def take_photo(shutter):
 
    os.system ('sudo gphoto2 --set-config shutterspeed=' + shutter)
    os.system ('sudo gphoto2 --capture-image')
    
def turn_table():   
    GPIO.output(7, GPIO.HIGH)
    print ('turn!')
    time.sleep(turndelay) # turn defined degrees
    GPIO.output(7, GPIO.LOW)
    time.sleep(1.0) # turn 10 

""" switch off all leds """
init_panel()
switch_off_panel()


""" main loop """


for step in range(steps):

    for led, shutter in zip(leds, shutters):
        switch_led_photogram(led, panels_left[0],panels_right[0])
	switch_led_photogram(led, panels_left[1],panels_right[1])
        switch_led_photogram(led, panels_left[2],panels_right[2])
	switch_led_photogram(led, panels_left[3],panels_right[3])

        time.sleep(1) # turn 10
        take_photo(shutter)
        time.sleep(0.1) # turn 10
        switch_off_panel()
        
    turn_table()
