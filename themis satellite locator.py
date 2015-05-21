# This program downloads all the cdf themis satellite location files corresponding to the event times
import os
import numpy as np
import pandas as pd
import urllib
from datetime import datetime,timedelta
q = 'C:\Users\Fikre\Desktop\\results_100nT\\'
m = os.listdir(q)
date = []
time = []
r = []
for i in m:
    j= pd.read_csv(q + i)
    df = pd.DataFrame(j, columns = ['number','IAGA','MLT','MLAT','N','E','Z','Date','Time'])
    for a in df['Date']:
        date.append(a)
    for b in df['Time']:
        time.append(b)
Satellite = urllib.URLopener()
for c in range(len(date)):
    day_of_year = datetime.strptime(date[c],"%Y-%m-%d").timetuple().tm_yday
    if (1<=datetime.strptime(time[c],"%H:%M:%S").hour<=23):
        hour_before = datetime.strftime(datetime.strptime(time[c],"%H:%M:%S")-timedelta(hours = 1),"%H:%M:%S")
        hour_after = datetime.strftime(datetime.strptime(time[c],"%H:%M:%S")+timedelta(hours = 1),"%H:%M:%S")
    if (datetime.strptime(time[c],"%H:%M:%S").hour == 0):
        hour_before ="00:00:00"
        hour_after = datetime.strftime(datetime.strptime(time[c],"%H:%M:%S")+timedelta(hours = 1),"%H:%M:%S")
    time_acceptable_format = time[c].replace(":",";")
    Satellite.retrieve("http://sscweb.gsfc.nasa.gov/cgi-bin/Locator.cgi?SPCR=themisa&SPCR=themisb&SPCR=themisc&SPCR=themisd&SPCR=themise&START_TIME=2008%20"+str(day_of_year)+"%20"+hour_before+"&STOP_TIME=2008%20"+str(day_of_year)+"%20"+hour_after+"&REG_OPT=7&GSM=7&SUBMIT=Submit%20query%20and%20wait%20for%20output","C:\Users\Fikre\Desktop\\themis satellite locations\\"+str(date[c])+" "+time_acceptable_format+".doc")
