
from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
import os
from environs import Env

env = Env()
env.read_env(os.path.join('..', '.env'))

BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


admin_ids = [int(env('ADMIN_ID'))]


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids

@dp.message(IsAdmin(admin_ids))
async def answer_if_admin(message: Message):
    print(message.from_user.id, admin_ids)
    await message.answer(text='Вы админ')

@dp.message()
async def answer_if_not_admin(message: Message):
    print(message.from_user.id, admin_ids)
    await message.answer(text='Вы не админ')

if __name__ == '__main__':
    dp.run_polling(bot)