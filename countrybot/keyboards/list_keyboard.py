from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def list_keyboard(data: list, key: str, back : int = 0) -> InlineKeyboardMarkup:
    keyboard = [[InlineKeyboardButton(item, callback_data=f'{key}:{item}')] for item in data]
    if back == 1:
        keyboard.append([InlineKeyboardButton('Back', callback_data='back_to_country')])
    elif back == 2:
        keyboard.append([InlineKeyboardButton('Back', callback_data='back_to_search')])
    return InlineKeyboardMarkup(keyboard=keyboard)
