
import re
import os
import glob
os.chdir('C:\Users\U2970\Desktop')
for file in glob.glob('*.TXT'):
    with open(file,'rb') as hand:
        for line in hand:
            line = line.rstrip()
            if re.search('^[0-9]\S\d*.[0-9]\d+', line):
                if 'i' in line:
                    iVar = line.replace('i','')
                    if '+' in iVar:
                        iPlus = iVar.replace('+','.')
                    else:
                        iPlus = iVar
                    print iPlus
            
    
            
            
