import os
import weather_api
from keyboards.keyboard import get_keyboard

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class Weather(StatesGroup):
    city_name = State()


async def get_day_weather(message: types.Message, state: FSMContext):
    """Return message to user with current weather"""
    keyboard = get_keyboard()
    weather = weather_api.get_current_weather_dict(message.text)
    location = weather_api.get_location(message.text)
    location_name = location.raw["display_name"]
    city_weather = "\n".join(f"*{key}:* {value}" for key, value in weather.items())

    await Weather.city_name.set()
    await state.update_data(city_name=message.text)

    await message.answer(
        f"*Погода в городе {location_name}*\n" + city_weather,
        reply_markup=keyboard,
        parse_mode="Markdown"
    )


async def get_five_day_weather(callback: types.CallbackQuery, state: FSMContext):
    """After pressing the button, return to user 5-day weather forecast"""
    from bot import bot

    await bot.answer_callback_query(callback.id)

    state_data = await state.get_data()
    user_message = state_data.get("city_name")
    five_day_forecast = weather_api.get_five_day_weather_list(user_message)
    weather_text = ""
    for elem in five_day_forecast:
        day = "\n".join(f"*{key}:* {value}" for key, value in elem.items())
        weather_text += day + "\n\n"
    await callback.message.answer(weather_text, parse_mode="Markdown")
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(get_day_weather)
    dp.register_callback_query_handler(get_five_day_weather, state=Weather.city_name)