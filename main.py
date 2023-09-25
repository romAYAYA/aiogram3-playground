import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

bot = Bot(token='6297836283:AAGEaCSnuxlFJmc5a52s09uWJABvsRVAOe8')
dp = Dispatcher()


@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Welcome, my lil bro')


@dp.message(F.text == '/check_id')
async def cmd_check_user_id(message: Message):
    await message.answer(f'Bro, how did you forgot that? Your id is: {message.from_user.id}')
    await message.reply(f'Bro, wtf? You forgot even your name, dude. Your name is: {message.from_user.first_name}')
    await message.answer_photo(photo='https://i.pinimg.com/564x/ff/0d/f4/ff0df44c4cd43c7cd964e36b4354e56b.jpg',
                               caption='Hello, mfucker. Did you expect that?')


@dp.message(F.text == 'Пивет')
async def cmd_check_user_id(message: Message):
    await message.answer('Привет, маленький пенис')


@dp.message()
async def echo(message: Message):
    await message.answer_photo(photo='https://i.imgflip.com/487j1m.png',
                               caption='You wanna fuck me? NO, MFUCKER. FUCK YOU! GET THE FUCK OUT OF HERE!')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
