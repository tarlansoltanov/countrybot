from telebot.async_telebot import AsyncTeleBot

from .start import start


def register_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(start, commands=['start'], pass_bot=True)
