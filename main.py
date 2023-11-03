from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

bot = Bot(token='6297836283:AAGEaCSnuxlFJmc5a52s09uWJABvsRVAOe8')
dp = Dispatcher()


@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer('Hi there. \nThis is an echo bot \nWrite smth here')


@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer('Write smth here and I will send it back')


@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Not supported type'
        )


# @dp.message()
# async def send_echo(message: Message):
#     await message.reply(text=message.text)


# async def process_start_command(message: Message):
#     await message.answer('Hi there. \nThis is an echo bot \nWrite smth here')
#
#
# async def process_help_command(message: Message):
#     await message.answer(
#         'Write smth here'
#         ' and I will send it back'
#     )
#
#
# async def send_photo_echo(message: Message):
#     print(message)
#     await message.reply_photo(message.photo[0].file_id)
#
#
# async def send_echo(message: Message):
#     await message.reply(text=message.text)
#
#
# dp.message.register(process_start_command, Command(commands='start'))
# dp.message.register(process_help_command, Command(commands='help'))
# dp.message.register(send_echo)
# dp.message.register(send_photo_echo, F.photo)

if __name__ == '__main__':
    dp.run_polling(bot)
