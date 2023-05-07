import logging

from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, CallbackQuery

from countrybot.keyboards import back_keyboard


async def country_coa(call: CallbackQuery, bot: AsyncTeleBot):
    async with bot.retrieve_data(call.from_user.id) as data:
        country = data['country']

    logging.info(f'User {call.from_user.id} selected showing coat of arms of the country : {country["name"]["common"]}')

    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(call.from_user.id, country['coatOfArms']['png'], f'Coat Of Arms Of {country["name"]["common"]}', reply_markup=back_keyboard(1))
    