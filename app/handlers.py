from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter
import app.keyboards as kb

router = Router()


class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in [418009489, 143]


@router.message(Admin(), F.text == '/admin')
async def cmd_admin(message: Message):
    await message.answer('You\'re admin')


@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Welcome!', reply_markup=kb.main)


@router.message(F.text == 'Catalog')
async def get_catalog(message: Message):
    await message.answer("Catalog: ", reply_markup=kb.catalog)


@router.callback_query(F.data == 'anime')
async def get_anime(callback: CallbackQuery):
    await callback.message.answer(f'You chose: {callback.data}')
    await callback.answer('Item was added!')
