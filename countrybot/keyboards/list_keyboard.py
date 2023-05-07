from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def list_keyboard(data: list, key: str) -> InlineKeyboardMarkup:
    keyboard = [[InlineKeyboardButton(item, callback_data=f'{key}:{item}')] for item in data]
    return InlineKeyboardMarkup(keyboard=keyboard)
