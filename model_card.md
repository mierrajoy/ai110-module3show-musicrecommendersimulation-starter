# Model Card: VibeFinder 1.0

## Model Name
VibeFinder 1.0

## Goal / Task
Suggest the top 5 songs from a catalog that best match a user's taste profile based on genre, mood, and energy level.

## Data Used
10 songs in CSV format
Features: genre, mood, energy (0.0–1.0), tempo_bpm, valence, danceability, acousticness
Limitation: small dataset with heavy representation of lofi and pop genres

## Algorithm Summary
Each song is scored against the user's preferences:
Genre match adds 2.0 points
Mood match adds 1.0 point
Energy proximity adds up to 1.5 points based on how close the song's energy is to the user's target

Songs are then sorted by score and the top k results are returned with explanations.

## Observed Behavior / Biases
The system strongly favors genre matches due to the highest weight. Songs outside the user's preferred genre rarely appear in top results even if they match mood and energy well.
The dataset is small and lacks diversity — genres like classical, R&B, and country are completely absent, so users with those preferences will get poor results.
 A filter bubble effect is likely: users will keep seeing the same 1-2 genres repeatedly.

## Evaluation Process
Tested with three profiles: High-Energy Pop, Chill Lofi, and Deep Intense Rock. Each profile returned sensible top results. The Chill Lofi profile showed the strongest genre dominance — all top 3 results were lofi regardless of other attributes.

## Intended Use
Educational simulation to demonstrate how content-based filtering works. Suitable for learning purposes only.

## Non-Intended Use
Not suitable for real music discovery. Should not be used to make actual playlist recommendations for real users.

## Ideas for Improvement
1. Add more songs across more genres to reduce bias
2. Let users adjust the weights themselves
3. Add a diversity penalty so the same genre cannot dominate the top 5

## Personal Reflection
My biggest learning moment in this project was realizing that a recommendation system is really just math — scoring and sorting. Using weighted rules made it clear why genre dominates the results. AI tools helped me structure the scoring logic quickly, but I had to double-check the CSV parsing since the delimiter caused a key error at first. What surprised me was how "real" the recommendations felt even with only 10 songs and 3 simple rules. If I extended this project I would add more songs, more genres, and let users tune the weights themselves.