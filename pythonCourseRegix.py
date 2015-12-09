import os
import re
 
info = []
infoNum = []

os.chdir('C:\Users\U2970\Documents')

for line in open('regex_sum_43.txt','rb'):
    for line in re.findall('[0-9]*',line):
            info.append(line)            
for line in filter(None,info):
    infoNum.append(int(line))
print sum(infoNum)

