import re  # Import regular expression module for input validation

from tabulate import tabulate  # Import tabulate for pretty table formatting

from CONSTANTS import genre_synonyms, features, valid_genres  # Import constants, including valid genres

from generate_playlist import generate_playlist  # Import the function to generate playlists based on user inputs

# Function to handle the music recommendation process
def music_reco_answer_function(df):
    # Initialize empty lists to store user choices for genres, artists, and periods
    genres, artists, periods = [], [], []

    while True:
        print("\nYou’ve chosen to create a playlist.")

        # Genre selection
        genres = []
        print("\nChoose a genre (rap, edm, latin, r&b, rock, pop) or press 0 to finish.")
        while True:
            genre = input("Please enter your song genre:\n     >>> ").strip().lower()  # Get user input for genre
            if genre == '0':  # Exit loop if user presses 0
                break
            elif genre in valid_genres:  # If the genre is valid, add it to the list
                genres.append(genre)
            else:
                print(f"Invalid genre. Please choose from {', '.join(valid_genres)}.")  # Error message for invalid genre

        # Artist selection
        artists = []
        print("\nPlease enter one or more artist names or press 0 to finish.")
        while True:
            artist = input("Please enter the name of an artist:\n     >>> ").strip()  # Get user input for artist
            if artist == '0':  # Exit loop if user presses 0
                break
            elif artist:  # Ensure that a non-empty string is entered
                artists.append(artist)
            else:
                print("Invalid input. Please enter a valid artist name.")  # Error message for empty input

        # Period selection
        periods = []
        print("\nPlease enter years or time periods (e.g., 1980, 1990-2000, 2001, 2002) or press 0 to finish.")

        while True:
            period = input("Please enter years or a time period:\n     >>> ").strip()  # Get user input for time period
            # Validate if the input is a valid year or time period range
            if period == '0':  # Exit loop if user presses 0
                break
            elif re.match(r'^(\d{4}(-\d{4})?|(\d{4})(, \d{4})*)$', period):  # Regex to check valid format (single years, ranges, or lists)
                # If the input contains a comma (e.g., a list of years), split it into a list
                if ',' in period:
                    periods = list(map(str, period.split(',')))
                else:  # If the input is a single year or a range, add it directly
                    periods.append(period)
                break
            else:
                print(
                    "Invalid input. Please enter valid years (e.g., 1980) or a valid time period (e.g., 1990-2000, 2001, 2002).")  # Error message for invalid input

        # Display the selections made by the user
        print("\nHere’s the information extracted from your selections:")
        data = [
            ["Genre", ", ".join(genres) if genres else "N/A"],  # Display genres if selected
            ["Artists", ", ".join(artists) if artists else "N/A"],  # Display artists if selected
            ["Period", ", ".join(periods) if periods else "N/A"],  # Display periods if selected
        ]
        print(tabulate(data, headers=["Category", "Details"], tablefmt="grid"))  # Display formatted selections using tabulate

        # Ask the user to confirm the selections
        confirm = input("\nAre you satisfied with your prompt? (Yes/No)\n>>> ").strip().lower()
        if confirm in ['yes', 'y']:  # Exit loop if the user confirms
            break

    # Number of songs selection
    while True:
        try:
            num_songs = int(input("\nHow many songs do you want in your playlist?\n>>> "))  # Get user input for number of songs
            if num_songs > 0:  # Ensure the number is positive
                break
            else:
                print("Please enter a positive integer.")  # Error message for invalid number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")  # Error message for non-integer input

    # Generate the playlist based on the user’s preferences
    try:
        playlist = generate_playlist(df, num_songs, artists=artists, genres=genres, year_range=periods)  # Call the generate_playlist function
        if not playlist.empty:  # If the playlist is not empty, display it
            print("\nHere’s your generated playlist:")
            print(tabulate(playlist, headers='keys', tablefmt='grid'))  # Display the generated playlist in a formatted table
            return playlist  # Return the playlist
        else:
            print("No songs match your prompt. Please try again with different criteria.")  # Error message if no songs match
    except Exception as e:  # Handle any potential errors during playlist generation
        print(f"\nAn error occurred while generating the playlist: {e}")  # Display error message