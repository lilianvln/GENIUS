import pandas as pd
from GUI_function.music_reco_answer_function import *
from GUI_function.music_reco_prompt_function import *
from GUI_function.generator_playlist_reco_function import *
from tabulate import tabulate


def display_welcome():
    print("=" * 100)
    print(" Welcome to the SOUNDER application, we're here to help you create your own playlist.")
    print("=" * 100)


def display_banner(title):
    print("\n")
    print("-" * 100)
    print(' ' * (50 - len(title) // 2) + title)
    print("-" * 100)


def display_menu(menus):
    for i, menu in enumerate(menus):
        print(f"{i} - {menu}")


def GUI(df_spotify, similarity_matrix):
    playlist = pd.DataFrame()  # Initialize empty playlist
    display_welcome()  # Show welcome message
    while True:
        display_banner("MAIN MENU")  # Show main menu banner

        # Main menu options
        display_menu([
            "Exit",
            "Playlist generator with Prompt extraction",
            "Playlist generator with Data",
            "Playlist generator with recommendations",
            "Show playlist",
        ])

        # Prompt user for menu choice
        opt_main_menu = input("\nPlease select menu:\n>>> ").strip()

        if opt_main_menu == '0':  # Exit the application
            print("\nExiting the application...")
            break

        elif opt_main_menu == '1':  # Playlist generator with prompt extraction
            display_banner("Playlist generator with Prompt extraction")
            playlist = music_reco_prompt_function(df_spotify)

        elif opt_main_menu == '2':  # Playlist generator with data
            display_banner("Playlist generator with Data")
            playlist = music_reco_answer_function(df_spotify)

        elif opt_main_menu == '3':  # Playlist generator with recommendations
            display_banner("Playlist generator with recommendations")
            if not playlist.empty:
                recommendations = generator_playlist_reco_function(playlist, df_spotify, similarity_matrix)
                playlist = playlist[['track_name', 'track_artist']]
                recommendations = recommendations[['track_name', 'track_artist']]
                playlist = pd.concat([playlist, recommendations], ignore_index=True)
            else:
                print("Warning! Please create a playlist first!")

        elif opt_main_menu == '4':  # Show current playlist
            display_banner("Show Playlist")
            if not playlist.empty:
                print(tabulate(playlist, headers='keys', tablefmt='grid'))
            else:
                print("Warning! Please create a playlist first!")

        else:
            print("\nWarning! Invalid choice. Please select a valid option.")