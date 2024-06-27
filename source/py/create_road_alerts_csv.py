import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CREATING .CSV WITH ROAD ALERTS DATA
# Run this script to create the .csv files with the road alerts data

# ROAD ALERTS
road_alerts_path = "alerts.json"

# read json file
df = pd.read_json(road_alerts_path)
# convert to csv
df.to_csv("alerts.csv")

# get dateIssued column values
dateIssued = df['dateIssued'].values
df[['dateIssued', 'timeIssued']] = df['dateIssued'].str.split('T', expand=True)
df['timeIssued'] = df['timeIssued'].str.split('.', expand=True)[0]
# print(df['timeIssued'].values)

# get start_date column values
validFrom = df['validFrom'].values
df[['dateStart', 'timeStart']] = df['validFrom'].str.split('T', expand=True)
df['timeStart'] = df['timeStart'].str.split('.', expand=True)[0]

# get end_date column values
validTo = df['validTo'].values
df[['dateEnd', 'timeEnd']] = df['validTo'].str.split('T', expand=True)
df['timeEnd'] = df['timeEnd'].str.split('.', expand=True)[0]

# get subCategory column values
subCategory = df['subCategory'].values

# get location column values
location = df['location'].values
lat = []
long = []
for loc in location:
    if len(loc) == 2:
        lat.append(loc[1])
        long.append(loc[0])
    else:
        lat.append(0)
        long.append(0)

# create .csv with the selected columns
df = pd.DataFrame({'subCategory': subCategory, 'start_date': df['dateStart'].values,
                   'start_time': df['timeStart'].values, 'end_date': df['dateStart'].values,
                   'end_time': df['timeEnd'].values, 'latitude': lat, 'longitude': long})
df.to_csv("road_constrains.csv")

# convert time hh:mm:ss to seconds
time = df['start_time'].values
seconds = []
for t in time:
    h, m, s = t.split(':')
    seconds.append(int(h) * 3600 + int(m) * 60 + int(s))
# print(seconds)

# add seconds column to dataframe
df['seconds'] = seconds
df.to_csv("road_constrains_sec.csv")

# Filter rows where the date is not previous to 2021
df = df[df['start_date'] >= "2021-01-01"]

# Save the filtered DataFrame to a CSV file
df.to_csv("road_constrains_filtered_old_dates.csv")

# plot events by hours
plt.plot(df['seconds'].values, df['subCategory'].values, '.')
plt.xlabel('time(sec)')
plt.xticks(np.arange(0, 86400, 3600), labels=np.arange(0, 24, 1))
plt.ylabel('event')
plt.title('Road Constrains')
plt.show()
