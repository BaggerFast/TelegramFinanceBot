from typing import Final

from aiogram import types

main_keyboard: Final = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
main_keyboard.add(types.KeyboardButton(text="Да"), types.KeyboardButton(text="Нет"))
