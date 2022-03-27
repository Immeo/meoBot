from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('1'),
            KeyboardButton('2'),
        ],
        [
            KeyboardButton('3'),
        ],
        [
            KeyboardButton('test1'),
            KeyboardButton('test2'),
        ]
    ],
    resize_keyboard=True
)