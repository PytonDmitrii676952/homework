from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translations import texts
keyb = ReplyKeyboardMarkup( 
    keyboard=[
        [KeyboardButton(text="🇷🇺RU")],
        [KeyboardButton(text="🇺🇸EN")]
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
def create_question(language):
    question = InlineKeyboardMarkup(
        inline_keyboard=[
        [
            InlineKeyboardButton(
                text=texts[language]["menu"]["add_channel"],
                callback_data="add_channel"
            )
        ],
        [
            InlineKeyboardButton(
                text=texts[language]["menu"]["no_channel"],
                callback_data="no_channel"  
            )
        ]
    ],
)
    return question
