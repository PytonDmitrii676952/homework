from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
keyb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📥 Гайд по установке"),
            KeyboardButton(text="📖 Мануалы"),
            KeyboardButton(text="📽️ ВидеоГайды"),
        ],   
    ],
    resize_keyboard=True)