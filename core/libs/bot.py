from disnake.ext.commands import AutoShardedBot, Bot;
from aiohttp import ClientSession; from loguru import logger; from datetime import datetime
from core import functions; from core.config import Config


class MyShardedBot(AutoShardedBot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.uptime = datetime.now()
        self.session = ClientSession()
        self.logger = logger
        self.functions = functions
        self.config = Config

        functions.ModulesLoader(self)

class MyBot(Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        kwargs['command_prefix'] = self.get_prefix

        self.uptime = datetime.now()
        self.session = ClientSession()
        self.logger = logger
        self.functions = functions
        self.config = Config

        functions.ModulesLoader(self, "core/modules")
