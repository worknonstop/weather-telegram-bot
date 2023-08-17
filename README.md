# Weather Telegram Bot
This telegram bot shows the current weather and weather forecast for 5 days using OpenWeatherMap API

## Requirements
- python = "^3.8"
- poetry = "^1.3.2"

## Preparation

To use the bot, you will need to register and get a free API key at openweathermap.org.
The bot uses primitive access for the administrator by his telegram user id.

## Installation and Setup

1. **Clone the repository:**
```bash
git clone git@github.com:worknonstop/weather-telegram-bot.git
```
2. **Install dependencies using Poetry:**
```bash
poetry install
```
3. **Create a `.env` file at the root of the project and set values ​​for constants:**
- TOKEN - telegram bot token
- ADMIN_IDS - user id to which the bot will be available
- API_KEY - key provided by openweatherapi

4. **Run the bot:**
```bash
poetry run python bot.py
```

5. **Usage:**  
Write the name of the city or country to get the current weather.
Along with the message, a button will appear to receive a 5-day weather forecast.