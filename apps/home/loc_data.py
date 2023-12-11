from os import getenv
from dotenv import load_dotenv
import json
import requests


def get_user_location_data(user_ip):
    load_dotenv()
    api_key = getenv('IPSTACK_API_KEY')
    api_url = f'http://api.ipstack.com/{user_ip}?access_key={api_key}'
    loc_data = {}
    try:
        response = requests.get(api_url)
    except requests.exceptions.RequestException as e:
        response = None
        # TODO log the error after

    data = response.json()

    if is_valid_json(data):
        to_get_data = ['continent_name', 'country_name', 'city']
        for item in to_get_data:
            loc_data[item] = data.get(item, "Not Found")
    return loc_data


def is_valid_json(json_data):
    try:
        json_object = json.loads(json_data)
        return True
    except json.JSONDecodeError:
        return False
