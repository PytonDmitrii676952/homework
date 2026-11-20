# 9130229374:AAHDMIh9lSBEzAH2r6_tSRyzLtgOm-LyNSg
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message,CallbackQuery
from aiogram.filters import Command
from aiogram import F
from keyb import create_menu,keyb,question
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
@dp.message(Command("question"))
async def start(message: Message):
    await message.answer(
        "Хотите присоединится к нашему каналу?",
        reply_markup=question
    )

@dp.callback_query(F.data == "add_channel")
async def add_channel(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "Отлично! Добро пожаловать в наш канал!"
    )
@dp.callback_query(F.data == "no_channel")
async def no_channel(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "Хорошо! Вы всегда можете присоеденится позже."
    )
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

# @dp.message(F.text == texts["ru"]["menu"]["install_guide"])
# async def echo(message: Message):
#     await message.answer("Вот ссылка на сайт со всей информацией:" \
#     " https://git-scm.com/book/ru/v2/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-Git"
#     " Надо перейти по ссылке и найти пункт соответствующий вашей системе, после следовать инструкции.")
# @dp.message(F.text == texts["ru"]["menu"]["manuals"])
# async def echo(message: Message):
#     await message.answer("Вот мануалы для создания среды для использования Git:" \
#     " https://docs.github.com/ru/get-started/learning-to-code/getting-started-with-git" \
#     " Подробная инструция для настройки а так же использования Git.")
# @dp.message(F.text == texts["ru"]["menu"]["videos"])
# async def echo(message: Message):
#     await message.answer("Вот полезное видео, которе поможет вникнуть в Git и GitHub" \
#     " https://www.youtube.com/watch?v=eMETcugEX_c" \
#     " Это Видео очень подробно объясняет главное, что нужно знать о Git и GitHub.")
# @dp.message(F.text == texts["en"]["menu"]["install_guide"])
# async def echo(message: Message):
#     await message.answer("Here is link for installing Git:" \
#     " https://git-scm.com/book/en/v2/Getting-Started-Installing-Git"
#     " You need to follow the link and find the installer that corresponds to your system, then follow the guide.")
# @dp.message(F.text == texts["en"]["menu"]["manuals"])
# async def echo(message: Message):
#     await message.answer("Here's manuals for creating the environment for using Git:" \
#     " https://docs.github.com/en/get-started/learning-to-code/getting-started-with-git" \
#     " Detailed instructions for setting up and using Git.")
# @dp.message(F.text == texts["en"]["menu"]["videos"])
# async def echo(message: Message):
#     await message.answer("Here's a helpful video, that will help you get to grips with Git and GitHub" \
#     " https://www.youtube.com/watch?v=eMETcugEX_c" \
#     " This video explains, in great detail, the most important things you need to know about Git and GitHub.")

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
