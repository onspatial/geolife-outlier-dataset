
from utils.GeoDataFrame import getGeolifeDataFrame,findBusiestDayDate, getBusiestDayDataFrame, getDataFrameFromSSV, getPreprocessedPOLTrajDataFrame, getDataFrameFromFeather

import pandas

# geoLifeDataFrame = getGeolifeDataFrame()
# busyDayRow = findBusiestDayDate(geoLifeDataFrame)
# busyDay = busyDayRow.iloc[0]
# dataName = 'geolife'
# print(f'{dataName} busyDay', busyDay)
# getBusiestDayDataFrame(geoLifeDataFrame,busyDay).to_csv(f'data/poster/{dataName}-busiest-day-{busyDay}.tsv', sep=' ', index=False)


# gowallaDataFrame = getDataFrameFromSSV('data/cities/San Francisco_gowalla.tsv')
# busyDayRow = findBusiestDayDate(gowallaDataFrame)
# busyDay = busyDayRow.iloc[0]

# dataName = 'gowalla'
# print(f'{dataName} busyDay', busyDay)
# getBusiestDayDataFrame(gowallaDataFrame,busyDay).to_csv(f'data/poster/{dataName}-busiest-day-{busyDay}.tsv', sep=' ', index=False)

# brightDataFrame = getDataFrameFromSSV('data/cities/San Francisco_brightkite.tsv')
# busyDayRow = findBusiestDayDate(brightDataFrame)
# busyDay = busyDayRow.iloc[0]

# dataName = 'brightkite'
# print(f'{dataName} busyDay', busyDay)
# getBusiestDayDataFrame(brightDataFrame,busyDay).to_csv(f'data/poster/{dataName}-busiest-day-{busyDay}.tsv', sep=' ', index=False)

# dataName = 'pol-traj-2020-02-01.tsv'
# polDataFrame = getPreprocessedPOLTrajDataFrame(dataName, 'data/pol')

# geolifeLocation = getDataFrameFromFeather('geolife/location/concat.feather')


# # exit()

# busyDayRow = findBusiestDayDate(geolifeLocation, timeColumn='time')
# busyDay = busyDayRow.iloc[0]

# dataName = 'geolife'
# busyDay = '2009-02-14'
# print(f'{dataName} busyDay', busyDay)

# busiestDayDataFrame = getBusiestDayDataFrame(geolifeLocation,busyDay,timeColumn='time')
# print(busiestDayDataFrame.head())
# count number of unique users
# print('users:',busiestDayDataFrame['user'].nunique())
# count number of unique locations



# busiestDayDataFrame.to_csv(f'data/poster/{dataName}-busiest-day-{busyDay}.tsv', sep=' ', index=False)









