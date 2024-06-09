
import os
import pandas
raw_data_dir = 'data/geolife/raw'
columns = ['AgentID','Latitude', 'Longitude', 'Zero', 'Altitude', 'NumDays', 'Date', 'Time']
data_df = pandas.DataFrame(columns=columns)
raw_lines='AgentID,Latitude,Longitude,Zero,Altitude,NumDays,Date,Time'+ '\n'
for root, dirs, files in os.walk(raw_data_dir):
    for file in files:
        if file.endswith('.plt'):
            agent_id = str(int(root.split('/')[-2]))

            file_path = os.path.join(root, file)
            print('processing file: ', file_path)
            with open(file_path, 'r') as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if i > 5:
                        line =  agent_id + ',' + line 
                        raw_lines += line

with open('data/geolife/concat_plt.csv', 'w') as f:
    f.write(raw_lines)  
   