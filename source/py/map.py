import folium
import pandas as pd
import random

# Read the CSV file
df = pd.read_csv('../data/roadConstrains.csv')

# Convert latitude and longitude to numeric values
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

# Drop rows with missing latitude or longitude values
df = df.dropna(subset=['latitude', 'longitude'])

# Check if there are still rows in the DataFrame
if not df.empty:
    # Create a folium map centered at the mean of the coordinates
    map_center = [df['latitude'].mean(), df['longitude'].mean()]
    mymap = folium.Map(location=map_center, zoom_start=13.2)

    # Add markers for each event in the DataFrame with random colors
    for index, row in df.iterrows():
        # Generate a random color (orange, green, or red)
        color = random.choice(['orange', 'green', 'red'])

        # Create an Icon with the specified color
        icon = folium.Icon(color=color)

        # Add marker to the map using the Icon
        folium.Marker(location=[row['latitude'], row['longitude']],
                      popup=row['subCategory'], icon=icon).add_to(mymap)

    # Save the map as an HTML file
    mymap.save('map.html')
    print("Map saved to map.html")
else:
    print("No valid coordinates found in the CSV.")
