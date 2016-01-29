import os
import re
import gc
import csv
import time
import glob as g

os.chdir('C:\Users\U2970\Desktop\SEC_FILE_EXPORTS')
#os.chdir('X:\PavementAnalysis\Pavemgmt\\\\DATA_COLLECTION\\\\AUTOMATED_VANS\\\\07_GIS_LAYERS\\\\2015_NORTH_VAN_EXPORTS\\\\SEC_FILE_EXPORTS')

def dataOut():
    for file in g.glob('*.SEC'):
        for line in open(file):
            yield line
  
def headerBody():
    data = []
    for line in dataOut():
        gc.disable()
        data.append(line.split('!'))
        gc.enable()
    for col in data:
        corrRB = col[4] + col[32]
        begMi = round(float(col[12]),3)
        endMi = round(float(col[13]),3)
        length = round(float(col[40]),3)
        dir_ = col[16]
        lane = int(col[31])
        set_ = int(col[41])
        month = int(col[47])
        day = int(col[48])
        yield corrRB,begMi,endMi,length,dir_,lane,set_,month,day
        
def printerOut():
    outfile = csv.writer(open('program_NORTH_data.csv','wb'))
    n = 0
    columns = ('corridorRB','begMi','endMi','length',\
                   'dir_','lane','set_','month','day')
    outfile.writerows([columns])
    for line in headerBody():
        n = n + 1
        colNew = ','.join(columns)
        outfile.writerows([line])
        print'Row created',n,time.clock()
printerOut()

def corrSearch():
    n = 0
    data = []
    for line in dataOut():
        gc.disable()
        data.append(line.split('!'))
        gc.enable()
    for col in data:
        while n < 61:
            try:
                n = n + 1
                if '.' in col[n]:
                    yield round(float(col[n]),6),n
                else:
                    yield int(col[n]),n
            except:
                if re.search('^C\S\d.[0-9]*\d+',col[n]):
                    yield col[n],n,'Corridor'
                if (('I' in col[n] or 'D' in col[n]) and\
                    len(col[n]) == 1): 
                    yield col[n],n,'Direction'
                if ('E' in col[n] or 'N' in col[n] or\
                    'W' in col[n] or 'S' in col[n])\
                    and len(col[n]) == 1: 
                    yield col[n],n,'Cardinal'
                break
                
for line in corrSearch():
    print line



 
