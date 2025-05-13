from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards import main_menu_keyboard

async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    welcome_text = (
        "Привет! Этот бот поможет тебе изучать английский, немецкий и французский языки.\n"
        "Ты можешь добавлять слова, просматривать словарь, изучать грамматические правила и отслеживать прогресс.\n\n"
        "Выбери действие в меню ниже."
    )
    await message.answer(welcome_text, reply_markup=main_menu_keyboard())
