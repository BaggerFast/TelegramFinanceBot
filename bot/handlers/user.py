from aiogram import types, Dispatcher

from bot.keyboards import main_keyboard


async def start(msg: types.Message):
    await msg.bot.send_message(msg.from_user.id, f"Ты BaggerFast?", reply_markup=main_keyboard)


async def answer_start_question(msg: types.Message):
    bot = msg.bot
    if msg.text == "Да":
        await bot.send_message(msg.from_user.id, "Попался питонист!")
    elif msg.text == "Нет":
        await bot.send_message(msg.from_user.id, "Ок, поверим тебе.\n"
                                                 "Но я за тобой слежу!")
    else:
        pass


def register_users_handlers(dp: Dispatcher):
    dp.register_message_handler(answer_start_question, content_types=["text"], text=["Да", "Нет"])
    dp.register_message_handler(start, commands=["start"])
