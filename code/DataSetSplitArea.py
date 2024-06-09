from utils.GeoDataFrame import getBoundingBoxFilteredDataFrame, getCleanedCSVFile, saveDataFrameToTSV
from utils.Geo import getLocationType

country = {
    'Germany': {'minLatitude': 47.27, 'maxLatitude': 55.06, 'minLongitude': 5.87, 'maxLongitude': 15.04},
    'Italy': {'minLatitude': 36.65, 'maxLatitude': 47.09, 'minLongitude': 6.62, 'maxLongitude': 18.79},
    'USA':  {'minLatitude': 31.458778, 'maxLatitude': 48.047273, 'minLongitude': -125.366156, 'maxLongitude': -61.422812},
    'China': {'minLatitude': 18.15, 'maxLatitude': 53.55, 'minLongitude': 73.66, 'maxLongitude': 135.05}
}

dataFrame = getCleanedCSVFile('clean_data.tsv', 'data/gowalla')


# germanyDataFrame = getBoundingBoxFilteredDataFrame(
#     dataFrame, country['Germany'])
# print('Germany: ', len(germanyDataFrame))
# germanyDataFrame['LocationType'] = germanyDataFrame.apply(
#     lambda row: getLocationType(row['Latitude'], row['Longitude']), axis=1)
# saveDataFrameToTSV(germanyDataFrame, 'germany.tsv')

# italyDataFrame = getBoundingBoxFilteredDataFrame(dataFrame, country['Italy'])
# print('Italy: ', len(italyDataFrame))
# italyDataFrame['LocationType'] = italyDataFrame.apply(
#     lambda row: getLocationType(row['Latitude'], row['Longitude']), axis=1)
# print("saving italy ...")
# saveDataFrameToTSV(italyDataFrame, 'italy.tsv')

usaDataFrame = getBoundingBoxFilteredDataFrame(dataFrame, country['USA'])
print('USA: ', len(usaDataFrame))
usaDataFrame['LocationType'] = usaDataFrame.apply(
    lambda row: getLocationType(row['Latitude'], row['Longitude']), axis=1)
print("saving usa ...")
saveDataFrameToTSV(usaDataFrame, 'usa.tsv')


# chinaDataFrame = getBoundingBoxFilteredDataFrame(dataFrame, country['China'])
# print('China: ', len(chinaDataFrame))
# chinaDataFrame['LocationType'] = chinaDataFrame.apply(
#     lambda row: getLocationType(row['Latitude'], row['Longitude']), axis=1)
# print("saving china ...")
# saveDataFrameToTSV(chinaDataFrame, 'china.tsv')
