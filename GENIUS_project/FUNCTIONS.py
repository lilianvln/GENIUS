import re  # Import regular expression module for text processing
import spacy  # Import spaCy for advanced natural language processing (NLP)

from nltk.corpus import stopwords  # Import stopwords from NLTK for text cleaning
from nltk.corpus import wordnet as wn  # Import WordNet for synonym extraction
from collections import defaultdict  # Import defaultdict for convenient dictionary handling

# Load the English language model for spaCy (large version for better accuracy)
nlp = spacy.load("en_core_web_lg")

# Function to clean the prompt by removing unwanted characters and stopwords
def prompt_cleaning(prompt):
    text_lower = prompt.lower()  # Convert the entire text to lowercase for uniformity
    # Remove non-alphanumeric characters, excluding spaces and digits
    text_cleaned = re.sub(r'[^a-z0-9\s]', '', text_lower)
    doc = nlp(text_cleaned)  # Process the text with spaCy

    # Lemmatize the words and filter out stopwords and punctuation
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]

    # Return the cleaned and lemmatized prompt as a string
    return ' '.join(tokens)


# Function to clean general text (different from prompt cleaning)
def clean_text(text):
    # Check if the text is a valid string (not empty or None)
    if isinstance(text, str):
        text = text.lower()  # Convert to lowercase
        # Remove non-alphanumeric characters (except spaces)
        text = re.sub(r'[^a-z0-9\s]', '', text)
        # Remove stopwords using NLTK's stopword list
        stop_words = set(stopwords.words('english'))  # Change to 'french' or other languages if needed
        text = ' '.join(word for word in text.split() if word not in stop_words)

    return text


# Function to get synonyms of a word using WordNet
def get_synonyms(word):
    synonyms = {word}  # Include the word itself to avoid an empty set
    for syn in wn.synsets(f"{word}_music"):  # Search WordNet for music-specific synonyms of the word
        for lemma in syn.lemmas():  # Iterate through the lemma (synonym) list
            synonyms.add(prompt_cleaning(lemma.name()))  # Clean the synonym and add it to the set
    return list(synonyms)


# Function to get synonyms for a list of words
def get_synonyms_for_list(word_list):
    all_synonyms = defaultdict(list)  # Using defaultdict for automatic empty lists
    for word in word_list:
        all_synonyms[word] = get_synonyms(word)  # Populate the dictionary with synonyms for each word
    return all_synonyms


# Function to get the track ID based on the track name and artist from the provided DataFrame
def get_track_id_by_name(track_name, track_artist, df_sample):
    track_artist = clean_text(track_artist)  # Clean the artist's name

    if track_name is not None:
        track_name = clean_text(track_name)  # Clean the track name
        # Look for an exact match in the cleaned DataFrame
        track = df_sample[
            (df_sample['track_name_cleaned'] == track_name) &
            (df_sample['track_artist_cleaned'] == track_artist)
        ]
    else:
        # If no track name is provided, get all tracks by the artist
        track = df_sample[
            df_sample['track_artist_cleaned'] == track_artist
        ]

    if track.empty:
        return ''  # Return an empty string if no match is found

    # Return the track IDs as a list if a match is found
    return track['track_id'].tolist()


# Function to calculate a weighted similarity score based on similarity and popularity
def weighted_similarity_score(similarity, popularity, weight_popularity=0.3):
    return similarity * (1 - weight_popularity) + (popularity / 100) * weight_popularity