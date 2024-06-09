def getDataFrameFromSSV(ssvFileName, rootDirectory='data'):
    from pandas import read_csv as readCSV, DataFrame as newDataFrame
    dataFrame = readCSV(f'{rootDirectory}/{ssvFileName}', sep='\s+')
    if dataFrame is None:
        raise Exception('dataFrame is None')
    return dataFrame
def getDataFrameFromTSV(ssvFileName, rootDirectory='data'):
    from pandas import read_csv as readCSV
    dataFrame = readCSV(f'{rootDirectory}/{ssvFileName}', sep='\t')
    if dataFrame is None:
        raise Exception('dataFrame is None')
    return dataFrame

def getDataFrameFromFeather(featherFileName, rootDirectory='data'):
    from pandas import read_feather as readFeather
    dataFrame = readFeather(f'{rootDirectory}/{featherFileName}')
    if dataFrame is None:
        raise Exception('dataFrame is None')
    return dataFrame

def getFilteredDataFrame(dataFrame, minimumNeedleRecords):
    agentRecords = getAgentsRecords(dataFrame)
    eligibleAgents = agentRecords[agentRecords > minimumNeedleRecords]
    dataFrame = dataFrame.loc[dataFrame['AgentID'].isin(eligibleAgents.index)]
    return dataFrame


def getAgentsRecords(dataFrame):
    return dataFrame['AgentID'].value_counts()

def getTrainDataFrame(dataFrame, trainPercentage):
    from pandas import DataFrame as newDataFrame, concat
    trainDataFrame = newDataFrame()
    agentsStat = dataFrame['AgentID'].value_counts()
    agentIds = agentsStat.index

    for agentId in agentIds:
        agentData = dataFrame.loc[dataFrame['AgentID'] == agentId]
        agentDataSize = agentData.shape[0]
        agentTrainSize = int(agentDataSize * trainPercentage)
        agentTrainData = agentData[0:agentTrainSize]
        trainDataFrame = concat([trainDataFrame, agentTrainData])

    return trainDataFrame


def getTestDataFrame(dataFrame, trainDataFrame):
    return dataFrame.loc[~dataFrame.index.isin(trainDataFrame.index)]


def addNeedle(dataFrame, swapAgents):
    (agentIdsToBeReplaced, needleIds) = swapAgents
    for counter in range(len(agentIdsToBeReplaced)-1, -1, -1):
        agentId = agentIdsToBeReplaced[counter]
        needleId = needleIds[counter]
        dataFrame.loc[dataFrame['AgentID'] ==
                      agentId, 'AgentID'] = needleId
    return dataFrame

def getGeolifeDataFrame(file_name='clean_data.tsv'):
    from pandas import read_csv as readCSV
    dataFrame = readCSV(f'/home/emo/research/papers/2024--LLM-Outlier/data/geolife/{file_name}', sep='\s+')
    return dataFrame

def getBrightkiteDataFrame(file_name='clean_data.tsv'):
    from pandas import read_csv as readCSV
    dataFrame = readCSV(f'/home/emo/research/papers/2024--LLM-Outlier/data/brightkite/{file_name}', sep='\s+')
    return dataFrame

def getGoWallaDataFrame(file_name='clean_data.tsv'):
    from pandas import read_csv as readCSV
    dataFrame = readCSV(f'/home/emo/research/papers/2024--LLM-Outlier/data/gowalla/{file_name}', sep='\s+')
    return dataFrame

def getDataFrameFullPath(ssvFilePath):
    from pandas import read_csv as readCSV
    dataFrame = readCSV(ssvFilePath, sep='\s+')
    return dataFrame

def findBusiestDayDate(dataFrame,timeColumn='ArrivingTime',splitter=','):
    from pandas import to_datetime as toDateTime
    tempDataFrame = dataFrame.drop(['lat','lon','user','alt', 'label'], axis=1)
    tempDataFrame = tempDataFrame.reset_index(drop=True)
    print(tempDataFrame.head())
    tempDataFrame[timeColumn] = tempDataFrame[timeColumn].astype(str).str.split(splitter).str[0]
    if (not tempDataFrame[timeColumn].str.split(splitter).str[1].any()):
        tempDataFrame[timeColumn] = tempDataFrame[timeColumn].str.split('T').str[0]
    if (not tempDataFrame[timeColumn].str.split('T').str[1].any()):
        print('WARNING: space is used as a splitter')
        tempDataFrame[timeColumn] = tempDataFrame[timeColumn].str.split(' ').str[0]
    print(tempDataFrame.head())
    tempDataFrame = tempDataFrame.groupby([timeColumn]).size().reset_index(name='counts')
    tempDataFrame = tempDataFrame.loc[tempDataFrame['counts'] == tempDataFrame['counts'].max()]
    busiestDay = tempDataFrame[timeColumn]
    return busiestDay

def getBusiestDayDataFrame(dataFrame, busiestDay, timeColumn='ArrivingTime'):
    busiestDayDataFrame = dataFrame[dataFrame[timeColumn].astype(str).str.contains(busiestDay)]
    return busiestDayDataFrame

def getCleanGeoDataFrame(ssvFileName, rootDirectory='data', limit=None):
    from pandas import read_csv as readCSV
    dataFrame = readCSV(f'{rootDirectory}/{ssvFileName}', sep='\s+', header=None,
                        names=['AgentID', 'ArrivingTime', 'Latitude', 'Longitude', 'LocationType'])

    if limit is not None:
        dataFrame = dataFrame.groupby(
            'AgentID').filter(lambda x: len(x) > limit)
    dataFrame['LocationType'] = 'TBD'
    return dataFrame


def fillLocationType(dataFrame):
    from utils.Geo import getLocationType
    dataFrame['LocationType'] = dataFrame.apply(
        lambda row: getLocationType(row['Latitude'], row['Longitude']), axis=1)
    return dataFrame

def saveDataFrameToTSV(dataFrame, outputFileName, rootDirectory='data'):
    print("inside saveDataFrameToTSV", dataFrame.head())
    dataFrame.to_csv(f'{rootDirectory}/{outputFileName}', sep=' ', index=False)
    

def getAllCoordinates(*dataFrames):
    from pandas import concat
    allCoordinates = concat(dataFrames)
    allCoordinates = allCoordinates.drop_duplicates()
    allCoordinates = allCoordinates.reset_index(drop=True)
    return allCoordinates


def getPreprocessGeolifeDataFrame(ssvFileName, rootDirectory='data'):

    geolifeOriginalDataFrame = getDataFrameFromSSV(ssvFileName, rootDirectory)
    geolifeCompatibleDataFrame = getCompatibleGeolifeDataFrame(geolifeOriginalDataFrame)
    saveRawData(geolifeCompatibleDataFrame, rootDirectory)
    return geolifeCompatibleDataFrame

def getCompatibleGeolifeDataFrame(dataFrame):
    dataFrame = dataFrame.drop(['LeavingTime'], axis=1)
    dataFrame= dataFrame[[
        'AgentID', 'ArrivingTime', 'Latitude', 'Longitude', 'LocationType']]
    return dataFrame

def saveRawData(dataFrame, rootDirectory='data'):
    from pandas import DataFrame
    DataFrame.to_csv(dataFrame,
                     f'{rootDirectory}/raw_data.tsv', sep=' ', index=False)
    DataFrame.to_csv(dataFrame.head(100),
                     f'{rootDirectory}/small_raw_data.tsv', sep=' ', index=False)

def getPreprocessedPOLTrajDataFrame(tsvFileName, rootDirectory='data'):
    dataFrame = getDataFrameFromTSV(tsvFileName, rootDirectory)

    # remove '(' and ')' from the location tuple
    dataFrame['Longitude'] =dataFrame['location'].str.split(' ').str[1].str.replace('(', '')
    dataFrame['Latitude'] =  dataFrame['location'].str.split(' ').str[2].str.replace(')', '')
    dataFrame = dataFrame.drop(['location'], axis=1)
    dataFrame.reset_index(drop=True, inplace=True)
    saveRawData(dataFrame, rootDirectory)
    print( dataFrame.head())

    return dataFrame
    


def getBoundingBoxFilteredDataFrame(dataFrame, boundingBox,):
    minLatitude = boundingBox['minLatitude']
    maxLatitude = boundingBox['maxLatitude']
    minLongitude = boundingBox['minLongitude']
    maxLongitude = boundingBox['maxLongitude']

    dataFrame = dataFrame[dataFrame['Latitude'] >= minLatitude]
    dataFrame = dataFrame[dataFrame['Latitude'] <= maxLatitude]
    dataFrame = dataFrame[dataFrame['Longitude'] >= minLongitude]
    dataFrame = dataFrame[dataFrame['Longitude'] <= maxLongitude]

    return dataFrame


def getUserIDFilteredDataFrame(dataFrame, userIDs):
    dataFrame = dataFrame[dataFrame['AgentID'].isin(userIDs)]
    return dataFrame
