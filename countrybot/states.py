from telebot.asyncio_handler_backends import State, StatesGroup


class Search(StatesGroup):
    search = State()
    country = State()
    name = State()
    code = State()
    capital = State()
    currency = State()
    language = State()
    calling_code = State()
    selection = State()
