from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import User
from config import CHAT_ID


async def is_chat_member(user: User) -> bool:
    bot = Bot.get_current()
    if bot:
        try:
            chat_member = await bot.get_chat_member(CHAT_ID, user.id)
            return chat_member.status == 'member'
        except TelegramBadRequest:
            return False

    return False
