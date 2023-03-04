import disnake #disnake
from disnake.ext import commands
import psutil

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="about", description="О боте.")
    async def about(self, ctx):
        embed = disnake.Embed(title="LessonBot | About", description=":closed_book: **Привет** \nМеня создали для уроков по disnake! Мой исходный код можно найти в GitHub", color = disnake.Color.green())
        embed.add_field(name="Информация о серверах", value = f"Количество серверов: **{len(self.bot.guilds)}** \nКоличество пользователей: **{len(self.bot.users)}** \nКоличество стикеров: **{len(self.bot.stickers)}** \nКоличество эмодзи: **{len(self.bot.emojis)}**")
        embed.add_field(name="Информация о боте", value=f"Мой ID: **{ctx.me.id}** \nКоличество слеш команд: **{len(self.bot.global_slash_commands)}** \nКоличество обычных команд: **{len([i for i in self.bot.commands])}** \nЗадержка: **{round(self.bot.latency*1000, 2)}mc** \n RAM^ ** {psutil.virtual_memory().percent}%**")
        await ctx.send(embed=embed)

    @commands.slash_command()
    async def command_1(self, ctx):
        await ctx.send("тест")

def setup(bot):
    bot.add_cog(Info(bot))