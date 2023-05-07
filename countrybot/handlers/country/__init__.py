from .borders import country_borders
from .flag import country_flag

from telebot.async_telebot import AsyncTeleBot

from countrybot.states import Search

def register_country_handlers(bot: AsyncTeleBot):
    bot.register_callback_query_handler(country_borders, lambda call: call.data == 'country:borders', pass_bot=True)
    bot.register_callback_query_handler(country_flag, lambda call: call.data == 'country:flag', pass_bot=True)