import numpy as np
from tabulate import tabulate

from FUNCTIONS import weighted_similarity_score

def recommend_songs(track_ids, similarity_matrix, df, top_n=10, weight_popularity=0.3):
    # Check if track_ids are valid (i.e., exist in the DataFrame)
    if not track_ids:
        return f"Tracks/artists do not exist in the DataFrame."

    # Get the indices of the tracks from the DataFrame
    track_indices = [df[df['track_id'] == track_id].index[0] for track_id in track_ids]

    # Calculate the average similarity of the selected tracks
    combined_similarity = np.mean(similarity_matrix[track_indices], axis=0)

    # Find indices of the most similar tracks (excluding the input tracks)
    similar_indices = np.argsort(combined_similarity)[::-1]
    similar_indices = [idx for idx in similar_indices if idx not in track_indices][:top_n]

    # Get the similarity scores for the recommended tracks
    similar_scores = combined_similarity[similar_indices]

    # Create a DataFrame for the recommendations
    recommendations = df.iloc[similar_indices][['track_name', 'track_artist', 'playlist_genre', 'track_popularity']].copy()
    recommendations['similarity_score'] = similar_scores

    # Calculate a weighted score considering both similarity and popularity
    recommendations['weighted_score'] = recommendations.apply(
        lambda row: weighted_similarity_score(row['similarity_score'], row['track_popularity'], weight_popularity),
        axis=1
    )

    # Sort the recommendations by the weighted score
    recommendations = recommendations.sort_values(by='weighted_score', ascending=False)

    # If recommendations are found, print them
    if not recommendations.empty:
        print(tabulate(recommendations, headers='keys', tablefmt='grid'))
        return recommendations
    else:
        print("No songs match your prompt.")