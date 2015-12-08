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
    plt.ylabel('IRI value',fontsize=14)
    plt.title('IRI data shown per mile')
    ax1 = plt.scatter([startList,endList],[iriRList,iriLList])
    plt.tick_params(axis='both', which='major', labelsize=8)

    plt.subplot(2, 1, 2)
    plt.grid(True)
    plt.xlabel('Mile marker',fontsize=14)
    plt.ylabel('Rut value',fontsize=14)
    plt.title('Rut data shown per mile')
    ax2 = plt.scatter([startList,endList],[rutRList,rutLList])
    plt.tick_params(axis='both', which='major', labelsize=8)

    plt.gcf()
    plt.show()
    plt.gcf().clear()
    plt.close('all')
graphWriterIRIandRut()
