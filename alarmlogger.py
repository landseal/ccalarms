"""
Simple logging script to log clipper creek alarms
Uses GPIO pin 3 configured with a pull up resistor to measure relay output
Logs to a csv file every 10 seconds
"""

import csv
from datetime import datetime

start = datetime.now()
print(start)
filename = str(start)[:19]+'_alarmlog.csv'
print(filename)

with open(filename, 'wb') as csvfile:
    alarmwriter = csv.writer(csvfile)

    while True:
        data = [datetime.now(), 'hi']
        alarmwriter.writerow(data)
