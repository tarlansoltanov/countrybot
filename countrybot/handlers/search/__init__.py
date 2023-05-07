from .by_name import search_by_name, get_by_name
from .by_code import search_by_code, get_by_code
from .by_capital import search_by_capital, get_by_capital
from .by_language import search_by_language, get_by_language
from .by_selection import search_by_selection, select_subregion, select_country, get_by_selection

from telebot.async_telebot import AsyncTeleBot

from countrybot.states import Search


def register_search_handlers(bot: AsyncTeleBot):
    bot.register_callback_query_handler(search_by_name, lambda call: call.data == 'search_by_name', pass_bot=True)
    bot.register_message_handler(get_by_name, state=Search.name, pass_bot=True)

    bot.register_callback_query_handler(search_by_code, lambda call: call.data == 'search_by_code', pass_bot=True)
    bot.register_message_handler(get_by_code, state=Search.code, pass_bot=True)

    bot.register_callback_query_handler(search_by_capital, lambda call: call.data == 'search_by_capital', pass_bot=True)
    bot.register_message_handler(get_by_capital, state=Search.capital, pass_bot=True)

    bot.register_callback_query_handler(search_by_language, lambda call: call.data ==
                                        'search_by_language', pass_bot=True)
    bot.register_message_handler(get_by_language, state=Search.language, pass_bot=True)

    bot.register_callback_query_handler(search_by_selection, lambda call: call.data ==
                                        'search_by_selection', pass_bot=True)
    bot.register_callback_query_handler(select_subregion, lambda call: call.data.startswith('region:'), pass_bot=True)
    bot.register_callback_query_handler(select_country, lambda call: call.data.startswith('subregion:'), pass_bot=True)
    bot.register_callback_query_handler(get_by_selection, lambda call: call.data.startswith('selected:'), pass_bot=True)
