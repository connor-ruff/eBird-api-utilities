import requests
import json 

with open('manual_scripts/api_key_file.json', 'r') as f:
    api_key_data = json.load(f)
API_KEY = api_key_data['ebird_api_key']

BASE_URL = "https://api.ebird.org/v2"

headers = {
    "X-eBirdApiToken": API_KEY
}

url = f"{BASE_URL}/ref/taxonomy/ebird?fmt=json"

response = requests.get(url, headers=headers)
resp_json = response.json()
with open('manual_scripts/outputs/taxonomy_ref.json', 'w') as f:
    json.dump(resp_json, f, indent=2)