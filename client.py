import os
from pyrogram import Client
from config import Config
from config import LOGGER

class User(Client):
    def __init__(self):
        super().__init__(
            session_name=Config.TG_USER_SESSION,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.LOGGER(__name__).info(
            f"@{me.username} started!"
        )
        return self, me.id

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")