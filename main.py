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
