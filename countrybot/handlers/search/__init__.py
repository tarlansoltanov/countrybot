from .by_name import search_by_name, get_by_name
from .by_code import search_by_code, get_by_code
from .by_capital import search_by_capital, get_by_capital

from telebot.async_telebot import AsyncTeleBot

from countrybot.states import Search


def register_search_handlers(bot: AsyncTeleBot):
    bot.register_callback_query_handler(search_by_name, lambda call: call.data == 'search_by_name', pass_bot=True)
    bot.register_message_handler(get_by_name, state=Search.name, pass_bot=True)

    bot.register_callback_query_handler(search_by_code, lambda call: call.data == 'search_by_code', pass_bot=True)
    bot.register_message_handler(get_by_code, state=Search.code, pass_bot=True)

    bot.register_callback_query_handler(search_by_capital, lambda call: call.data == 'search_by_capital', pass_bot=True)
    bot.register_message_handler(get_by_capital, state=Search.capital, pass_bot=True)
