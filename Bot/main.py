import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from routing import register_handlers


def main():
    logging.basicConfig(level=logging.DEBUG)

    bot = Bot(TOKEN)
    dp = Dispatcher()

    register_handlers(dp)

    dp.run_polling(bot, allowed_updates=['chat_join_request', 'chat_member'])


if __name__ == '__main__':
    main()