from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def search_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Search By Name', callback_data='search_by_name'),
            InlineKeyboardButton('Search By Code', callback_data='search_by_code')
        ],
        [
            InlineKeyboardButton('Search By Capital', callback_data='search_by_capital'),
            InlineKeyboardButton('Search By Currency', callback_data='search_by_currency')
        ],
        [
            InlineKeyboardButton('Search By Language', callback_data='search_by_language'),
            InlineKeyboardButton('Search By Calling Code', callback_data='search_by_calling_code')
        ],
        [
            InlineKeyboardButton('Search By Selection', callback_data='search_by_selection')
        ]
    ]

    return InlineKeyboardMarkup(keyboard=keyboard)
