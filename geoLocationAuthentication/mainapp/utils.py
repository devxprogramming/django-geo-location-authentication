import geocoder
from dotenv import load_dotenv
import requests
load_dotenv()
import os





def get_client_ip():
    endpoint = requests.get(f"https://api.ip2location.io/?key={os.getenv('API_KEY')}&ip=196.201.4.246")
    ip_address = endpoint.json()['ip']
    longitude = endpoint.json()['longitude']
    latitude = endpoint.json()['latitude']

    dict_format = {
        'ip_address': ip_address,
        'longitude': longitude,
        'latitude': latitude
    }
    print(dict_format)

    return dict_format

get_client_ip()

