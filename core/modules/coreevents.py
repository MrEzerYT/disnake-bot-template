from disnake.ext.commands import Cog

class CoreEvents(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        self.bot.logger.info("")
        self.bot.logger.info(f"Bot is loaded as {self.bot.user}")
        self.bot.logger.info(f"Client id {self.bot.user.id}")
        self.bot.logger.info(f"Developed by https://ezer.su (Dan)")
        self.bot.logger.info("")

def setup(bot):
    bot.add_cog(CoreEvents(bot))
