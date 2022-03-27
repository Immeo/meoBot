from aiogram import types
from loader import dp

@dp.message_handler(text=types.message.Message.text)
async def button_text(message: types.Message):
    await message.answer(f'Вы ввели {message.text}')
