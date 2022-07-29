from aiogram import Bot, Dispatcher, executor
from loguru import logger

from bot import TgBot


def main():
    bot = Bot(token=TgBot.TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot)
    logger.info('Bot start')
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
