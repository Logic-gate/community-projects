#! /usr/bin/env python3

__email__ = 'mad_dev@linuxmail.org'
import re
import subprocess
import pifacedigitalio as pio
import time
import datetime

def get_temp_from_system():
        temp = subprocess.check_output(['vcgencmd', 'measure_temp'])
        str_temp = str(temp) #important
        r = re.findall('[0-9]{1}', str_temp) #I am terrible at regex... 
        for_humans = r[0]+r[1]+'.'+r[2]
        return for_humans

def am_i_on(pin):
	return pd.output_pins[int(pin)].value

def run(pin):
	current_date = datetime.datetime.now()
        temp = get_temp_from_system()
        if temp >= '43.0':
		print(temp+' @ '+str(current_date))
		if am_i_on(int(pin)) == 0:
			print('Fan is Off...Starting Fan')
                	pd.output_pins[int(pin)].value = 1
		else:
			time.sleep(25)
			print('Fan is ON')
        elif temp <= '42.9':
		print(temp+' @ '+str(current_date))
		if am_i_on(int(pin)) == 1:
			print('Fan is on...Shuting it Down')
                	pd.output_pins[int(pin)].value = 0
		else:
			time.sleep(25) #Remove, if you want real-time checking
			print('Fan is OFF')
        else:
                pass


pd = pio.PiFaceDigital()
while(True):
	run(5) #Depends on your wiring. Mine was on OUTPUT_PIN-5 and the 5V-OUTPUT_PIN-9

