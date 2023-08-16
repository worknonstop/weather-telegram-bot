import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from aiogram.utils import executor

from handlers.weather_handlers import register_handlers

load_dotenv(".env")
token = os.getenv("TOKEN")

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def main(dp: Dispatcher):
    """Start the bot and handlers"""
    register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=main)
