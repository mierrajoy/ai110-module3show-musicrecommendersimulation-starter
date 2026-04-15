from recommender import load_songs, recommend_songs

def print_recommendations(label: str, user_prefs: dict, songs: list, k: int = 5):
    print(f"\n=== {label} ===")
    recommendations = recommend_songs(user_prefs, songs, k=k)
    for song, score, explanation in recommendations:
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"  Because: {explanation}")

def main():
    songs = load_songs("data/songs.csv")

    # Profile 1: High-Energy Pop
    pop_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    # Profile 2: Chill Lofi
    lofi_prefs = {"genre": "lofi", "mood": "chill", "energy": 0.35}

    # Profile 3: Deep Intense Rock
    rock_prefs = {"genre": "rock", "mood": "intense", "energy": 0.95}

    print_recommendations("High-Energy Pop", pop_prefs, songs)
    print_recommendations("Chill Lofi", lofi_prefs, songs)
    print_recommendations("Deep Intense Rock", rock_prefs, songs)

if __name__ == "__main__":
    main()