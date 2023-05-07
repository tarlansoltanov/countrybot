from telebot import asyncio_filters
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_storage import StateMemoryStorage

from decouple import config


bot = AsyncTeleBot(config('BOT_TOKEN'), state_storage=StateMemoryStorage())
