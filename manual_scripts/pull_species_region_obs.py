import requests
import json 

with open('manual_scripts/api_key_file.json', 'r') as f:
    api_key_data = json.load(f)
API_KEY = api_key_data['ebird_api_key']

BASE_URL = "https://api.ebird.org/v2"


headers = {
    "X-eBirdApiToken": API_KEY
}


REGION_CODE = 'US-NJ-003'
SPECIES_CODE = 'baleag'

url = f"{BASE_URL}/data/obs/{REGION_CODE}/recent/{SPECIES_CODE}"

response = requests.get(url, headers=headers)
resp_json = response.json()
with open(f'manual_scripts/outputs/{REGION_CODE}_{SPECIES_CODE}.json', 'w') as f:
    json.dump(resp_json, f, indent=2)