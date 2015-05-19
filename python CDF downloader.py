import urllib
import numpy as np
from spacepy import pycdf
cdf_file = urllib.URLopener()
month = np.arange(1,13) 
day = np.arange(1,32)
for i in month:
    for j in day:
        try:
            cdf_file.retrieve('http://cdaweb.sci.gsfc.nasa.gov/sp_phys/data/themis/thc/l2/fgm/2008/thc_l2_fgm_2008'+"%02d" % i+"%02d" % j+'_v01.cdf','C:\Users\Fikre\Desktop\\cdf_folder2\\'+"%02d" % i+"%02d" % j+'.cdf')
            print i,j
        except(IOError):
            print "day doesn't exist"