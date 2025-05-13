from aiogram import types
from aiogram.fsm.context import FSMContext
from states import Form
from keyboards import language_keyboard
from database import add_word_to_db

async def cmd_add_word_start(message: types.Message, state: FSMContext):
    await message.answer("В какой язык добавить слово?", reply_markup=language_keyboard())
    await state.set_state(Form.choosing_language_for_word)

async def process_language_for_word(message: types.Message, state: FSMContext):
    language = message.text.lower()
    if language not in ["английский", "немецкий", "французский"]:
        await message.answer("Пожалуйста, выберите язык из кнопок.")
        return
    await state.update_data(language=language)
    await message.answer(f"Введите слово на {language}:")
    await state.set_state(Form.adding_word_en)

async def process_word_en(message: types.Message, state: FSMContext):
    word = message.text.strip()
    await state.update_data(word=word)
    await message.answer(f"Введите перевод слова '{word}':")
    await state.set_state(Form.adding_word_ru)

async def process_word_ru(message: types.Message, state: FSMContext):
    data = await state.get_data()
    language = data.get("language")
    word = data.get("word")
    translation = message.text.strip()
    user_id = message.from_user.id

    add_word_to_db(user_id=user_id, language=language, word=word, translation=translation)

    await message.answer(f"Слово '{word}' с переводом '{translation}' добавлено в словарь ({language}).")
    await state.clear()
