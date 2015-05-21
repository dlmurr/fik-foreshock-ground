#This program takes all themis satellite location cdf files and creates a dataframe table of them
import os
import pandas as pd
q = 'C:\Users\Fikre\Desktop\\themis satellite locations\\'
m = os.listdir(q)
date = []
loca = []
filename = []
for d in m:
    r = []
    f = open(q+d, "r")
    for line in f:
        r.append(line)
    for e in r:
        if e[0:4] == '2008':
            date.append(e[0:22])
            loca.append(e[56:65])
            filename.append(d)
jk = pd.DataFrame(date,columns = ['Year'])
foo = lambda x: pd.Series([i for i in (x.split(' '))])
rev = jk['Year'].apply(foo)
jk['Year'] = rev[0]
jk['Day of Year'] = rev[1]
jk['Time'] = rev[2]
jk['Satellite'] = rev[3]
jk['Location'] = loca
jk['FileName'] = filename
jk_new2 = []
begin = 0
end = 0
loc_index = []
try:
    while end != len(jk):
        print "jk is length: " + str(len(jk)) + " end is: " + str(end)
        for a in jk['Satellite'].drop_duplicates():
            begin = end
            while jk['Satellite'][end] == a:
                end = end+1
            print "starting at: " + str(begin)+ " ending at: " + str(end)
            jk_new = jk[begin:end]
            loc_name = []
            for b in range(len(jk_new['Location'])):
                if jk_new['Location'][b+begin] not in loc_name:
                    loc_name.append(jk_new['Location'][b+begin])
                    loc_index.append(b+begin)
                    jk_new2.append(jk.iloc[[b+begin]])
except KeyError:
    for a in range(len(jk_new2) - 1):
        jk_new2[0] = jk_new2[0].append(jk_new2[a+1],ignore_index = True)
jk_new2[0]