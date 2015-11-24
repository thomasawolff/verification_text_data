
import glob
import csv
import os

def data_parser():
    os.chdir('C:\Users\U2970\Desktop\Rut and Ride Data2')
    for file in glob.glob('*.TXT'):
        for row in csv.DictReader(open(file,'rb')):
            try:
                beg = float(row['Beginning'])
            except ValueError:
                beg = int(row['Beginning'])
            corridor = str(row['Corridor'])
            try:
                end = float(row['Ending'])
            except ValueError:
                end = int(row['Ending'])
            ll1Date = str(row['LL1_Date'])
            try:
                ll1Ride = int(row['LL1_Ride'])
            except ValueError:
                ll1Ride = str(row['LL1_Ride'])
            try:
                ll1Rut = float(row['LL1_Rut'])
            except:
                ll1Rut = str(row['LL1_Rut'])
            rl1Date = str(row['RL1_Date'])
            try:
                rl1Ride = int(row['RL1_Ride'])
            except ValueError:
                rl1Ride = str(row['RL1_Ride'])
            try:
                rl1Rut = float(row['RL1_Rut'])
            except ValueError:
                rl1Rut = str(row['RL1_Rut'])
            year = int(row['Year'])
            yield beg,corridor,end,ll1Date,ll1Ride,\
                  ll1Rut,rl1Ride,rl1Rut,year

os.chdir('C:\Users\U2970\Desktop')
#outfile = csv.writer(open('project_outfile_christian_new.csv','wb'))
generator_1 = data_parser()
for row in generator_1:
    #outfile.writerow(row)
#print'creation is done of the .CSV'
    print row

