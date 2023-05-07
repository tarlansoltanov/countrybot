import logging

from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, CallbackQuery

from countrybot.keyboards import list_keyboard
from countrybot.utils import get_country_population_options

async def country_population(call: CallbackQuery, bot: AsyncTeleBot):
    async with bot.retrieve_data(call.from_user.id) as data:
        country = data['country']
    
    logging.info(f'User {call.from_user.id} selected showing population options of the country : {country["name"]["common"]}')

    await bot.edit_message_text(f'Current Population of {country["name"]["common"]}: {country["population"]}\n', call.from_user.id, call.message.message_id, reply_markup=list_keyboard(get_country_population_options(), 'country', 1))