from aiogram import Bot, Dispatcher, types, enums, F
from aiogram.filters.command import Command
from aiogram.client.default import DefaultBotProperties

import asyncio

from dotenv import dotenv_values

config = dotenv_values()
bot = Bot(token=config["TOKEN"],
          default=DefaultBotProperties(parse_mode=enums.ParseMode.HTML))

dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("ПРОВАЛИВАЙ!")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())