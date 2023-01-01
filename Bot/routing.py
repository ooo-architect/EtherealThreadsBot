from aiogram import Dispatcher
from handlers import channel
from handlers import chat


from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Any, Callable, Awaitable, Dict

class CounterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        print(event)
        return await handler(event, data)


def register_handlers(dp: Dispatcher):
    dp.include_router(chat.router)
    dp.include_router(channel.router)
    