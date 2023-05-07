import logging

from telebot.types import Message
from telebot.async_telebot import AsyncTeleBot

from countrybot.keyboards import search_menu_keyboard


async def start(message: Message, bot: AsyncTeleBot):
    logging.info(f'User {message.from_user.id} started bot.')

    await bot.reply_to(message, 'Welcome to Country Information Bot! \nTo get started, select the search method:', reply_markup=search_menu_keyboard())
