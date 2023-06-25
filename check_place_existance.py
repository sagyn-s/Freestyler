import os

import requests
from dotenv import load_dotenv

load_dotenv()

HERE_API_KEY = os.getenv("HERE_API_KEY")


def check_place_existence(place):
    API_KEY = HERE_API_KEY
    base_url = 'https://geocode.search.hereapi.com/v1/geocode'
    request_url = f"{base_url}?q={place}&apiKey={API_KEY}"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        items = data.get('items', [])
        return len(items) > 0
    else:
        print(f"An error occurred: {response.status_code}")
        return False
