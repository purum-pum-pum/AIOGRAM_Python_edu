from ast import If
from email import message
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType
import string
import random


TOKEN_API = '5371538285:AAGP91laa0Cbgs978G9-VnWS3DR3nv6FYz4'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def description_message(message: types.Message):
    if message.content_type == ContentType.PHOTO:
        await message.answer("я бот который становится умнее")

    elif message.text:
        await message.answer("Отправьте, пожалуйста, свою фотографию")

    else:
        message.answer("Это я не понимаю")


if __name__ == '__main__':
    executor.start_polling(dp)

#grewa