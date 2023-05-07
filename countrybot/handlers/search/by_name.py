import logging

from telebot.async_telebot import AsyncTeleBot
from telebot.types import CallbackQuery, Message

from countrybot.states import Search
from countrybot.keyboards import country_data_keyboard
from countrybot.utils import get_country_by_name, get_country_data


async def search_by_name(call: CallbackQuery, bot: AsyncTeleBot):
    logging.info(f'User {call.from_user.id} selected search by name.')

    await bot.edit_message_text('Enter the name of the country:', call.from_user.id, call.message.message_id)
    await bot.set_state(call.from_user.id, Search.name, call.message.chat.id)


async def get_by_name(message: Message, bot: AsyncTeleBot):
    logging.info(f'User {message.from_user.id} entered country name: {message.text}.')

    try:
        country = get_country_by_name(message.text)
    except ValueError:
        await bot.send_message(message.chat.id, 'Country not found.')
        await bot.send_message(message.chat.id, 'Enter the name of the country:')
        return

    await bot.send_message(message.chat.id, get_country_data(country), reply_markup=country_data_keyboard())
    await bot.set_state(message.from_user.id, Search.country, message.chat.id)
    await bot.add_data(message.from_user.id, country)
