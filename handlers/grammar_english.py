from aiogram import types
from aiogram.fsm.context import FSMContext
from rulesenglish import rules
from states import Form

async def grammar_menu(message: types.Message, state: FSMContext):
    await state.set_state(Form.learning_english)
    text = "📚 *Правила английского языка:*\n\n"
    for i, rule in enumerate(rules, 1):
        text += f"{i}. {rule['title']}\n"
    text += "\nВведите номер правила, чтобы узнать подробности, или /menu для возврата в меню."
    await message.answer(text, parse_mode="Markdown")

async def show_rule(message: types.Message, state: FSMContext):
    try:
        num = int(message.text.strip())
        if 1 <= num <= len(rules):
            rule = rules[num - 1]
            text = f"*{rule['title']}*\n\n{rule['body']}"
            if 'tasks' in rule and rule['tasks']:
                text += "\n\n*Задания:*\n"
                for t in rule['tasks']:
                    text += f"- {t}\n"
            await message.answer(text, parse_mode="Markdown")
            if "image" in rule and rule["image"]:
                await message.answer_photo(rule["image"])
        else:
            await message.answer("Такого номера нет. Введите номер из списка или /menu.")
    except ValueError:
        await message.answer("Введите номер правила или /menu.")