from ast import main
from aiogram import Bot, Dispatcher, executor, types

from TOKEN import TOKEN_API
from keyboard import rKeyboard


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def startCommand (message: types.Message):
    await message.answer(text='Answer', reply_markup=rKeyboard)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)