from aiogram.utils.keyboard import ReplyKeyboardBuilder

def language_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Английский")
    builder.button(text="Немецкий")
    builder.button(text="Французский")
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

def main_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Добавить слова")
    builder.button(text="Показать словарь")
    builder.button(text="Очистить словарь")
    builder.button(text="Мой прогресс")
    builder.button(text="Изучение правил (англ.)")
    builder.button(text="Изучение правил (нем.)")
    builder.button(text="Изучение правил (фр.)")
    builder.button(text="Помощь")
    builder.adjust(3, 3)
    return builder.as_markup(resize_keyboard=True)
