from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb

router = Router()


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
