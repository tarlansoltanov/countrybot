from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def back_keyboard(type : int = 0) -> InlineKeyboardMarkup:
    keyboard = []
    if type == 1:
        keyboard.append([InlineKeyboardButton('Back', callback_data='back_to_country')])
    elif type == 2:
        keyboard.append([InlineKeyboardButton('Back', callback_data='back_to_search')])
    return InlineKeyboardMarkup(keyboard=keyboard)
