import logging

from telebot.async_telebot import AsyncTeleBot
from telebot.types import CallbackQuery

from countrybot.states import Search


async def search_by_name(call: CallbackQuery, bot: AsyncTeleBot):
    logging.info(f'User {call.from_user.id} selected search by name.')

    await bot.edit_message_text('Enter the name of the country:', call.from_user.id, call.message.message_id)
    await bot.set_state(call.from_user.id, Search.name, call.message.chat.id)
