from .by_name import search_by_name, get_by_name

from telebot.async_telebot import AsyncTeleBot

from countrybot.states import Search


def register_search_handlers(bot: AsyncTeleBot):
    bot.register_callback_query_handler(search_by_name, lambda call: call.data == 'search_by_name', pass_bot=True)

    bot.register_message_handler(get_by_name, state=Search.name, pass_bot=True)
