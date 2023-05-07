import logging

from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, CallbackQuery

from countrybot.keyboards import list_keyboard
from countrybot.utils import get_country_borders_names

async def country_borders(call: CallbackQuery, bot: AsyncTeleBot):
    async with bot.retrieve_data(call.from_user.id) as data:
        country = data['country']
    
    logging.info(f'User {call.from_user.id} selected showing borders of the country : {country["name"]["common"]}')

    await bot.edit_message_text(f'Borders of {country["name"]["common"]}:\n', call.from_user.id, call.message.message_id, reply_markup=list_keyboard(get_country_borders_names(country), 'selected', 1))