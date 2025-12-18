import nltk
import re
import pandas as pd
from spacy.lang.ca.tokenizer_exceptions import period

from CONSTANTS import dico_language
from FUNCTIONS import prompt_cleaning, nlp

# Extract Genre function: This function extracts genres mentioned in the prompt
def extract_genre(prompt, genres):
    genre_extract = []
    # Loop through each genre category and its corresponding list of synonyms
    for key, value in genres.items():
        # Create a regex pattern to match any of the synonyms for this genre
        pattern = r'\b(' + '|'.join(value) + r')\b'
        # If the pattern is found in the prompt, add the genre key to the result list
        if re.search(pattern, prompt):
            genre_extract.append(key)
    return genre_extract

# Extract Artist Names function: This function uses NLP to extract artist names from the prompt
def extract_artists(prompt):
    doc = nlp(prompt)
    # Return all recognized entities that are labeled as "PERSON" (i.e., artist names)
    return [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

# Extract Years function: This function uses regex to extract valid years (between 1000 and 2999) from the text
def extract_years(text):
    # Regular expression to match years between 1000 and 2999
    year_pattern = r'\b(1[0-9]{3}|2[0-9]{3})\b'
    # Find all matches in the text
    years = re.findall(year_pattern, text)
    # Convert matches to integers, remove duplicates, and sort
    periods = sorted(set(map(int, years)))
    if periods:
        # Format the years as strings
        periods = [f"{period}" for period in periods]
    else:
        periods = []  # If no years were found, return an empty list
    return periods

# Main Extraction Function: Combines genre, artist, and year extraction
def extract_all(genre_synonyms, prompt):
    # Clean the prompt by removing unnecessary elements (like stop words or punctuation)
    prompt_cleaned = prompt_cleaning(prompt)
    # Extract genres using the cleaned prompt and genre synonyms
    genre = extract_genre(prompt_cleaned, genre_synonyms)
    # Extract artist names from the original prompt
    artists = extract_artists(prompt)
    # Extract years from the cleaned prompt
    period = extract_years(prompt_cleaned)
    return genre, artists, period