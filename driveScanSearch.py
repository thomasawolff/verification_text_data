import os

def missingFileSearch():
    n = 0
    collSet = []
    driveList = []
    southVan = 'Z:\\\\'
    northVan = 'Q:\\\\'
    external = 'H:\\\\'
    testData = 'E:\Test Search'
    driveList.append(southVan)
    driveList.append(northVan)
    driveList.append(testData)
    driveList.append(external)
    for drives in driveList:
        os.chdir(drives)
        print 'Drive being scanned: ',drives
        for setFolder in os.listdir(os.getcwd()):
            if os.path.isdir(setFolder)==True\
            and len(setFolder)==3\
            and setFolder != 'sec':
                 collSet.append(os.listdir(setFolder))
                 if (('prft')+'0002.'+setFolder)in collSet[n]:
                     pass
                 elif (('PRFT')+'0002.'+setFolder)in collSet[n]:
                     pass
                 else:
                     print'Missing files:','Set',setFolder
                 n = n + 1
                 continue
            else:continue
missingFileSearch()
