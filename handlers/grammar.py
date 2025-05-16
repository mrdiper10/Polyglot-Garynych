from aiogram import types
from aiogram.fsm.context import FSMContext

rules = [
    {
        "title": "Артикль a/an",
        "body": "Артикль a/an используется с исчисляемыми существительными в единственном числе. A - перед согласным звуком, an - перед гласным звуком.",
        "tasks": [
            "Вставьте a или an: ___ apple, ___ book, ___ orange, ___ cat.",
            "Переведите на английский: 'У меня есть книга.'"
        ]
    },
    # ... остальные правила
]

async def grammar_menu(message: types.Message):
    text = "📚 *Правила английского языка:*\n\n"
    for i, rule in enumerate(rules, start=1):
        text += f"{i}. {rule['title']}\n"
    text += "\nВведите номер правила, чтобы узнать подробности, или /menu для возврата в меню."
    await message.answer(text, parse_mode="Markdown")

async def show_rule(message: types.Message, state: FSMContext):
    try:
        num = int(message.text.strip())
        if 1 <= num <= len(rules):
            rule = rules[num - 1]
            await message.answer(f"*{rule['title']}*\n\n{rule['body']}", parse_mode="Markdown")
            # Не отправляем фото!
        else:
            await message.answer("Такого номера нет. Введите номер из списка или /menu.")
    except ValueError:
        await message.answer("Введите номер правила или /menu.")

async def show_tasks(message: types.Message, state: FSMContext):
    try:
        num = int(message.text.strip())
        if 1 <= num <= len(rules):
            tasks = rules[num - 1].get("tasks", [])
            if not tasks:
                await message.answer("Для этого правила задания не заданы.")
                return
            text = f"📝 *Задания к правилу {num} - {rules[num - 1]['title']}:*\n\n"
            text += "\n".join(f"{i+1}. {task}" for i, task in enumerate(tasks))
            await message.answer(text, parse_mode="Markdown")
        else:
            await message.answer("Такого номера нет. Введите номер из списка или /menu.")
    except ValueError:
        await message.answer("Введите номер правила или /menu.")
