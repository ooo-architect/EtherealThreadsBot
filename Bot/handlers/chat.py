import logging

from aiogram import Bot, Router, F
from aiogram.filters import IS_MEMBER, IS_NOT_MEMBER, ChatMemberUpdatedFilter
from aiogram.types import ChatMemberUpdated
from config import CHANNEL_ID, CHAT_ID

router = Router()


@router.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER), F.chat.id == CHAT_ID)
async def handle_chat_leave(event: ChatMemberUpdated):
    user = event.old_chat_member.user
    if user is None:
        return

    logging.debug(
        f'Member leave chat: Chat={event.chat.id} User={user.id}, {user.username} '
    )
    bot = Bot.get_current()
    if bot:
        logging.info(
            f'Member kicked: Chat={event.chat.id} User={user.id}, {user.username} '
        )
        # await bot.kick_chat_member(CHANNEL_ID, event.old_chat_member.user.id)
