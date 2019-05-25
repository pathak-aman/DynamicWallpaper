import time
import datetime

SECONDSINDAY = 24*3600
currentDT = datetime.datetime.now()
seconds = currentDT.second
minutes = currentDT.minute
hour = currentDT.hour

tot_seconds = hour*3600 + minutes*60 +seconds
while True:
    time.sleep(1)
    tot_seconds+=1
    print(SECONDSINDAY-tot_seconds)
