import itertools  # Import itertools for handling iterable data
from tabulate import tabulate  # Import tabulate for table formatting (not used in this function)
from CONSTANTS import genre_synonyms, features, \
    valid_genres  # Import constants (possibly for filtering or categorizing genres)
from FUNCTIONS import get_track_id_by_name  # Import a function to get track IDs by name
from recommend_songs import recommend_songs  # Import the song recommendation function


# Define the function that generates playlist recommendations
def generator_playlist_reco_function(playlist, df, similarity_matrix):
    # Convert the playlist into a list of track names and artists
    playlist_list = playlist[['track_name', 'track_artist']].values.tolist()
    track_ids = []  # Initialize an empty list to store track IDs

    # Iterate through each track (title, artist) in the playlist and get their corresponding track IDs
    for title, artist in playlist_list:
        track_ids.append(get_track_id_by_name(None, artist, df))  # Append the track ID to the list
    track_ids = list(itertools.chain.from_iterable(track_ids))  # Flatten the list of track IDs

    # Prompt the user to input the number of songs they want in the playlist
    while True:
        try:
            num_songs = int(input("\nHow many songs do you want in your playlist?\n>>> "))  # Get user input
            if num_songs > 0:  # Ensure the number is positive
                break  # Exit the loop if the input is valid
            else:
                print("Please enter a positive integer.")  # Prompt again if the input is not positive
        except ValueError:  # Handle the case where input is not a valid integer
            print("Invalid input. Please enter a valid integer.")

    # Get song recommendations based on the track IDs and similarity matrix
    recommendations = recommend_songs(track_ids, similarity_matrix, df, top_n=num_songs)

    return recommendations  # Return the list of recommended songs