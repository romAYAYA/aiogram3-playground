import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

import keyboards as kb

bot = Bot(token='6297836283:AAGEaCSnuxlFJmc5a52s09uWJABvsRVAOe8')
dp = Dispatcher()


@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Welcome, my lil bro', reply_markup=kb.main)


@dp.message(F.text == 'Contacts')
async def cmd_get_contacts(message: Message):
    await message.answer('Contacts: ', reply_markup=kb.socials)


@dp.message(F.text == '/check_id')
async def cmd_check_user_id(message: Message):
    await message.answer(f'Bro, how did you forgot that? Your id is: {message.from_user.id}')
    await message.reply(f'Bro, wtf? You forgot even your name, dude. Your name is: {message.from_user.first_name}')
    await message.answer_photo(photo='https://i.pinimg.com/564x/ff/0d/f4/ff0df44c4cd43c7cd964e36b4354e56b.jpg',
                               caption='Hello, mfucker. Did you expect that?')


@dp.message(F.text == 'Пивет')
async def cmd_check_user_id(message: Message):
    await message.answer('Hello, little bro ')


@dp.message(F.text == '/send_image')
async def cmd_send_image(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAM2ZRLkiyU-Zrt68Vy81-taatJ-rZkAAo_YMRukRZFIvRVDiFVk_NoBAAMCAAN5AAMwBA',
        caption='Photo sending example')


@dp.message(F.photo)
async def cmd_get_photo_id(message: Message):
    await message.answer(message.photo[-1].file_id)


@dp.message(F.document)
async def cmd_get_doc_id(message: Message):
    try:
        await bot.send_document(chat_id='408818548', document=message.document.file_id)
        await message.answer('File was sent')
    except Exception as err:
        await message.answer(f'File was not sent {err}')


@dp.message(F.text == '/send_doc')
async def cmd_send_doc(message: Message):
    await message.answer_document(document='BQACAgIAAxkBAAM9ZRLofOuJKubzJQrnMhV8W-ZfdYAAApc6AAK5bJhIgHUTcjZsaOgwBA')


@dp.message()
async def echo(message: Message):
    await message.answer_photo(photo='https://i.imgflip.com/487j1m.png',
                               caption='You wanna fuck me? NO, MFUCKER. FUCK YOU! GET THE FUCK OUT OF HERE!')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
