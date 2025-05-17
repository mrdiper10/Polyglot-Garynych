from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    choosing_language_for_word = State()
    adding_word_en = State()
    adding_word_ru = State()
    learning_english = State()  # Новое состояние для английских правил
    learning_german = State()   # Новое состояние для немецких правил
    learning_french = State()   # Новое состояние для французских правил