import asyncio
import logging
from typing import Any, Dict

import discord
from discord import Locale
from discord.ext import commands


from database import database
from utils.console_logger import setup_logger
from utils.data_loader import load_yml

setup_logger()
logger = logging.getLogger("bot")
logger.info("Log file has been created.")


class MyBot(commands.Bot):
    def __init__(self, *, config: Dict[str, Any], db: database.Database, **kwargs):
        super().__init__(**kwargs)
        self.default_locale = Locale.american_english
        self.config = config
        self.db = db

    async def load_cogs(self) -> None:
        cogs = ['help', 'weather', 'history'] 
        for cog in cogs:
            try:
                await self.load_extension(f"cogs.{cog}")
                logger.info("Loaded extension '%s'", cog)
            except Exception:
                logger.exception("Failed to load extension %s", cog)

    async def setup_hook(self) -> None:
        await self.load_cogs()
        logger.info("Sharding configuration: total shards = %d", self.shard_count or -1)
        logger.info("Syncing command tree...")
        await self.tree.sync()
        logger.info("Command tree synced.")
        self.remove_command('help')

    async def on_ready(self) -> None:
        logger.info("%s Bot is ready. %s", "=" * 20, "=" * 20)

    async def on_socket_response(self, msg: Dict[str, Any]) -> None:
        if msg.get('t') == 'RESUMED':
            logger.info('Shard connection resumed.')

    async def on_shard_disconnect(self, shard_id: int) -> None:
        logger.warning('Shard %d has disconnected from Gateway, attempting to reconnect...', shard_id)

    async def on_shard_ready(self, shard_id: int) -> None:
        self._ready_shards.add(shard_id)
        logger.info('Shard %d is ready (%d/%d).', shard_id, len(self._ready_shards), self.shard_count)
        if len(self._ready_shards) == self.shard_count:
            logger.info('All shards ready (%d total).', self.shard_count)

    async def on_shard_connect(self, shard_id: int) -> None:
        logger.info('Shard %d has connected to Gateway.', shard_id)


async def main():
    config = load_yml('assets/token.yml')

    token = config['TOKEN']
    db_url = config['DB_LOCAL_URI']

    logger.info("Local database connect")
    db_instance = database.Database(url=db_url)
    db_instance.database_init()

    intents = discord.Intents.all()
    intents.message_content = True

    activity = discord.CustomActivity(name="Testowy bot z programowania sieciowego")

    bot = MyBot(
        command_prefix="!$%ht",
        intents=intents,
        activity=activity,
        status=discord.Status.online,
        config=config,
        db=db_instance
    )

    async with bot:
        logger.info("%s Starting the bot. %s", "=" * 20, "=" * 20)
        await bot.start(token)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning("Bot has been terminated from console line")
