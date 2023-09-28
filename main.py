import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router


async def main():
    bot = Bot(token='6297836283:AAGEaCSnuxlFJmc5a52s09uWJABvsRVAOe8')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
