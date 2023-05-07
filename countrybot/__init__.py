from decouple import config

from telebot import asyncio_filters
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_storage import StateMemoryStorage

from countrybot.handlers import register_handlers


bot = AsyncTeleBot(config('BOT_TOKEN'), state_storage=StateMemoryStorage())

bot.add_custom_filter(asyncio_filters.StateFilter(bot))

register_handlers(bot)
