# 8960738280:AAHttdG3JulfHRaP8kwm5shF8HTW1J88jl8
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

bot = Bot(
    token = '8960738280:AAHttdG3JulfHRaP8kwm5shF8HTW1J88jl8',
    default = DefaultBotProperties(parse_mode = ParseMode.HTML)
)
dp = Dispatcher()
# @dp.message()
# async def echo(message: Message):
#     await message.answer(message.text)
@dp.message(Command("start"))
async def echo(message: Message):
    await message.answer("Привет,друг")

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
