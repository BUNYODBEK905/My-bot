import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

BOT_TOKEN = "8607471107:AAGUUb5xz3wCY-1TN5n7sxPn9saAbKJWIrA"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Salom!")

async def main():
    await dp.start_polling(bot)

if__name ==" __main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())