import os
import requests
from datetime import datetime
from typing import Any, Dict, List

from dotenv import load_dotenv
from geopy.geocoders import Nominatim

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


def get_location(city_name: str) -> Any:
    """Take a city name and return city name and country"""
    geolocator = Nominatim(user_agent="weather-telegram-bot")
    return geolocator.geocode(city_name)
    

def get_lat(location):
    """Take the location and return the latitude."""
    return f"{location.latitude:.2f}"


def get_lon(location):
    """Take the location and return the longitude."""
    return f"{location.longitude:.2f}"


def get_today_weather_json(city_name):
    """Take city name and return weather data in json format"""
    location = get_location(city_name)
    lat = get_lat(location)
    lon = get_lon(location)
    ru = "ru"

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&units=metric&lon={lon}&appid={API_KEY}&lang={ru}"
    )
    return weather_data.json()


def get_five_day_weather_json(city_name):
    """Take city name and return json data of 5 day weather forecast"""
    location = get_location(city_name)
    lat = get_lat(location)
    lon = get_lon(location)
    ru = "ru"

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={API_KEY}&lang={ru}"
    )
    return weather_data.json()


def get_current_weather_dict(city_name: str) -> Dict:
    """Return a dictionary with weather indicators"""
    city_data = get_today_weather_json(city_name)

    temp = city_data["main"]["temp"]
    weather = city_data["weather"][0]["description"]
    humidity = city_data["main"]["humidity"]
    wind_speed = city_data["wind"]["speed"]
    pressure = city_data["main"]["pressure"]
    timestamp_sunrise = city_data["sys"]["sunrise"]
    sunrise = datetime.fromtimestamp(timestamp_sunrise)
    timestamp_sunset = city_data["sys"]["sunset"]
    sunset = datetime.fromtimestamp(timestamp_sunset)
    day_length = sunset - sunrise
    hours, _ = divmod(day_length.seconds, 3600)

    weather = {
        "Температура": f"{temp} °C",
        "Тип погоды": f"{weather}",
        "Влажность": f"{humidity}",
        "Скорость ветра": f"{wind_speed} м/с",
        "Атмосферное давление": f"{pressure}",
        "Восход": f"{sunrise}",
        "Закат": f"{sunset}",
        "Продолжительность дня": f"{hours} часов",
    }
    return weather


def get_five_day_weather_list(city_name: str) -> List:
    weather_json = get_five_day_weather_json(city_name)
    day_weather = weather_json["list"]
    twelve_hours = "12:00:00"
    
    all = []
    for day in day_weather:
        if twelve_hours in day["dt_txt"]:
            stage = {
                "Дата": f"{day['dt_txt']}",
                "Температура": f"{day['main']['temp']}",
                "Тип погоды": f"{day['weather'][0]['description']}",
                "Влажность": f"{day['main']['humidity']}",
                "Скорость ветра": f"{day['wind']['speed']}",
                "Атмосферное давление": f"{day['main']['pressure']}"
            }
            all.append(stage)
    return all