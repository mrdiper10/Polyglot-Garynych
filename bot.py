import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from config import API_TOKEN
from database import init_db
from states import Form
from handlers import start, words, menu, grammar, grammar_german, grammar_french

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=API_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    init_db()

    # Регистрация обработчиков команд /start
    dp.message.register(start.cmd_start, Command(commands=['start']))

    # Регистрация обработчиков добавления слов с выбором языка
    dp.message.register(words.cmd_add_word_start, lambda message: message.text == "Добавить слова")
    dp.message.register(words.process_language_for_word, Form.choosing_language_for_word)
    dp.message.register(words.process_word_en, Form.adding_word_en)
    dp.message.register(words.process_word_ru, Form.adding_word_ru)

    # Регистрация обработчиков меню
    dp.message.register(menu.cmd_show_dictionary, lambda message: message.text == "Показать словарь")
    dp.message.register(menu.cmd_clear_dictionary, lambda message: message.text == "Очистить словарь")
    dp.message.register(menu.cmd_progress, lambda message: message.text == "Мой прогресс")
    dp.message.register(menu.cmd_help, lambda message: message.text == "Помощь")

    # Регистрация обработчиков изучения правил
    dp.message.register(menu.cmd_grammar, lambda message: message.text == "Изучение правил (англ.)")
    dp.message.register(grammar.show_rule, lambda message: message.text.isdigit())

    dp.message.register(menu.cmd_grammar_german, lambda message: message.text == "Изучение правил (нем.)")
    dp.message.register(grammar_german.show_rule_german, lambda message: message.text.isdigit())

    dp.message.register(menu.cmd_grammar_french, lambda message: message.text == "Изучение правил (фр.)")
    dp.message.register(grammar_french.show_rule_french, lambda message: message.text.isdigit())

    # Обработчик команды /menu для выхода в главное меню из любого состояния
    dp.message.register(menu.cmd_menu, Command(commands=['menu']))

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
