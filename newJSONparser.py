import os
import json

os.chdir('C:\Users\U2970\Documents\ArcGIS')

def jSonYield():
    n = 0
    with open('new_corrs_shapy_FeaturesToJS.json')as datafile:
        data = json.load(datafile)
    for k, v in data['features']:
        corr =  data['features'][n]['attributes']['CORRIDOR_C']
        trf =  data['features'][n]['attributes']['TRFPOST']
        frf =  data['features'][n]['attributes']['FRFPOST']
        coords = data['features'][n]['geometry']['paths']
        for line in coords:
            latMin = coords[0][0][0]
            longMin = coords[0][0][1]
            latMax = coords[0][-1][0]
            longMax = coords[0][-1][1]
        n = n + 1
        yield corr,frf,trf,latMin,longMin,latMax,longMax

for line in jSonYield():
    print line
