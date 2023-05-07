import logging

from telebot.types import Message, CallbackQuery
from telebot.async_telebot import AsyncTeleBot

from countrybot.keyboards import search_menu_keyboard, country_data_keyboard
from countrybot.states import Search
from countrybot.utils import get_country_data


async def back_to_search(call: CallbackQuery, bot: AsyncTeleBot):
    logging.info(f'User {call.from_user.id} clicked back to search.')

    await bot.reset_data(call.from_user.id)

    await bot.edit_message_text('Select the search method:', call.from_user.id, call.message.message_id, reply_markup=search_menu_keyboard())
    await bot.set_state(call.from_user.id, Search.search, call.message.chat.id)


async def back_to_country(call: CallbackQuery, bot: AsyncTeleBot):
    logging.info(f'User {call.from_user.id} clicked back to country.')

    async with bot.retrieve_data(call.from_user.id) as data:
        country = data['country']
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_message(call.from_user.id, get_country_data(country), reply_markup=country_data_keyboard())
        # await bot.edit_message_text(get_country_data(country), call.from_user.id, call.message.message_id, reply_markup=country_data_keyboard())
        await bot.set_state(call.from_user.id, Search.country, call.message.chat.id)
