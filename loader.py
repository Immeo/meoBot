from aiogram import Bot, Dispatcher, types

from data import config

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)