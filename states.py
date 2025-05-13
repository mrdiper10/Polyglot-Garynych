from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    choosing_language_for_word = State()
    adding_word_en = State()
    adding_word_ru = State()
