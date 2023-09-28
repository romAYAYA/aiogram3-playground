from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)

main_kb = [
    [KeyboardButton(text='Catalog'),
     KeyboardButton(text='Cart')],
    [KeyboardButton(text='Profile'),
     KeyboardButton(text='Contacts')]
]

main = ReplyKeyboardMarkup(keyboard=main_kb, resize_keyboard=True, input_field_placeholder='Choose an action below')

socials = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='tg', url='https://t.me/supernaturalmlady')],
    [InlineKeyboardButton(text='tg Dilya', url='https://t.me/daverexia')]
])

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Anime', callback_data='anime')],
    [InlineKeyboardButton(text='Nike', callback_data='nike')],
    [InlineKeyboardButton(text='Adidas', callback_data='adidas')]
])
