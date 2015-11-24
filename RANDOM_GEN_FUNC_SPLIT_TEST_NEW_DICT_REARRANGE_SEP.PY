import os
import csv
import math
import sys
import random as r

def readerIn():
    os.chdir\
    ('S:\PAVE_MANAGEMENT\AUTOMATED_DISTRESS_SURVEYS\\\\02_COLLECTION_VEHICLES\\\\07_GIS_LAYERS\\\\2015_NORTH_VAN_EXPORTS\\\\USEFULL_2015_SPREADSHEETS')
    
    
def readerOut():
    os.chdir('S:\PAVE_MANAGEMENT\AUTOMATED_DISTRESS_SURVEYS\\\\02_COLLECTION_VEHICLES\\\\07_GIS_LAYERS')


class nCounter(object):
    
    def __init__(self):
        self.length = 10
        self.rounder = 3

    def yielderOut(self):
        n = 0
        readerIn()
        corr = raw_input('Enter the corridor you want: ').upper()
        for col in csv.DictReader(open('2015_FILES_COMBINED.CSV')):
            corridorRB = str(col['CORRIDOR_CODE_RB'])
            corridor = str(col['CORRIDOR_CODE'])
            begMi = float(col['BEGIN_MI'])
            begHi = float(col['BEGIN_MI'])
            begLi = float(col['BEGIN_MI'])
            endMi = float(col['END_MI'])
            lane = int(col['LANE'])
            dir_ = str(col['DIR'])
            group = corridor,begMi,endMi,lane,dir_
            n = n + 1
            try:
                if corridor == corr and dir_ == 'I':
                    if abs(endMi - begMi) < self.length:
                        varsL = round(r.uniform(math.ceil(begMi),\
                            (math.floor(endMi))),self.rounder)
                        if (varsL > begMi and varsL < endMi):
                            yield group,varsL
                        else:continue                
                    if abs(endMi - begMi) <= (2*self.length)\
                         and abs(endMi - begMi) > self.length:
                        varsM = round(r.uniform(math.ceil(begMi),\
                            (math.floor(begMi+self.length))),self.rounder)
                        yield group,varsM                    
                    elif abs(endMi - begMi) > (2*self.length):
                        for i in range(0,n):
                            begHi = math.floor(begHi)+(self.length)
                            varsN = round(r.uniform(math.ceil(begHi),\
                                (math.floor(begHi+self.length))),self.rounder)
                            if varsN < endMi and varsN > begMi:
                                yield group,varsN
                            else:continue
                    else:continue
                if corridor == corr and dir_ == 'D':
                    if abs(endMi - begMi) < self.length:
                        varsL = round(r.uniform(math.ceil(begMi),\
                            (math.floor(endMi))),self.rounder)
                        if (varsL < begMi and varsL > endMi):
                            yield group,varsL
                        else:continue
                    elif abs(endMi - begMi) <= (2*self.length)\
                         and abs(endMi - begMi) > self.length:
                        varsO = round(r.uniform(math.ceil(begMi),\
                            (math.floor(begMi-self.length))),self.rounder)
                        yield group,varsO
                    elif abs(endMi - begMi) > (2*self.length):
                        for i in range(0,n):
                            begLi = math.floor(begLi)-(self.length)
                            varsP = round(r.uniform(math.ceil(begLi),\
                                (math.floor(begLi-self.length))),self.rounder)
                            if varsP > endMi and varsP < begMi:
                                yield group,varsP
                            else:continue
                    else:continue
            except:break
     
def nCounterGo():
    readerOut()
    #outfile = csv.writer(open('random_gen_writer.csv','wb'))
    for i in range(0,1):
        out = nCounter()
        for line in out.yielderOut():
            print line
            #outfile.writerow(line)
    print'Have a nice day!'
nCounterGo()



##  round(r.uniform(begMi,begMi-self.length),self.rounder)

##                        begLi = math.floor(begLi)-self.length
##                        varsP = round(r.uniform(math.ceil(begLi),\
##                            (math.floor(begLi-self.length))),self.rounder)

##                    elif endMi < begMi:
##                        if begMi - endMi < self.length:
##                            varsQ = round(r.uniform(math.ceil(begMi),\
##                                (math.floor(endMi))),self.rounder)
##                            if varsQ > endMi:
##                                yield group,varsQ
##                            else: continue
##                        else:
##                            varsO = round(r.uniform(math.ceil(begMi),\
##                                (math.floor(begMi-self.length))),self.rounder)
##                            if varsO > (begMi-self.length):
##                                yield group,varsO
##                            else: continue
##                        for i in range(0,n):
##                            begLi = math.floor(begLi)-self.length
##                            varsP = round(r.uniform(math.ceil(begLi),\
##                                (math.floor(begLi-self.length))),self.rounder)
##                            if varsP > endMi:
##                                yield group,varsP
##                            else: continue
##    begLi = math.floor(begLi)-self.length
##    varsP = round(r.uniform(math.ceil(begLi),\
##    (math.floor(begLi-self.length))),self.rounder)
##    yield group,varsP

#if corridor == 'C000001':
#if (self.length+begMi) > endMi:
##            self.countList.append(corridor)
##        valList = Counter([val for val in self.countList])
##        for valList in valList.values():
##            if 2 not in [valList]:
##                self.corrList.append(valList)
##        #yield set(Counter(self.countList).values()).union(self.corrList)
##        for element in self.countList:
##            for element in self.corrList:
##                newList.append(element)
##        yield newList
            
##            if int(corridor[1:7]) <= 574:
##                if (begMi < endMi) and (endMi - begMi) <= self.length:
##                       vars1 = round(r.uniform(begMi,endMi),self.rounder)
##                       yield corridorRB,round(begMi,self.rounder),\
##                          round(endMi,self.rounder),lane,\
##                          'Increasing 1',
                       
##                if (self.length+begMi) < endMi:
##                    vars1 = round(r.uniform((math.ceil(begMi)+1),\
##                    (math.floor(begMi)+(self.length))),self.rounder)
##                    yield corridorRB,round(begMi,self.rounder),\
##                          round(endMi,self.rounder),lane,\
##                          'Increasing 1',vars1
##
##                if ((self.multi[0]*self.length)+begMi) < endMi:
##                    vars2 = round(r.uniform((math.ceil(begMi)+self.length),\
##                            (math.floor(begMi)+(self.length*self.multi[0]))),self.rounder)
##                    yield corridorRB,round(begMi,self.rounder),\
##                              round(endMi,self.rounder),lane,\
##                              'Increasing 2',vars2
##                   
##                if ((self.multi[1]*self.length)+begMi) < endMi:
##                    vars3 = round(r.uniform((math.ceil(begMi)+self.length*self.multi[0]),\
##                            (math.floor(begMi)+(self.length*self.multi[1]))),self.rounder)
##                    yield corridorRB,round(begMi,self.rounder),\
##                              round(endMi,self.rounder),lane,\
##                              'Increasing 3',vars3
##                   
##                if ((self.multi[2]*self.length)+begMi) < endMi:
##                    vars4 = round(r.uniform((math.ceil(begMi)+(self.length*self.multi[1])),\
##                            (math.floor(begMi)+(self.length*self.multi[2]))),self.rounder)
##                    yield corridorRB,round(begMi,self.rounder),\
##                              round(endMi,self.rounder),lane,\
##                              'Increasing 4',vars4
##                                     
##                if  ((self.multi[3]*self.length)+begMi) < endMi:
##                    vars5 = round(r.uniform((math.ceil(begMi)+(self.length*self.multi[2])),\
##                            (math.floor(begMi)+(self.length*self.multi[3]))),self.rounder)
##                    yield corridorRB,round(begMi,self.rounder),\
##                              round(endMi,self.rounder),lane,\
##                              'Increasing 5',vars5
##
##                if ((self.multi[4]*self.length)+begMi) < endMi:
##                    vars6 = round(r.uniform((math.ceil(begMi)+(self.length*self.multi[3])),\
##                            (math.floor(endMi)-1)),self.rounder)
##                    yield corridorRB,round(begMi,self.rounder),\
##                          round(endMi,self.rounder),lane,\
##                          'Increasing 6',vars6
##
##                if (endMi < begMi) and (begMi - endMi) <= self.length:
##                        vars7 = round(r.uniform(begMi,endMi),self.rounder)
##                        yield corridorRB,round(begMi,self.rounder),\
##                              round(endMi,self.rounder),lane,\
##                              'Decreasing 1',vars7
##
##                if (begMi - self.length) > endMi:
##                    vars7 = round(r.uniform(math.floor(begMi),\
##                        (math.ceil(begMi)-(self.length)-1)),self.rounder)
##                    yield corridorRB,round(begMi,self.rounder),\
##                          round(endMi,self.rounder),lane,\
##                          'Decreasing 1',vars7
##
##                if (begMi - (self.multi[0]*self.length)) > endMi:
##                    vars8 = round(r.uniform((math.floor(begMi)-self.length),\
##                        (math.ceil(begMi)-(self.multi[0]*self.length))),self.rounder)
##                    yield corridorRB,round(begMi,self.rounder),\
##                              round(endMi,self.rounder),lane,\
##                              'Decreasing 2',vars8
##
##                if (begMi - (self.multi[1]*self.length)) > endMi:
##                    vars9 = round(r.uniform((math.floor(begMi)-(self.multi[0]*self.length)),\
##                        (math.ceil(begMi)-(self.multi[1]*self.length))),self.rounder)
##                    yield corridorRB,round(begMi,self.rounder),\
##                              round(endMi,self.rounder),lane,\
##                              'Decreasing 3',vars9
##
##                if (begMi - (self.multi[2]*self.length)) > endMi:
##                    vars10 = round(r.uniform((math.floor(begMi)-(self.multi[1]*self.length)),\
##                        (math.ceil(begMi)-(self.multi[2]*self.length))),self.rounder)
##                    yield corridorRB,round(begMi,self.rounder),\
##                              round(endMi,self.rounder),lane,\
##                              'Decreasing 4',vars10
##
##                if (begMi - (self.multi[3]*self.length)) > endMi:
##                    vars11 = round(r.uniform((math.floor(begMi)-(self.multi[2]*self.length)),\
##                        (math.ceil(begMi)-(self.multi[3]*self.length))),self.rounder)
##                    yield corridorRB,round(begMi,self.rounder),lane,\
##                              round(endMi,self.rounder),\
##                              'Decreasing 5',vars11
##
##                if (begMi - (self.multi[4]*self.length)) > endMi:
##                    vars12 = round(r.uniform((math.floor(begMi)-(self.multi[3]*self.length)),\
##                        (math.ceil(endMi)+1)),self.rounder)
##                    yield corridorRB,round(begMi,self.rounder),\
##                          round(endMi,self.rounder),lane,\
##                          'Decreasing 6',vars12
##    
##def nCounterGo():
##    readerOut()
##    #outfile = csv.writer(open('random_gen_writer.csv','wb'))   
##    out = nCounter()
##    for line in out.yielderOut():
##        print line
##        #outfile.writerow(line)
##nCounterGo()
            
        

