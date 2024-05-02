from disnake import Embed, Color
from disnake.ext.commands import slash_command, Cog
from psutil import virtual_memory

class Info(Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="about", description="О боте.")
    async def about(self, inter):
        embed = Embed(title="Disnake Bot Template | About", description=":closed_book: **Привет** \nМеня создали как основу для создания ботов в Discord! Мой исходный код можно найти в [GitHub](https://github.com/MrEzerYT/disnake-bot-template)", color = Color.green())
        embed.add_field(name="Информация о серверах", value = f"Количество серверов: **{len(self.bot.guilds)}** \nКоличество пользователей: **{len(self.bot.users)}** \nКоличество стикеров: **{len(self.bot.stickers)}** \nКоличество эмодзи: **{len(self.bot.emojis)}**")
        embed.add_field(name="Информация о боте", value=f"Мой ID: **{inter.me.id}** \nКоличество слеш команд: **{len(self.bot.global_slash_commands)}** \nКоличество обычных команд: **{len([i for i in self.bot.commands])}** \nЗадержка: **{round(self.bot.latency*1000, 2)}mc** \n RAM^ ** {virtual_memory().percent}%**")
        await inter.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
