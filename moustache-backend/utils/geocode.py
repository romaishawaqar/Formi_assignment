from geopy.geocoders import Nominatim

def get_lat_lng(location):
    geolocator = Nominatim(user_agent="moustache_locator")
    loc = geolocator.geocode(location)
    if loc:
        return (loc.latitude, loc.longitude)
    return None
