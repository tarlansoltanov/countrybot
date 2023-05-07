from telebot.asyncio_handler_backends import State, StatesGroup


class Search(StatesGroup):
    search = State()
    country = State()
    name = State()
    code = State()
    capital = State()
    language = State()
    selection = State()
