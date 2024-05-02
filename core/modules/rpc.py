from disnake.ext.commands import Cog; from disnake.ext.tasks import loop; from disnake import Game
from core.config import Status; from random import choice

class RPC(Cog):

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        await self.status.start()

    @loop(seconds=60.0)
    async def status(self):
        current_status = choice(Status)
        await self.bot.change_presence(activity=Game(name=current_status, platform="Linux"))

def setup(bot):
    bot.add_cog(RPC(bot))