from spacepy import pycdf
import datetime
import matplotlib.dates as mdates
from matplotlib import pylab as plt
cdf = pycdf.CDF('C:\Users\Fikre\Desktop\\thc_l2_fgm_20080714_v01.cdf')
btotal = cdf['thc_fgs_btotal'][...]
bcomponent_x = cdf['thc_fgs_gsm'][...][:,0]
bcomponent_y = cdf['thc_fgs_gsm'][...][:,1]
bcomponent_z = cdf['thc_fgs_gsm'][...][:,2]
time = cdf['thc_fgs_time'][...]
time1=[datetime.datetime.utcfromtimestamp(i) for i in time]
hour = map(lambda v : v.hour,time1)
minute = map(lambda v : v.minute,time1)
start = hour.index(21) + minute[hour.index(21):].index(40)
end = hour.index(21) + minute[hour.index(21):].index(48)
myFmt = mdates.DateFormatter('%H:%M:%S')
plt.figure(1)
ax = plt.subplot(1,1,1)
ax.xaxis.set_major_formatter(myFmt)
plt.plot(time1[start:end],btotal[start:end])
plt.title('B total')
plt.show()
plt.figure(2)
ax = plt.subplot(3,1,1)
ax.xaxis.set_major_formatter(myFmt)
plt.plot(time1[start:end],bcomponent_x[start:end])
plt.title('Bx component')
ax = plt.subplot(3,1,2)
ax.xaxis.set_major_formatter(myFmt)
plt.plot(time1[start:end],bcomponent_y[start:end])
plt.title('By component')
ax = plt.subplot(3,1,3)
ax.xaxis.set_major_formatter(myFmt)
plt.plot(time1[start:end],bcomponent_z[start:end])
plt.title('Bz component')
plt.show()
cdf2 = pycdf.CDF('C:\Users\Fikre\Desktop\\thc_l2_mom_20080714_v01.cdf')
electron_density = cdf2['thc_peem_density'][...]
velocity_x = cdf2['thc_peim_velocity_gse'][...][:,0]
velocity_y = cdf2['thc_peim_velocity_gse'][...][:,1]
velocity_z = cdf2['thc_peim_velocity_gse'][...][:,2]
time2=[datetime.datetime.utcfromtimestamp(i) for i in cdf2['thc_pxxm_time'][...]]
hour = map(lambda v : v.hour,time2)
minute = map(lambda v : v.minute,time2)
start = hour.index(21) + minute[hour.index(21):].index(40)
end = hour.index(21) + minute[hour.index(21):].index(48)
plt.figure(3)
ax = plt.subplot(1,1,1)
ax.xaxis.set_major_formatter(myFmt)
plt.plot(time2[start:end],electron_density[start:end])
plt.title('Electron Density')
plt.show()
plt.figure(4)
ax = plt.subplot(3,1,1)
ax.xaxis.set_major_formatter(myFmt)
plt.plot(time2[start:end],velocity_x[start:end])
plt.title('Velocity x')
ax = plt.subplot(3,1,2)
ax.xaxis.set_major_formatter(myFmt)
plt.plot(time2[start:end],velocity_y[start:end])
plt.title('Velocity y')
ax = plt.subplot(3,1,3)
ax.xaxis.set_major_formatter(myFmt)
plt.plot(time2[start:end],velocity_z[start:end])
plt.title('Velocity z')
plt.show()