import os

def missingFileSearch():
    n = 0
    collSet = []
    driveList = []
    setList = []
    driveList.append('Z:\\\\')
    driveList.append('Q:\\\\')
    driveList.append('H:\\\\')
    driveList.append('E:\Test Search')
    for drives in driveList:
        ##print drives
        os.chdir(drives)
        ##print 'Drive being scanned:',drives
        for setFolder in os.listdir(os.getcwd()):
            if os.path.isdir(setFolder)==True and \
               len(setFolder)==3 and setFolder != 'sec':
                collSet.append(os.listdir(setFolder))
                if (('prft')+'0002.'+setFolder)in collSet[n]:
                    pass
                elif (('PRFT')+'0002.'+setFolder)in collSet[n]:
                    pass
                else:
                    setList.append(int(setFolder))
                n = n + 1
                continue
    return setList

def binarySearch():
    n = 0
    driveList = []
    driveList.append('Z:\\\\')
    driveList.append('Q:\\\\')
    driveList.append('H:\\\\')
    driveList.append('E:\Test Search')
    for drives in driveList:
        setFolder = []
        os.chdir(drives) 
        print''
        print os.getcwd()
        for line in os.listdir(drives):
            if len(line)==3 and line != 'sec':
                setFolder.append(int(line)) 
        setFolder.sort()
        for value in missingFileSearch():
            [value].sort()
            first = 0 
            last = len(line)-1 
            found = False 
            while first<=last and not found: 
                midpoint = (first + last)//2 
                if setFolder[midpoint] == value: 
                    found = True
                else:
                    if value < setFolder[midpoint]: 
                        last = midpoint-1 
                    else: 
                        first = midpoint+1
            if found == True:
                print value,found,drives
        print setFolder
        n = n + 1
        continue
binarySearch()
