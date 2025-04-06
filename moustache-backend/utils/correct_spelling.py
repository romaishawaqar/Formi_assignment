import Levenshtein

def correct_location(user_input, known_locations):
    user_input = user_input.strip().lower()
    best_match = None
    best_distance = float('inf')

    for loc in known_locations:
        distance = Levenshtein.distance(user_input, loc.lower())
        if distance < best_distance:
            best_distance = distance
            best_match = loc

    # Accept if distance is 2 or less (tolerate 1-2 typos/missing/swapped characters)
    if best_distance <= 2:
        return best_match
    return None
