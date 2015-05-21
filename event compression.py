#This program takes the results of the event identifier program and groups similar events found by multiple stations into one event.
import pandas as pd
from datetime import datetime,timedelta
q = 'C:\Users\Fikre\Desktop\\results_100nT\\2008-08-09.csv'
j= pd.read_csv(q)
df = pd.DataFrame(j, columns = ['IAGA','MLT','MLAT','N','E','Z','Date','Time'])
time = sorted([datetime.strptime(i,"%H:%M:%S") for i in df['Time'].tolist()])
def event_finder(time):
    event_list = []
    start = time[0]
    end = time[0] + timedelta(minutes = 30)
    a1 = 0
    for a in range(len(time)):
        start = time[a1]
        end = time[a1] + timedelta(minutes = 30)
        print "start time is: " + str(start) + " end time is: " + str(end)
        if start<=time[a]<=end:
                print(time[a])
                event_list.append(start)
        else:
            a1 = a
            event_list.append(time[a1])
    return event_list
j = sorted(list(set(event_finder(time))))