
from utils.GeoDataFrame import getBoundingBoxFilteredDataFrame, getCleanedCSVFile, saveDataFrameToTSV, getUserIDFilteredDataFrame
from utils.Geo import getTenCategoryLocationType

datasetName = 'clean_data.tsv'
# datasetDirectory = 'data/brightkite'
datasetDirectory = 'data/gowalla'
dataName = datasetDirectory.split('/')[-1]
print(f'processing {dataName} data...')
domesticCheckInLimit = 100
# Berlin bounding box: (52.34, 13.09, 52.69, 13.76);
# Rome bounding box: (41.78, 12.27, 42.01, 12.74);
# San Francisco bounding box: (37.7, -122.51, 37.81, -122.35);
# New York bounding box: (40.49, -74.26, 40.92, -73.69);
# Atlanta bounding box: (33.58, -84.58, 33.98, -84.17);
# Beijing bounding box: (39.75, 116.06, 40.08, 116.72);


citiesBoundingBox = {'Berlin': {'minLatitude': 52.34, 'maxLatitude': 52.69, 'minLongitude': 13.09, 'maxLongitude': 13.76},
                     'Rome': {'minLatitude': 41.78, 'maxLatitude': 42.01, 'minLongitude': 12.27, 'maxLongitude': 12.74},
                     'San Francisco': {'minLatitude': 37.7, 'maxLatitude': 37.81, 'minLongitude': -122.51, 'maxLongitude': -122.35},
                     'New York': {'minLatitude': 40.49, 'maxLatitude': 40.92, 'minLongitude': -74.26, 'maxLongitude': -73.69},
                     'Atlanta': {'minLatitude': 33.58, 'maxLatitude': 33.98, 'minLongitude': -84.58, 'maxLongitude': -84.17},
                     'Beijing': {'minLatitude': 39.75, 'maxLatitude': 40.08, 'minLongitude': 116.06, 'maxLongitude': 116.72}}


mainDataFrame = getCleanedCSVFile(datasetName, datasetDirectory)
boundedBoxDataFrame = {}
citiesDomesticUsersDataFrame = {}
for city in citiesBoundingBox:
    boundedBoxDataFrame[city] = getBoundingBoxFilteredDataFrame(
        mainDataFrame, citiesBoundingBox[city])
    # get user ids for each city that has more than 1000 check-ins
    citiesDomesticUsersDataFrame[city] = boundedBoxDataFrame[city].groupby(
        'AgentID').filter(lambda x: len(x) > domesticCheckInLimit)

    print(f'{city}: {len(boundedBoxDataFrame[city])}')
    print(
        f'{city} number of unique users: {len(citiesDomesticUsersDataFrame[city]["AgentID"].unique())}')

# add location type to each city's domestic user dataframe

for city in citiesDomesticUsersDataFrame:
    citiesDomesticUsersDataFrame[city]['LocationType'] = citiesDomesticUsersDataFrame[city].apply(
        lambda row: getTenCategoryLocationType(row['Latitude'], row['Longitude']), axis=1)
    saveDataFrameToTSV(
        citiesDomesticUsersDataFrame[city], f'{city}_{dataName}_domestic.tsv')
    print(
        f'{city} domestic user with location type: {len(citiesDomesticUsersDataFrame[city])}')
