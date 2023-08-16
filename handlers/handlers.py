from aiogram import Dispatcher, types

import weather_api


async def get_day_weather(message: types.Message):
    weather = weather_api.get_current_weather_dict(message.text)
    location = weather_api.get_location(message.text)
    location_name = location.raw["display_name"]
    city_weather = "\n".join(f"*{key}:* {value}" for key, value in weather.items())

    await message.answer(
        f"*Погода в городе {location_name}*\n" + city_weather,
        parse_mode="Markdown"
    )


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(get_day_weather)