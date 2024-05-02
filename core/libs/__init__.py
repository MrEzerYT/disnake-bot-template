from disnake import Intents, Status, __version__, Game; from disnake.ext.tasks import loop; from disnake.ext.commands import AutoShardedBot, when_mentioned_or
from loguru import logger;
from ..config import *; from ..oauth import release; from .bot import MyBot; from random import choice

logger.success("All libs imported!")
logger.info(f"Disnake version: {__version__}")

# Парсинг токена из конфига и проверка условия из oauth
if release:
    token = Auth.discord_auth["release"]
else:
    token = Auth.discord_auth["debug"]

intents = Intents.all()
client = MyBot(command_prefix = when_mentioned_or(prefix), intents = intents, strip_after_prefix = True, case_insensitive = True, enable_debug_events = True, reload = True) # для перезагрузки любого модуля (cog) не надо рестарить бота, за это отвечает reload