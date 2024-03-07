from disnake.ext.commands import AutoShardedBot, Bot;
from aiohttp import ClientSession; from loguru import logger; from datetime import datetime;  from aiosqlite import connect
from core.functions.loader import ModulesLoader

class MyShardedBot(AutoShardedBot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.uptime = datetime.now()
        self.logger = logger
        self.session = ClientSession()

        ModulesLoader(self)

class MyBot(Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        kwargs['command_prefix'] = self.get_prefix

        self.uptime = datetime.now()
        self.session = ClientSession()
        self.logger = logger
        # self.db = connect("core/database/db.db")

        ModulesLoader(self)