from telebot.async_telebot import AsyncTeleBot

from .start import start
from .search import register_search_handlers


def register_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(start, commands=['start'], pass_bot=True)

    register_search_handlers(bot)
