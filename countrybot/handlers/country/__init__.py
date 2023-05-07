from .borders import country_borders
from .flag import country_flag
from .coat_of_arms import country_coa
from .population import country_population, total_population

from telebot.async_telebot import AsyncTeleBot

from countrybot.states import Search

def register_country_handlers(bot: AsyncTeleBot):
    bot.register_callback_query_handler(country_borders, lambda call: call.data == 'country:borders', pass_bot=True)
    bot.register_callback_query_handler(country_flag, lambda call: call.data == 'country:flag', pass_bot=True)
    bot.register_callback_query_handler(country_coa, lambda call: call.data == 'country:coat_of_arms', pass_bot=True)
    bot.register_callback_query_handler(country_population, lambda call: call.data == 'country:population', pass_bot=True)
    bot.register_callback_query_handler(total_population, lambda call: call.data == 'population:total', pass_bot=True)
