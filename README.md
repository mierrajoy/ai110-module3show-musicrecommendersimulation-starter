# 🎵 Music Recommender Simulation

## Project Summary
This project basicaly simulates a content-based music recommendation system. It loads a catalog of songs from a CSV file, scores each song against a user's taste profile, and returns the top ranked suggestions with explanations.

## How The System Works

Real-world platforms like Spotify do actually use a mix of collaborative filtering (what similar users liked) and content-based filtering (matching song attributes to your taste). This simulation focuses on content-based filtering, it compares each song's genre, mood, and also energy level directly to the user's preferences.

**Algorithm Recipe:**
 +2.0 points for a genre match
 +1.0 point for a mood match
 Up to +1.5 points based on how close the song's energy is to the user's target energy

**Features used:** genre, mood, energy

## Terminal Output Screenshots

### High-Energy Pop Profile

=== High-Energy Pop ===
Sunrise City - Score: 4.47
  Because: genre match (+2.0), mood match (+1.0), energy proximity (+1.47)
Gym Hero - Score: 3.30
  Because: genre match (+2.0), energy proximity (+1.30)
Rooftop Lights - Score: 2.44
  Because: mood match (+1.0), energy proximity (+1.44)
Night Drive Loop - Score: 1.42
  Because: energy proximity (+1.42)
Storm Runner - Score: 1.33
  Because: energy proximity (+1.33)

### Chill Lofi Profile
=== Chill Lofi ===
Library Rain - Score: 4.50
  Because: genre match (+2.0), mood match (+1.0), energy proximity (+1.50)
Midnight Coding - Score: 4.40
  Because: genre match (+2.0), mood match (+1.0), energy proximity (+1.40)
Focus Flow - Score: 3.42
  Because: genre match (+2.0), energy proximity (+1.42)
Spacewalk Thoughts - Score: 2.40
  Because: mood match (+1.0), energy proximity (+1.40)
Coffee Shop Stories - Score: 1.47
  Because: energy proximity (+1.47)

### Deep Intense Rock Profile
=== Deep Intense Rock ===
Storm Runner - Score: 4.44
  Because: genre match (+2.0), mood match (+1.0), energy proximity (+1.44)
Gym Hero - Score: 2.47
  Because: mood match (+1.0), energy proximity (+1.47)
Sunrise City - Score: 1.30
  Because: energy proximity (+1.30)
Rooftop Lights - Score: 1.22
  Because: energy proximity (+1.22)
Night Drive Loop - Score: 1.20
  Because: energy proximity (+1.20)

## Potential Biases
Honestly, this system may over-prioritize genre since it carries the highest point weight (+2.0). A song that perfectly matches mood and energy but has a different genre will almost always rank lower than a genre-matching song with poor mood and energy alignment.