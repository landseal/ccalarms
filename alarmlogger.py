"""
Simple logging script to log clipper creek alarms
Uses GPIO pin 3 configured with a pull up resistor to measure relay output
Logs to a csv file every 10 seconds
"""

import csv
from datetime import datetime
import time
import os
import RPi.GPIO as GPIO

start = datetime.now()
print(start)
filepath = '/media/pi/BC67-8823/CClogger/'
filename = str(start)[:19].replace(':','')+'_alarmlog.csv'
print(filename)

pin = 4
# set GPIO mode to BCM numbering (GPIO4 is pin 7 on header)
GPIO.setmode(GPIO.BCM)
# set pin to input with internal pull up
GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

with open(os.path.join(filepath, filename), 'wb') as csvfile:
    alarmwriter = csv.writer(csvfile)

    # write header
    alarmwriter.writerow(['Date', 'State'])
    # write data
    while True:
        data = [datetime.now(), GPIO.input(pin)]
        alarmwriter.writerow(data)
	time.sleep(1)
