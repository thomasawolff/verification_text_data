import os
from xlrd import open_workbook

os.chdir('S:\\PAVE_MANAGEMENT\\AUTOMATED_DISTRESS_SURVEYS\\02_COLLECTION_VEHICLES\\07_GIS_LAYERS\\2015_NORTH_VAN_EXPORTS\\USEFULL_2015_SPREADSHEETS')

def xlsReader():
    while True:
        enter = raw_input('Enter the name of the file: ')
        if enter.lower() == 'done':
            print'Have a nice day'
            break
        else:
            try:
                workbook = open_workbook(enter)
                sheet = workbook.sheet_by_index(0)
                data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
                yield data[1:2]
            except:
                print'Bad entry try again'
            continue

import pprint as p   
for line in xlsReader():
    p.pprint(line)
