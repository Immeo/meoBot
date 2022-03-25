from aiogram import types

async def set_commands(dp):
    types.BotCommand('start', 'Запуск бота'),
    types.BotCommand('help', ' Помощь')