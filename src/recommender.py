from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv
import io

@dataclass
class Song:
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        return "Explanation placeholder"


def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file and returns a list of dicts with correct types."""
    songs = []
    with open(csv_path, newline='') as f:
        content = f.read()

    delimiter = '\t' if '\t' in content.split('\n')[0] else ','

    reader = csv.DictReader(io.StringIO(content), delimiter=delimiter)
    for row in reader:
        row = {k.strip(): v.strip() for k, v in row.items()}
        row['id'] = int(row['id'])
        row['energy'] = float(row['energy'])
        row['tempo_bpm'] = float(row['tempo_bpm'])
        row['valence'] = float(row['valence'])
        row['danceability'] = float(row['danceability'])
        row['acousticness'] = float(row['acousticness'])
        songs.append(row)
    print(f"Loaded songs: {len(songs)}")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song against user preferences. Returns (score, reasons)."""
    score = 0.0
    reasons = []

    # Genre match: +2.0
    if song['genre'].lower() == user_prefs.get('genre', '').lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match: +1.0
    if song['mood'].lower() == user_prefs.get('mood', '').lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Energy proximity: up to +1.5 based on closeness
    target_energy = user_prefs.get('energy', 0.5)
    energy_diff = abs(song['energy'] - target_energy)
    energy_score = round((1.0 - energy_diff) * 1.5, 2)
    score += energy_score
    reasons.append(f"energy proximity (+{energy_score})")

    return round(score, 2), reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores all songs and returns top k as (song, score, explanation) tuples."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored.append((song, score, explanation))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]