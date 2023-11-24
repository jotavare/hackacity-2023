import folium
import pandas as pd

df = pd.read_csv('../data/noise_levels_data.csv')

# Create a folium map centered at the mean of the coordinates
map_center = [df['latitude'].mean(), df['longitude'].mean()]
mymap = folium.Map(location=map_center, zoom_start=10)

# Add markers for each point in the DataFrame
for index, row in df.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']], popup=row['name']).add_to(mymap)

# Save the map as an HTML file
mymap.save('map_with_points.html')
