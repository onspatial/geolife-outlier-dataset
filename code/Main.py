import pandas

# read txt file into a dataframe
# dataFrame = pandas.read_csv('./data/allcat.csv', sep=',+s')

# print(dataFrame.head())

# # remove duplicate
# dataFrame = dataFrame.drop_duplicates()
# print(dataFrame.head())

# # save dataframe to tsv
# dataFrame.to_csv('./data/allcatclean.tsv', sep='\t', index=False)

data_feather = pandas.read_feather('data/geolife/location/concat.feather')
print(data_feather.head())
data_csv = pandas.read_csv('data/geolife/location/concat.csv')
print(data_csv.head())

print(data_feather.shape)
print(data_csv.shape)

# compare dataframes
for i in range(0, data_feather.shape[0]):
    if str(data_feather.iloc[i, 0]) != str(data_csv.iloc[i, 0]):
        print('feather', data_feather.iloc[i, 0])
        print('csv', data_csv.iloc[i, 0])
        break

