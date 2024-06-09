from utils.GeoDataFrame import getDataFrame
from utils.Geo import getOsmData
from utils.Files import saveToJsonFile
from utils.Mongo import saveMany
from config.Sensitive import MONGO_URI
from time import sleep

allCoordinate = getDataFrame('allCoordinate.tsv', 'data')


dataSize = len(allCoordinate.values)
data = []
step = 0
minWait = 0.15
minWaitWeight = 0.05
stepsFailedRequest = 1
numberOfMissingData = 0
wait = minWait
stepThreshold = 1000
maxTry = 100
numberOfSavedData = 0

for coordinate in allCoordinate.values:
    for tryCount in range(maxTry):
        print(
            f'[{stepThreshold*numberOfSavedData+step+1}/{dataSize}] : {tryCount+1}/{maxTry} trying to get data from {coordinate[0]}, {coordinate[1]}')
        osmData = getOsmData(coordinate[0], coordinate[1])
        if osmData:
            wait = minWait
            break
        else:
            wait += minWaitWeight * stepsFailedRequest
            stepsFailedRequest += 1
            print('retrying in', wait, 'seconds')
            sleep(wait)

    temp = {
        'Latitude': coordinate[0],
        'Longitude': coordinate[1],
        'GeoJSON': osmData
    }
    data.append(temp)
    step += 1

    if step == stepThreshold:
        saveToJsonFile(data, 'data/osm/temp')
        numberOfSavedData += 1
        print('number of success request:', step*numberOfSavedData)
        print('saving to mongo...')
        try:
            saveMany(MONGO_URI, 'OSM', 'GeoData', data)
            print('saved to mongo')
        except Exception as e:
            print('error saving to mongo: ', e.message)

        if stepsFailedRequest > maxTry:
            print('too many failed request, exiting...')
            numberOfMissingData += 1

        if numberOfMissingData > 10:
            print('too many missing data, exiting...')
            minWait += minWaitWeight

        if stepsFailedRequest == 1:
            minWait -= minWaitWeight
            if minWait <= 0:
                minWait = minWaitWeight

        # print statistics
        print('number of success request:', step*numberOfSavedData)
        print('number of missing data:', numberOfMissingData)
        print('number of failed request:', stepsFailedRequest)
        print('number of total request:', dataSize)
        print('minWait:', minWait)
        print('wait:', wait)
        print('step:', step)
        print('numberOfSavedData:', numberOfSavedData)
        print('numberOfMissingData:', numberOfMissingData)
        print('stepsFailedRequest:', stepsFailedRequest)

        step = 0
        data = []
        wait = minWait
        stepsFailedRequest = 1
