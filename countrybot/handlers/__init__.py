from telebot.async_telebot import AsyncTeleBot

from .start import start
from .back import back_to_search, back_to_country
from .search import register_search_handlers


def register_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(start, commands=['start'], pass_bot=True)

    bot.register_callback_query_handler(back_to_search, func=lambda call: call.data == 'back_to_search', pass_bot=True)
    bot.register_callback_query_handler(back_to_country, func=lambda call: call.data == 'back_to_country', pass_bot=True)

    register_search_handlers(bot)
