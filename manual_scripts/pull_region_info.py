import requests
import json 

with open('manual_scripts/api_key_file.json', 'r') as f:
    api_key_data = json.load(f)
API_KEY = api_key_data['ebird_api_key']

BASE_URL = "https://api.ebird.org/v2"

headers = {
    "X-eBirdApiToken": API_KEY
}

def list_subregions(region_type: str, parent_region_code: str = "world"):
    """
    List sub-regions of given type under parent_region_code.

    region_type: "country", "subnational1", or "subnational2"
    parent_region_code: 
      - "world" for top-level country list, or
      - a valid country code (for subnational1), or
      - a valid subnational1 code (for subnational2)
    """
    url = f"{BASE_URL}/ref/region/list/{region_type}/{parent_region_code}"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()

# — Get all countries —
countries = list_subregions("country", "world")
print(f"Total countries: {len(countries)}")
with open('manual_scripts/countries.json', 'w') as f:
    json.dump(countries, f, indent=2)

# — For example, get all US states (subnational1) —
states = list_subregions("subnational1", "US")
print("First few US states/subnational1:")
with open('manual_scripts/us_states.json', 'w') as f:
    json.dump(states, f, indent=2)

# — (Optional) For example, get counties (subnational2) in New Jersey state —
nj_counties = list_subregions("subnational2", "US-NJ")
with open('manual_scripts/nj_counties.json', 'w') as f:
    json.dump(nj_counties, f, indent=2)
