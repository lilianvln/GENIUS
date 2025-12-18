from tabulate import tabulate  # Import tabulate for pretty table formatting
from CONSTANTS import genre_synonyms, features, valid_genres  # Import constants related to genres and features
from prompt_treatment import extract_all  # Import the function to extract genres, artists, and periods from the prompt
from generate_playlist import generate_playlist  # Import the function to generate playlists based on user input


# Function to handle playlist creation based on a user prompt
def music_reco_prompt_function(df):
    while True:
        print("\nYou chose to create a playlist with a prompt.")

        # Ask the user to enter a prompt
        prompt = input("\nPlease enter your prompt for playlist creation:\n>>> ").strip()

        try:
            # Use the 'extract_all' function to extract genres, artists, and periods from the user’s prompt
            genres, artists, periods = extract_all(genre_synonyms, prompt)

            # Display the extracted information in a table
            print("\nHere's the information extracted from your prompt:")
            data = [
                ["Genres", ", ".join(genres) if genres else "N/A"],
                # If genres are found, join them in a string, else display "N/A"
                ["Artists", ", ".join(artists) if artists else "N/A"],  # Same for artists
                ["Periods", ", ".join(periods) if periods else "N/A"],  # Same for periods
            ]
            print(tabulate(data, headers=["Category", "Details"],
                           tablefmt="grid"))  # Print the extracted details in a tabular format

            # Ask the user to confirm the extracted information
            confirm = input("\nAre you satisfied with the extracted prompt? (Yes/No)\n>>> ").strip().lower()
            if confirm in ['yes', 'y']:  # If the user is satisfied, break the loop and proceed
                break

        except Exception as e:
            # If an error occurs during the extraction process, display an error message
            print(f"\nAn error occurred while processing your prompt. Please try again.\nError details: {e}")

    # Prompt the user for the number of songs in the playlist
    while True:
        try:
            num_songs = int(
                input("\nHow many songs do you want in your playlist?\n>>> "))  # Ask for the number of songs
            if num_songs > 0:  # Check if the number is positive
                break  # Exit the loop if a valid number is entered
            else:
                print("Please enter a positive integer.")  # Error message for invalid number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")  # Error message for non-integer input

    # Generate the playlist based on the user’s preferences
    try:
        playlist = generate_playlist(df, num_songs, artists=artists, genres=genres,
                                     year_range=periods)  # Generate playlist
        if not playlist.empty:  # If the playlist is not empty, display it
            print("\nHere’s your generated playlist:")
            print(tabulate(playlist, headers='keys', tablefmt='grid'))  # Display the generated playlist in a table
            return playlist  # Return the generated playlist
        else:
            print(
                "No songs match your prompt. Please try again with different criteria.")  # Error message if no songs match
    except Exception as e:
        # If an error occurs during playlist generation, display an error message
        print(f"\nAn error occurred while generating the playlist: {e}")