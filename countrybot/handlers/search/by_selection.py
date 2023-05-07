import logging

from telebot.async_telebot import AsyncTeleBot
from telebot.types import CallbackQuery, Message

from countrybot.states import Search
from countrybot.keyboards import list_keyboard, country_data_keyboard
from countrybot.utils import get_regions, get_subregions, get_countries_by_subregion, get_country_by_name, get_country_data


async def search_by_selection(call: CallbackQuery, bot: AsyncTeleBot):
    logging.info(f'User {call.from_user.id} selected search by selection.')

    await bot.edit_message_text('Select a Region:', call.from_user.id, call.message.message_id, reply_markup=list_keyboard(get_regions(), 'region'))
    await bot.set_state(call.from_user.id, Search.selection, call.message.chat.id)


async def select_subregion(call: CallbackQuery, bot: AsyncTeleBot):
    logging.info(f'User {call.from_user.id} selected Region: {call.data.split(":")[1]}.')

    await bot.edit_message_text('Select a Subregion:', call.from_user.id, call.message.message_id, reply_markup=list_keyboard(get_subregions(call.data.split(':')[1]), 'subregion'))
    await bot.set_state(call.from_user.id, Search.region, call.message.chat.id)

async def select_country(call: CallbackQuery, bot: AsyncTeleBot):
    logging.info(f'User {call.from_user.id} selected Subregion: {call.data.split(":")[1]}.')

    await bot.edit_message_text('Select a Country:', call.from_user.id, call.message.message_id, reply_markup=list_keyboard(get_countries_by_subregion(call.data.split(':')[1]), 'selected'))
    await bot.set_state(call.from_user.id, Search.subregion, call.message.chat.id)


async def get_by_selection(call: CallbackQuery, bot: AsyncTeleBot):
    logging.info(f'User {call.from_user.id} selected country name: {call.data.split(":")[1]}.')

    country = get_country_by_name(call.data.split(":")[1])

    await bot.edit_message_text(get_country_data(country), call.from_user.id, call.message.message_id, reply_markup=country_data_keyboard())
    await bot.set_state(call.from_user.id, Search.country, call.message.chat.id)

    async with bot.retrieve_data(call.from_user.id) as data:
        data['country'] = country
