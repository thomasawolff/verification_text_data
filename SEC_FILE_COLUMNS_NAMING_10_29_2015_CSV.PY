
import glob
import csv
import os
import pprint as p

os.chdir('C:\Users\U2970\Desktop\\\\SEC_FILE_EXPORTS')

def data_parser():
    for file in glob.glob('*ATTEMPT.CSV'):
        for row in csv.DictReader(open(file,'rU')):
            corridor = row['       SEC_FILE'].strip()
            card = row[' D'].strip()
            corrRB = corridor + card
            road = row['    Road'].strip()
            from_ = row['                     From'].strip()
            to_ = row['                       To'].strip()
            dir_ = row['     DIR'].strip()
            lane = int(row['      LN'])
            frfpost = float(row[' Frfpost'])
            trfpost = float(row[' Trfpost'])
            date = row['  SurveyDateTime']\
                   .strip().replace('/','').replace(':','')
            dateMon = int(date[0:2])
            dateDay = int(date[2:4])
            dateYear = int(date[4:8])
            dateHour = int(date[9:11])
            dateMin = int(date[11:13])
            yield corrRB,from_,to_,lane,dir_,frfpost,trfpost,\
                  dateMon,dateDay,dateYear,dateHour,dateMin

outfile = csv.writer(open('sec_corridor_join.csv','wb'))
for line in data_parser():
    print line
    outfile.writerow(line)
print 'job completed'
