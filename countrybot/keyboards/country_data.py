from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def country_data_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Borders', callback_data='borders'),
            InlineKeyboardButton('Population', callback_data='population')
        ],
        [
            InlineKeyboardButton('Back', callback_data='back_to_search')
        ]
    ]

    return InlineKeyboardMarkup(keyboard=keyboard)
