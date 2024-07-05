
from aiogram import Bot, Dispatcher, F
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


class PositiveNumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        for word in message.text.split():
            norm_word = word.replace('.', '').replace(',', '').strip()
            if norm_word.isdigit():
                numbers.append(int(norm_word))
        if numbers:
            return {'numbers': numbers}
        return False

@dp.message(F.text.lower().startswith('найди числа'), PositiveNumbersInMessage())
# Помимо объекта типа Message, принимаем в хэндлер список чисел из фильтра
# по соответствующему ключу `numbers`
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
            text=f'Нашел: {", ".join(str(num) for num in numbers)}')


# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа", но в нем нет чисел
@dp.message(F.text.lower().startswith('найди числа'))
async def process_if_not_numbers(message: Message):
    await message.answer(
            text='Не нашел что-то :(')

if __name__ == '__main__':
    dp.run_polling(bot)