from aiogram import Router
import logging

from aiogram import Router
from aiogram.types import ChatJoinRequest
from utils import is_chat_member

router = Router()


@router.chat_join_request()
async def handle_join_request(request: ChatJoinRequest):
    logging.info(
        f'Chat join request: Chat={request.chat.id} User={request.from_user.id}, {request.from_user.username} '
    )

    if await is_chat_member(request.from_user):
        logging.info(
            f'Join approved: Chat={request.chat.id} User={request.from_user.id}, {request.from_user.username} '
        )
        await request.approve()
    else:
        logging.info(
            f'Join declined: Chat={request.chat.id} User={request.from_user.id}, {request.from_user.username} '
        )
        await request.decline()


# @router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER), F.chat.id == CHANNEL_ID)
# async def handle_chat_member(event: ChatMemberUpdated):
#     logging.info(
#         f'New channel member: Chat={event.chat.id} User={e}'
#     )
#     if not await is_chat_member(event.from_user):
#         bot = Bot.get_current()
#         if bot:
#             logging.info(f'Member kicked: Chat={event.chat.id} User={event.from_user.id}, {event.from_user.username} ')
#             await bot.kick_chat_member(CHANNEL_ID, event.from_user.id)
    