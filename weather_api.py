import os
from dotenv import load_dotenv
from typing import Any
from geopy.geocoders import Nominatim

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


def get_location(city_name: str) -> Any:
    """Take a city name and return city name and country"""
    geolocator = Nominatim(user_agent="weather_bot")
    return geolocator.geocode(city_name)
    

def get_lat(location):
    return f"{location.latitude: .2f}"


def get_lon(location):
    return f"{location.longitude: .2f}"
