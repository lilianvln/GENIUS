import pandas as pd
import itertools

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity

from CONSTANTS import genre_synonyms, features
from FUNCTIONS import get_track_id_by_name
from GUI import GUI

from recommend_songs import recommend_songs
from generate_playlist import generate_playlist

import warnings
from urllib3.exceptions import NotOpenSSLWarning

# Filtrer les avertissements liés à NotOpenSSLWarning
warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

# Read the data
df_spotify = pd.read_csv('data_cleaned.csv')

# Proceed with computing the feature vectors and similarity matrix
feature_vectors = df_spotify[features].values
similarity_matrix = cosine_similarity(feature_vectors)

# Launch the GUI with the precomputed similarity matrix
GUI(df_spotify, similarity_matrix)
