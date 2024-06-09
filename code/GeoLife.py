import pandas
data = 'data/geolife/concat_plt.csv'

data_df = pandas.read_csv(data)
print('data_df head: ', data_df.head())
# data_df head:     AgentID   Latitude   Longitude   Zero   Altitude       NumDays        Date      Time
# 0        2  39.925581  116.336281      0      492.0  39858.103368  2009-02-14  02:28:51
# 1        2  39.925761  116.336190      0      492.0  39858.103391  2009-02-14  02:28:53
# 2        2  39.925846  116.336188      0      492.0  39858.103403  2009-02-14  02:28:54
# 3        2  39.925836  116.336194      0      492.0  39858.103461  2009-02-14  02:28:59
# 4        2  39.925827  116.336201      0      492.0  39858.103519  2009-02-14  02:29:04
# remove data out of this bond:[116.1632651  39.7831364 116.6294095  40.039197 ]
data_df = data_df[(data_df['Longitude'] >= 116.1632651) & (data_df['Longitude'] <= 116.6294095)]
data_df = data_df[(data_df['Latitude'] >= 39.7831364) & (data_df['Latitude'] <= 40.039197)]
data_df = data_df.reset_index(drop=True)
data_df.to_csv('data/geolife/bjng_2009-02-14_plt.csv', index=False)
# count unique AgentID
print('count unique AgentID: ', data_df['AgentID'].nunique())