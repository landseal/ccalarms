import os
import time 
from time import sleep
from datetime import datetime

file = open("data_log.csv", "a")
i=0
file.write("Time,Sensor1,Sensor2,Sensor3,Sensor4,Sensor5\n")
while i < 100:
        i=i+1
        now = datetime.now()
        file.write(str(now)+","+str(i)+","+str(-i)+","+str(i-10)+","+str(i+5)+","+str(i*i)+"\n")
        file.flush()
        time.sleep(5)<br>file.close()
