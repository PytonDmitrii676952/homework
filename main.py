# 9130229374:AAHDMIh9lSBEzAH2r6_tSRyzLtgOm-LyNSg
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from keyb import create_menu,keyb
from translations import texts
import asyncio

bot = Bot(
    token = '9130229374:AAHDMIh9lSBEzAH2r6_tSRyzLtgOm-LyNSg',
    default = DefaultBotProperties(parse_mode = ParseMode.HTML)
)
dp = Dispatcher()
# @dp.message()
# async def echo(message: Message):
#     await message.answer(message.text)
user_language = {}
@dp.message(Command("start"))
async def echo(message: Message):   
    user_language[message.from_user.id] = "ru"
    await message.answer("Enter the language you want to communicate in:", reply_markup=keyb)
# @dp.message(Command("help"))
# async def echo(message: Message):
#     await message.answer(texts["ru"]["help"])
# async def echo(message: Message):
#     language = message.text.upper()
#     if language == "RU":
#         await message.answer("Привет,Я ваш бот,который может помочь тебе в изучении git и github")
#     elif language == "EN":
#         await message.answer("Hello, I am your bot that can help you learn git and github")
@dp.message(F.text == "RU")
async def russian(message: Message):
    user_language[message.from_user.id] = "ru"
    await message.answer(
        texts["ru"]["welcome"], reply_markup=create_menu("ru")
    )
@dp.message(F.text == "EN")
async def english(message: Message):
    user_language[message.from_user.id] = "en"
    await message.answer(
        texts["en"]["welcome"], reply_markup=create_menu("en")
    )
@dp.message(F.text == "📥 Гайд по установке")
async def echo(message: Message):
    await message.answer("Вот ссылка на сайт со всей информацией:" \
    " https://git-scm.com/book/ru/v2/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-Git"
    " Надо перейти по ссылке и найти пункт соответствующий вашей системе, после следовать инструкции.")
@dp.message(F.text == "📖 Мануалы")
async def echo(message: Message):
    await message.answer("Вот мануалы для создания среды для использования Git:" \
    " https://docs.github.com/ru/get-started/learning-to-code/getting-started-with-git" \
    " Подробная инструция для настройки а так же использования Git.")
@dp.message(F.text == "📽️ ВидеоГайды")
async def echo(message: Message):
    await message.answer("Вот полезное видео, которе поможет вникнуть в Git и GitHub" \
    " https://www.youtube.com/watch?v=VJm_AjiTEEc" \
    " Это Видео очень подробно объясняет главное, что нужно знать о Git и GitHub.")

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
