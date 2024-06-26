import pandas as pd

# Read the CSV file
df = pd.read_csv('../data/airQualityData.csv')

locations_array = [
    {'Name': 'OFF - MANUTENCAO - Porto - SmartAirSense - Parque da Cidade / Circunvalacao',
        'Longitude': -8.59837, 'Latitude': 41.1484},
    {'Name': 'ManutencaoPorto - SmartAirSense - Parque da Cidade / Circunvalacao',
        'Longitude': -8.59837, 'Latitude': 41.1484},
    {'Name': 'Porto - SmartAirSense - Arca dAgua',
        'Longitude': -8.61319, 'Latitude': 41.1719},
    {'Name': 'Porto - SmartAirSense - Av. da Boavista / Av. do Parque',
        'Longitude': -8.67215, 'Latitude': 41.1652},
    {'Name': 'Porto - SmartAirSense -Fernao de Magalhaes / Monte Aventino',
        'Longitude': -8.5907, 'Latitude': 41.1625}
]

# Get unique timestamps
timestamps = ['00:00:00',
              '01:00:00',
              '02:00:00',
              '03:00:00',
              '04:00:00',
              '05:00:00',
              '06:00:00',
              '07:00:00',
              '08:00:00',
              '09:00:00',
              '10:00:00',
              '11:00:00',
              '12:00:00',
              '13:00:00',
              '14:00:00',
              '15:00:00',
              '16:00:00',
              '17:00:00',
              '18:00:00',
              '19:00:00',
              '20:00:00',
              '21:00:00',
              '22:00:00',
              '23:00:00']

# Create a list to store dictionaries
result_data = []

# Iterate through each location in the predefined array
for location in locations_array:
    # Iterate through each timestamp for the current location
    for timestamp in timestamps:
        result_row = {'name': location['Name'], 'longitude': location['Longitude'],
                      'latitude': location['Latitude'], 'timestamp': timestamp}

        # Retrieve the 'o3' value for the current location and timestamp
        timestamp_data = df[(df['name'] == location['Name'])
                            & (df['time_observed'] == timestamp)]
        unique_value = timestamp_data['co'].iloc[0] if not timestamp_data.empty else None
        result_row['co'] = unique_value

        # Check for duplicates before appending to the result_data list
        if not any((d['name'] == location['Name']) and (d['timestamp'] == timestamp) for d in result_data):
            result_data.append(result_row)

# Convert the list of dictionaries to a DataFrame
result_df = pd.DataFrame(result_data)

# Save the result DataFrame to a new CSV file
result_df.to_csv('result_data.csv', index=False)

print("Result file 'result_data.csv' created.")
