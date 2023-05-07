from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def country_data_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Flag', callback_data='country:flag'),
            InlineKeyboardButton('Coat Of Arms', callback_data='country:coat_of_arms')
        ],
        [
            InlineKeyboardButton('Borders', callback_data='country:borders'),
            InlineKeyboardButton('Population', callback_data='country:population')
        ],
        [
            InlineKeyboardButton('Back', callback_data='back_to_search')
        ]
    ]

    return InlineKeyboardMarkup(keyboard=keyboard)
