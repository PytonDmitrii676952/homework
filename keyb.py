from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translations import texts
keyb = ReplyKeyboardMarkup( 
    keyboard=[
        [KeyboardButton(text="RU")],
        [KeyboardButton(text="EN")]
    ],
    resize_keyboard=True
)
def create_menu(language):
    keyb_menu = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=texts[language]["menu"]["install_guide"])],
            [KeyboardButton(text=texts[language]["menu"]["manuals"])],
            [KeyboardButton(text=texts[language]["menu"]["videos"])]
        ],
        resize_keyboard=True
    )
    return keyb_menu
question = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Xoчу добавится в канал",
                callback_data="add_channel"
            )
        ],
        [
            InlineKeyboardButton(
                text="Не хочу добавляться в канал",
                callback_data="no_channel"
            )
        ]
    ],
)
