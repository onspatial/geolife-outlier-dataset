import pandas

geolife_df = pandas.read_csv('data/geolife/data.tsv', sep=' ')

geolife_df['ArrivingTime'] = geolife_df['ArrivingTime'].str.split(',').str[0]


print(geolife_df.head())
# print(geolife_df['AgentID'].nunique())
# geolife_df = geolife_df.groupby('ArrivingTime').size().reset_index(name='count')
# busiest_day = geolife_df.loc[geolife_df['count'] == geolife_df['count'].max()]
# print(busiest_day)  # 2009-02-14
# # save the data for this day:2009-02-14 to a file
busiest_day_df = geolife_df.loc[geolife_df['ArrivingTime'] == '2009-02-14'] 

# # count uniq AgentID
print(busiest_day_df['AgentID'].nunique())
geolife_df.to_csv('data/geolife/full.csv', index=False)
busiest_day_df.to_csv('data/geolife/busiest-day-2009-02-14.csv', index=False)
# print(geolife_df.head())

pol_df = pandas.read_csv('data/life/data.tsv', sep=r'\s+')
print(pol_df.head())
pol_df['CheckinTime'] = pol_df['CheckinTime'].str.split('T').str[0]
pol_df.to_csv('data/life/full.csv', index=False)
print(pol_df.head())
random_day = pol_df.loc[pol_df['CheckinTime'] == '2019-07-01']
print(random_day)
random_day.to_csv('data/life/random-day-2019-07-01.csv', index=False)


