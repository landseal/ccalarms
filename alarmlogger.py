"""
Simple logging script to log clipper creek alarms
Uses GPIO pin 3 configured with a pull up resistor to measure relay output
Logs to a csv file every 10 seconds
Also sends an email when it sees a fault
"""

import csv
from datetime import datetime
import time
import os
import RPi.GPIO as GPIO
import smtplib
from email.mime.text import MIMEText

start = datetime.now()
print(start)
#filepath = '/media/pi/BC67-8823/CClogger/'
filepath = ''
filename = str(start)[:19].replace(':','')+'_alarmlog.csv'
print(filename)

pin = 4
# set GPIO mode to BCM numbering (GPIO4 is pin 7 on header)
GPIO.setmode(GPIO.BCM)
# set pin to input with internal pull up
GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# add GPIO event detect on pin
# GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime=5000)

with open(os.path.join(filepath, filename), 'wb') as csvfile:
    alarmwriter = csv.writer(csvfile)

    # write header
    alarmwriter.writerow(['Time', 'State'])
    # write data
    while True:
        # get state of relay
        time = datetime.now()
        state = GPIO.input(pin)
    	data = [time, state]
    	alarmwriter.writerow(data)

        # send email if alarm is detected
        if state == 0:
            # set up email stuff
            msg = MIMEText('uhoh')
            me = 'joshua.sealand@motivps.com'
            you = 'joshua.sealand@motivps.com'
            msg['From'] = me
            msg['To'] = me
            msg['Subject'] = str(time)
            s = smtplib.SMTP('localhost')
            s.sendmail(me, [you], msg.as_string())
            s.quit()

        # wait 10 seconds
    	time.sleep(10)
        
        # # if an event is detected, add the state of the pin
        # if GPIO.event_detected(pin):
	    # print('event detected')
        #     data = [datetime.now(), GPIO.input(pin)]
        #     alarmwriter.writerow(data)
