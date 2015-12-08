import os
import csv
import glob as g
import pprint as p
import matplotlib.pyplot as plt

os.chdir('C:\Users\U2970\Desktop\calibrationFiles')

def dataIn():
    for file in g.glob('*.TXT'):
        for col in csv.DictReader(open(file,'rU')):
            yield col

def graphWriterIRIandRut():
    startList = []
    endList = []
    iriRList = []
    iriLList = []
    rutRList = []
    rutLList = []
    for col in dataIn()
        set_ = int(col[' Set'])
        startList.append(float(col['Start-Mi']))
        endList.append(float(col['  End-Mi']))
        iriRList.append(float(col[' IRI R e']))
        iriLList.append(float(col['IRI LWP ']))
        rutRList.append(float(col[' RUT R e']))
        rutLList.append(float(col[' RUT L e']))
            
    plt.subplot(2, 1, 1)
    plt.grid(True)
    colors = np.random.rand(n)
    plt.ylabel('IRI value',fontsize=12)
    plt.title('IRI data per mile for 2015 calibrations')
    plt.scatter([startList,endList],[iriRList,iriLList],c=colors)
    plt.tick_params(axis='both', which='major', labelsize=8)

    plt.subplot(2, 1, 2)
    plt.grid(True)
    colors = np.random.rand(n)
    plt.xlabel('Mile marker of 5 mile calibration stretch',fontsize=12)
    plt.ylabel('Rut value',fontsize=12)
    plt.title('Rut data per mile for 2015 calibrations')
    plt.scatter([startList,endList],[rutRList,rutLList],c=colors)
    plt.tick_params(axis='both', which='major', labelsize=8)
    
    plt.gcf()
    plt.show()
    plt.gcf().clear()
    plt.close('all')
graphWriterIRIandRut()
