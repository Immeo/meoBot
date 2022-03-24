from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from data.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def getMsg(message: types.message):
    chatId = message.chat.id
    text = message.text + f' {message.from_user.full_name}'

    await message.answer(text)
    print(text)

executor.start_polling(dp)