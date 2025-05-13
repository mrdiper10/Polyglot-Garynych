from aiogram import types
from aiogram.fsm.context import FSMContext
from database import get_words, get_words_count_by_language, clear_user_dictionary
from keyboards import main_menu_keyboard
from handlers import grammar, grammar_german, grammar_french, words

async def cmd_menu(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Главное меню:", reply_markup=main_menu_keyboard())

async def cmd_add_words(message: types.Message, state: FSMContext):
    await words.cmd_add_word_start(message, state)

async def cmd_show_dictionary(message: types.Message):
    user_id = message.from_user.id
    words = get_words(user_id)
    if not words:
        await message.answer("Твой словарь пуст.")
        return

    msg = "Твой словарь:\n\n"
    for lang in ["английский", "немецкий", "французский"]:
        msg += f"--- {lang.title()} ---\n"
        lang_words = [w for w in words if w[2] == lang]  # предполагается, что язык в 3-м элементе
        if not lang_words:
            msg += "Слов нет.\n"
            continue
        for word, translation, language, known in lang_words:
            if translation:
                msg += f"{word} - {translation}\n"
            else:
                msg += f"{word} - [нет перевода]\n"
        msg += "\n"

    await message.answer(msg)

async def cmd_clear_dictionary(message: types.Message):
    user_id = message.from_user.id
    clear_user_dictionary(user_id)
    await message.answer("Твой словарь успешно очищен.")

async def cmd_progress(message: types.Message):
    user_id = message.from_user.id
    languages = ["английский", "немецкий", "французский"]
    texts = []
    for lang in languages:
        total, known = get_words_count_by_language(user_id, lang)
        if total == 0:
            texts.append(f"{lang.title()}: словарь пуст.")
        else:
            percent = (known / total) * 100
            texts.append(f"{lang.title()}: {known} из {total} слов выучено ({percent:.1f}%)")
    await message.answer("\n".join(texts))

async def cmd_help(message: types.Message):
    help_text = (
        "📚 *Команды бота:*\n\n"
        "• Добавить слова - добавить новые слова в словарь. Сначала выберите язык, затем введите слово и перевод.\n"
        "• Показать словарь - посмотреть все слова в вашем словаре по каждому языку.\n"
        "• Очистить словарь - удалить все слова из вашего словаря.\n"
        "• Мой прогресс - узнать, сколько слов выучено по каждому языку отдельно.\n"
        "• Изучение правил (англ.) - грамматические уроки по английскому языку.\n"
        "• Изучение правил (нем.) - грамматические уроки по немецкому языку.\n"
        "• Изучение правил (фр.) - грамматические уроки по французскому языку.\n"
        "• /start - начать заново и получить главное меню.\n"
        "• /menu - вернуться в главное меню из любого состояния.\n\n"
        "Если у тебя есть вопросы или предложения, пиши сюда!"
    )
    await message.answer(help_text, parse_mode="Markdown")

async def cmd_grammar(message: types.Message):
    await grammar.grammar_menu(message)

async def cmd_grammar_german(message: types.Message):
    await grammar_german.grammar_menu_german(message)

async def cmd_grammar_french(message: types.Message):
    await grammar_french.grammar_menu_french(message)
