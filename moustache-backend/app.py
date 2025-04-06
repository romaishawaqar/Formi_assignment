from flask import Flask, request, jsonify
from utils.geocode import get_lat_lng
from utils.distance import calculate_distance
from utils.correct_spelling import correct_location
import pandas as pd

app = Flask(__name__)

# Load property data
df = pd.read_csv("data/properties.csv")
properties = df.to_dict(orient="records")
all_locations = df['location'].tolist()

@app.route('/')
def home():
    return "✅ Moustache Backend API is running! Use `/nearest-properties?q=YourLocation` to get nearby stays."

@app.route('/nearest-properties', methods=['GET'])
def find_nearest_properties():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Missing location query param `q`"}), 400

    # Fuzzy match user input
    matched_location = correct_location(query, all_locations)

    # Use corrected match or original input for geocoding
    location_to_geocode = matched_location if matched_location else query

    # Get coordinates of the input or matched location
    coords = get_lat_lng(location_to_geocode)
    if not coords:
        return jsonify({"error": f"Could not geocode location '{location_to_geocode}'"}), 404

    # Detect if input is likely a state-level query (to increase search radius)
    is_state_level = ' ' in query or query.lower() in [
        'uttar pradesh', 'madhya pradesh', 'rajasthan', 'himachal pradesh', 
        'maharashtra', 'goa', 'kerala', 'tamil nadu', 'karnataka', 'gujarat'
    ]
    search_radius = 150 if is_state_level else 50

    # Find nearby properties
    results = []
    for prop in properties:
        property_coords = (prop['latitude'], prop['longitude'])
        dist = calculate_distance(coords, property_coords)
        if dist <= search_radius:
            results.append({
                "name": prop['property'],
                "location": prop['location'],
                "distance_km": round(dist, 2)
            })

    if results:
        # Sort by distance
        closest = min(results, key=lambda x: x['distance_km'])
        bold_output = f"**Output: Nearest property is {closest['name']} which is {closest['distance_km']} KM away**"
        return jsonify({
            "matched_location": matched_location if matched_location else query,
            "results": results,
            "message": bold_output
        })
    else:
        return jsonify({
            "matched_location": matched_location if matched_location else query,
            "message": "No properties found nearby."
        }), 404


if __name__ == '__main__':
    app.run(debug=True)
