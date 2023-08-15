import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv(".env")
token = os.getenv("TOKEN")

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def main():
    """Start the bot and handlers"""
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
