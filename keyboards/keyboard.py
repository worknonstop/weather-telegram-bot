from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_keyboard():
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Прогноз на 5 дней", callback_data="five_days")
    keyboard.add(button)
    return keyboard