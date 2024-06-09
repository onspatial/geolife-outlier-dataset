from utils.GeoDataFrame import getCleanGeoDataFrame, saveDataFrameToTSV, getAllCoordinates, preprocessGeolifeData

inputFileName = 'small_raw_data.tsv'
outputFileName = 'small_clean_data.tsv'

# preprocessGeolifeData('original_data.tsv', 'data/geolife')

gowallaCleanedDataFrame = getCleanGeoDataFrame(
    inputFileName, 'data/gowalla', limit=0)
print('gowalla cleaned dataFrame head: ', gowallaCleanedDataFrame.head())
brightkiteCleanedDataFrame = getCleanGeoDataFrame(
    inputFileName, 'data/brightkite', limit=0)
print('brightkite cleaned dataFrame head: ', brightkiteCleanedDataFrame.head())
geolifeCleanedDataFrame = getCleanGeoDataFrame(
inputFileName, 'data/geolife', limit=0)
print('geolife cleaned dataFrame head: ', geolifeCleanedDataFrame.head())

gowallaCoordinate = gowallaCleanedDataFrame[['Latitude', 'Longitude']]
print('gowalla coordinate head: ', gowallaCoordinate.head())
brightkiteCoordinate = brightkiteCleanedDataFrame[['Latitude', 'Longitude']]
print('brightkite coordinate head: ', brightkiteCoordinate.head())
geolifeCoordinate = geolifeCleanedDataFrame[['Latitude', 'Longitude']]
print('geolife coordinate head: ', geolifeCoordinate.head())

allCoordinate = getAllCoordinates(
gowallaCoordinate, brightkiteCoordinate, geolifeCoordinate)

print('all coordinate head: ', allCoordinate.head())

saveDataFrameToTSV(allCoordinate, 'allCoordinate-2.tsv', 'data')
# saveDataFrameToTSV(gowallaCleanedDataFrame,
#                    'small_clean_data.tsv', 'data/gowalla')
# saveDataFrameToTSV(brightkiteCleanedDataFrame,
#                    'small_clean_data.tsv', 'data/brightkite')
# saveDataFrameToTSV(geolifeCleanedDataFrame,
#    'small_clean_data.tsv', 'data/geolife')
