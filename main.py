# 9130229374:AAHDMIh9lSBEzAH2r6_tSRyzLtgOm-LyNSg
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from keyb import keyb
import asyncio

bot = Bot(
    token = '9130229374:AAHDMIh9lSBEzAH2r6_tSRyzLtgOm-LyNSg',
    default = DefaultBotProperties(parse_mode = ParseMode.HTML)
)
dp = Dispatcher()
# @dp.message()
# async def echo(message: Message):
#     await message.answer(message.text)
@dp.message(Command("start"))
async def echo(message: Message):
    await message.answer("Привет,Я ваш бот,который может помочь тебе в изучении git и github.\n"
    " Выберите язык,на котором вы хотите общаться",reply_markup=keyb)
@dp.message(Command("help"))
async def echo(message: Message):
    await message.answer("Я бот,который может помочь тебе в изучении git и github")
# @dp.message()
# async def echo(message: Message):
#     language = message.text.upper()
#     if language == "RU":
#         await message.answer("Привет,Я ваш бот,который может помочь тебе в изучении git и github")
#     elif language == "EN":
#         await message.answer("Hello, I am your bot that can help you learn git and github")
@dp.message(F.text == "🇷🇺 RU")
async def echo(message: Message):
    await message.answer("Привет,Я ваш бот,который может помочь тебе в изучении git и github")
@dp.message(F.text == "🇺🇸 EN")
async def echo(message: Message):
    await message.answer("Hello, I am your bot that can help you learn git and github")

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
