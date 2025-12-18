import pandas as pd
from FUNCTIONS import clean_text

def generate_playlist(df, num_songs, genres=None, artists=None, year_range=None):
    # Validate num_songs
    if not isinstance(num_songs, int) or num_songs <= 0:
        raise ValueError("num_songs must be a positive integer")

    # Make a copy of the DataFrame to avoid modifying the original
    playlist = df.copy()

    # Filter by genre if specified
    if genres:
        genres = [clean_text(genre) for genre in genres]
        playlist = playlist[playlist['playlist_genre_cleaned'].isin(genres)]

    # Filter by artists if specified
    if artists:
        artists = [clean_text(artist) for artist in artists]
        playlist = playlist[playlist['track_artist_cleaned'].isin(artists)]

    # Filter by year range if specified
    if year_range:
        if isinstance(year_range, list):
            if isinstance(year_range[0], str) and '-' in year_range[0]:  # Single range as a string
                year_range = list(map(int, year_range[0].split('-')))
                start_year, end_year = year_range
                playlist = playlist[
                    (playlist['track_album_release_date'] >= start_year) &
                    (playlist['track_album_release_date'] <= end_year)
                ]
            else:  # List of specific years
                year_range = [int(year) for year in year_range]
                playlist = playlist[playlist['track_album_release_date'].isin(year_range)]
        else:
            raise ValueError("Invalid year_range format. Expected a list of years or a year range string.")

    # Check if playlist is empty after filtering
    if playlist.empty:
        print("No songs match your criteria.")
        return pd.DataFrame()  # Return an empty DataFrame if no songs match the filter

    # Limit the number of songs and sort by popularity
    playlist = (
        playlist.sort_values(by='track_popularity', ascending=False)
        [['track_name', 'track_artist', 'track_album_release_date', 'playlist_genre_cleaned']]
        .head(num_songs)
    )

    # Reset index for clean output
    playlist = playlist.reset_index(drop=True)

    return playlist