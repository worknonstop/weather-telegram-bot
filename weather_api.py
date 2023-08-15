import os
import requests

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
    """Take the location and return the latitude."""
    return f"{location.latitude: .2f}"


def get_lon(location):
    """Take the location and return the longitude."""
    return f"{location.longitude: .2f}"


def get_city_data_today(city_name):
    """Take city name and return weather data in json format"""
    location = get_location(city_name)
    lat = get_lat(location)
    lon = get_lon(location)

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&units=metric&lon={lon}&appid={API_KEY}&lang=ru"
    )
    return weather_data.json()