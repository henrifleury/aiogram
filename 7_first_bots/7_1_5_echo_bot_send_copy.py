import os
from environs import Env
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

env = Env()
env.read_env(os.path.join('..', '.env'))

BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Халоу, это эхо-бот. Напиши что-нибудь и я верну тебе твое сообщение')


@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer('Халоу, это эхо-бот. Я возвращаю обратно ТЕКСТОВЫЕ сообщения')


@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply('send_copy не поддерживает такой тип апдейтов')

if __name__ == '__main__':
    dp.run_polling(bot)
