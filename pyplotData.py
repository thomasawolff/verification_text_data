import os
import csv
import glob as g
import matplotlib.pyplot as plt

os.chdir('C:\Users\U2970\Desktop\calibrationFiles')

def graphWriterIRIandRut():
    startList = []
    endList = []
    iriRList = []
    iriLList = []
    rutRList = []
    rutLList = []
    for file in g.glob('*.TXT'):
        for col in csv.DictReader(open(file,'rU')):
            set_ = int(col[' Set'])
            startList.append(float(col['Start-Mi']))
            endList.append(float(col['  End-Mi']))
            iriRList.append(float(col[' IRI R e']))
            iriLList.append(float(col['IRI LWP ']))
            rutRList.append(float(col[' RUT R e']))
            rutLList.append(float(col[' RUT L e']))
    plt.scatter([iriRList,iriLList],[rutRList,rutLList])        
    fig1 = plt.gcf()
    plt.xlabel('Rut value',fontsize=14)
    plt.ylabel('IRI value',fontsize=14)
    plt.title('IRI vs Rut data')
    plt.grid(True)
    plt.show(fig1)
    plt.gcf().clear()
    plt.close('all')
graphWriterIRIandRut()
