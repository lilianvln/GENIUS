from FUNCTIONS import get_synonyms_for_list

valid_genres = ['rap', 'edm', 'latin', 'r&b', 'rock', 'pop']

genre_synonyms = get_synonyms_for_list(valid_genres)

dico_language = {
    'tr': 'turkish', 'en': 'english', 'he': 'hebrew', 'no': 'norwegian',
    'fil': 'filipino', 'it': 'italian', 'pl': 'polish', 'fr': 'french',
    'ru': 'russian', 'de': 'german', 'pt': 'portuguese', 'ja': 'japanese',
    'es': 'spanish', 'fi': 'finnish', 'da': 'danish', 'sv': 'swedish',
    'sr': 'serbian', 'ko': 'korean', 'vi': 'vietnamese', 'ca': 'catalan',
    'ta': 'tamil', 'el': 'greek', 'sk': 'slovak', 'ro': 'romanian',
    'cs': 'czech', 'id': 'indonesian', 'bg': 'bulgarian', 'th': 'thai',
    'nl': 'dutch', 'la': 'latin', 'ar': 'arabic', 'fa': 'persian',
    'nn': 'norwegian nynorsk', 'zh': 'chinese', 'my': 'burmese',
    'hi': 'hindi', 'uk': 'ukrainian', 'lv': 'latvian', 'eu': 'basque',
    'az': 'azerbaijani', 'ne': 'nepali', 'sq': 'albanian', 'sl': 'slovenian',
    'ka': 'georgian', 'hu': 'hungarian', 'is': 'icelandic', 'kk': 'kazakh',
    'hr': 'croatian', 'af': 'afrikaans', 'si': 'sinhala', 'ceb': 'cebuano',
    'et': 'estonian', 'ur': 'urdu'
}

features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
            'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']
