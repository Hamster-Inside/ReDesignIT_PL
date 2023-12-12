from os import getenv
from dotenv import load_dotenv
import requests
from .data_log import simple_log


def get_user_location_data(user_ip):
    load_dotenv()
    # api_key = getenv('IPSTACK_API_KEY') # ipstack less accurate info
    api_key = getenv('IPINFO_API_KEY')
    # api_url = f'http://api.ipstack.com/{user_ip}?access_key={api_key}'
    api_url = f'ipinfo.io/{user_ip}?token={api_key}'
    loc_data = {}
    try:
        response = requests.get(api_url)
    except requests.exceptions.RequestException as e:
        response = None
        simple_log(f'Problem with trying to get api_url = http://api.ipstack.com/{user_ip}')

    data = response.json()
    to_get_data = ['continent_name', 'country_name', 'city']
    for item in to_get_data:
        loc_data[item] = data.get(item, "Not Found") if data.get(item) is not None else "Not Found"
    return loc_data
