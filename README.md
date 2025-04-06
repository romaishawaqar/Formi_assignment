Thought Process & Problem Breakdown

When I first read the problem statement — “Find the nearest property based on a user’s location, even with spelling errors or vague inputs like state names” — my initial thought was to tackle it in stages:
1. Input Understanding: The user might input incorrect or partial location names, so some kind of fuzzy correction would be essential.
2. Geolocation Resolution: Once we have the corrected location, we need accurate latitude and longitude data.
3. Proximity Filtering: Compare this geolocation with all available properties and return only those within a certain radius.
4. Flexibility for Broader Inputs: For broader terms like state names, the radius should expand to catch nearby cities.
   
Breaking it down this way helped modularize the backend — with individual utilities for geocoding, distance calculation, and fuzzy string correction.

Tools, Libraries, and Resources Used-

Flask – for building the lightweight REST API quickly.
Pandas – to load and manage property data from a CSV file.
Geopy / geocode API – to convert location names into latitude/longitude.
Haversine Formula – implemented for accurate distance calculation between two coordinates.
FuzzyWuzzy – to handle typos and incorrect spellings in user queries.
Postman – to test API endpoints during development.

These tools were selected for their ease of integration and flexibility. Flask allowed rapid development, while FuzzyWuzzy stood out for its ability to handle minor spelling mistakes — an essential feature in this context.

Key Challenge & How I Solved It

One major challenge was handling user input that was either incorrect (e.g., “sissuu” instead of “Sissu”). Initial fuzzy matching failed for small villages or typos, and geocoding state names often returned coordinates too far from any known property.
To address this, I:
Introduced a two-tier search radius: 50km for precise city-level queries and 150km for broader queries (like states).
Enhanced fuzzy logic to tolerate missing or swapped characters using a combination of Levenshtein distance and scoring thresholds.
Implemented fallback behavior to return the nearest property in the state, even if no exact match was found.

This made the API far more forgiving and user-friendly.

Future Improvements
If I had more time, I'd explore:

Machine Learning Spell Correction: Going beyond fuzzy matching, using a trained model to better infer user intent.
Reverse Geocoding: To convert property coordinates back into readable locations dynamically for better UX.
Clustering & Caching: For large datasets, grouping properties geographically and caching results would enhance performance.
Autocomplete Suggestions: To reduce errors from the user side and make the interface more intuitive.

