from aiogram import types
from aiogram.fsm.context import FSMContext
from rules import rules

async def grammar_menu(message: types.Message):
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
            await message.answer(f"*{rule['title']}*\n\n{rule['body']}", parse_mode="Markdown")
            if "image" in rule and rule["image"]:
                await message.answer_photo(rule["image"])
        else:
            await message.answer("Такого номера нет. Введите номер из списка или /menu.")
    except ValueError:
        await message.answer("Введите номер правила или /menu.")
