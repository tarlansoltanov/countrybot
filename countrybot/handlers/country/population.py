import logging

from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, CallbackQuery

from countrybot.keyboards import population_keyboard, back_keyboard
from countrybot.utils.population import total_population_graph

async def country_population(call: CallbackQuery, bot: AsyncTeleBot):
    async with bot.retrieve_data(call.from_user.id) as data:
        country = data['country']
    
    logging.info(f'User {call.from_user.id} selected showing population options of the country : {country["name"]["common"]}')

    await bot.edit_message_text(f'Current Population of {country["name"]["common"]}: {country["population"]}\n', call.from_user.id, call.message.message_id, reply_markup=population_keyboard())


async def total_population(call: CallbackQuery, bot: AsyncTeleBot):
    async with bot.retrieve_data(call.from_user.id) as data:
        country = data['country']
    
    logging.info(f'User {call.from_user.id} selected showing total population graph of the country : {country["name"]["common"]}')

    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_photo(call.from_user.id, open(total_population_graph(country['cca3']), 'rb'), f'Total Population Graph Of {country["name"]["common"]}', reply_markup=back_keyboard(1))