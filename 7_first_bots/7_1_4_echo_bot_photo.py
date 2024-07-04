import os
from environs import Env
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from aiogram.types import ContentType
from aiogram import F

env = Env()
env.read_env(os.path.join('..', '.env'))

BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def process_start_command(message: Message):
    await message.answer('Халоу, это эхо-бот. Напиши что-нибудь и я верну тебе твое сообщение')


async def process_help_command(message: Message):
    await message.answer('Халоу, это эхо-бот. Я возвращаю обратно ТЕКСТОВЫЕ сообщения')

async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)

async def send_echo(message: Message):
    await message.reply(message.text)


dp.message.register(process_start_command, Command(commands=['start']))
dp.message.register(process_help_command, Command(commands=['help']))
#dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
