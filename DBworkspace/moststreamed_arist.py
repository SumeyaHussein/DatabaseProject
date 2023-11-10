import pandas as pd

# Load the CSV file into a DataFrame
path = pd.read_csv("spotify-2023.csv", encoding='ISO-8859-1')

# Rename columns for better readability
path.rename(columns={
    'artist(s)_name': 'artist_name',
    'danceability_%': 'danceability_percent',
    'valence_%': 'valence_percent',
    'energy_%': 'energy_percent',
    'acousticness_%': 'acousticness_percent',
    'instrumentalness_%': 'instrumentalness_percent',
    'liveness_%': 'liveness_percent',
    'speechiness_%': 'speechiness_percent'
}, inplace=True)

# Display the DataFrame
print(path.head(5))  # Modify this line for the desired output

# Query for the most streamed artist
result = path.groupby('artist_name').agg(total_streams=('streams', 'sum')).sort_values('total_streams', ascending=False).reset_index()

# Display the result
print(result)
