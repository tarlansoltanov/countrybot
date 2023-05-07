from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def country_data_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Flag', callback_data='country:flag'),
            InlineKeyboardButton('Coat Of Arms', callback_data='population')
        ],
        [
            InlineKeyboardButton('Borders', callback_data='borders'),
            InlineKeyboardButton('Population', callback_data='population')
        ],
        [
            InlineKeyboardButton('Back', callback_data='back_to_search')
        ]
    ]

    return InlineKeyboardMarkup(keyboard=keyboard)
