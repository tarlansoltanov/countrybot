from telebot.async_telebot import AsyncTeleBot

from .start import start
from .search import search_by_name


def register_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(start, commands=['start'], pass_bot=True)

    bot.register_callback_query_handler(search_by_name, lambda call: call.data == 'search_by_name', pass_bot=True)
