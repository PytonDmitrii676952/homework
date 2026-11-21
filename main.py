# 9130229374:AAHDMIh9lSBEzAH2r6_tSRyzLtgOm-LyNSg
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message,CallbackQuery
from aiogram.filters import Command
from aiogram import F
from keyb import create_menu,keyb,create_question
from translations import texts
import logging
import asyncio
logging.basicConfig(level=logging.INFO)
logging.info("Bot started")

bot = Bot(
    token = '9130229374:AAHDMIh9lSBEzAH2r6_tSRyzLtgOm-LyNSg',
    default = DefaultBotProperties(parse_mode = ParseMode.HTML)
)
dp = Dispatcher()
user_language = {}

@dp.message(Command("start"))
async def echo(message: Message):   
    user_language[message.from_user.id] = "ru"
    await message.answer("Enter the language you want to communicate in:", reply_markup=keyb)

@dp.message(Command("question"))
async def start(message: Message):
    language = user_language.get(message.from_user.id, "ru")
    await message.answer(
        texts[language]["question"],
        reply_markup=create_question(language)
    )
    print("User ID:", message.from_user.id)
    print("user language:", language)
    print("text:",texts[language]["question"])

@dp.callback_query(F.data == "add_channel")
async def add_channel(callback: CallbackQuery):
    await callback.answer()
    language = user_language.get(callback.from_user.id, "ru")
    await callback.message.answer(
        texts[language]["add_channel"]
    )
@dp.callback_query(F.data == "no_channel")
async def no_channel(callback: CallbackQuery):
    await callback.answer()
    language = user_language.get(callback.from_user.id, "ru")
    await callback.message.answer(
        texts[language]["no_channel"]
    )

@dp.message(F.text == "🇷🇺RU")
async def russian(message: Message):
    user_language[message.from_user.id] = "ru"
    await message.answer(
        texts["ru"]["welcome"], reply_markup=create_menu("ru")
    )
@dp.message(F.text == "🇺🇸EN")
async def english(message: Message):
    user_language[message.from_user.id] = "en"
    await message.answer(
        texts["en"]["welcome"], reply_markup=create_menu("en")
    )
@dp.message(F.text.in_([
    "📥 Гайд по установке",
    "📥 Install Guide"
]))
async def show_guides(message: Message):
    language = user_language.get(message.from_user.id, "ru")
    await message.answer( 
        texts[language]["install_guide"]
    )
@dp.message(F.text.in_([
    "📖 Мануалы",
    "📖 Manuals"
]))
async def show_manuals(message: Message):
    language = user_language.get(message.from_user.id, "ru")
    await message.answer(
        texts[language]["manuals"]
    )
@dp.message(F.text.in_([
    "📽️ ВидеоГайды",
    "📽️ Videos"
]))
async def show_videos(message: Message):
    language = user_language.get(message.from_user.id, "ru")
    await message.answer(
        texts[language]["videos"]
    )

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
