from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def population_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("Total Population Graph", callback_data='population:total')],
        [InlineKeyboardButton("Men Population Graph", callback_data='population:men')],
        [InlineKeyboardButton("Women Population Graph", callback_data='population:women')],
        [InlineKeyboardButton('Back', callback_data='back_to_country')]
    ]

    return InlineKeyboardMarkup(keyboard=keyboard)
