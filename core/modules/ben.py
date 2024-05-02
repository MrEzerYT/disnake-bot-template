from disnake import Embed, Color, ApplicationCommandInteraction
from disnake.ext.commands import command, BucketType, cooldown, guild_only, Cog, slash_command
from random import choice


class Ben(Cog):
    def __init__(self, client):
        self.client = client

    @guild_only()
    @cooldown(1, 5, BucketType.user)
    @command()
    async def ben(self, ctx, *, text):
        random_text = ['YES', 'NO', 'HOHOHO']
        choices = choice(random_text)
        embed = Embed(color=Color.dark_theme(), title="Говорящий Бен", description="",
                                  timestamp=ctx.message.created_at)
        embed.add_field(name="Вопрос", value=text, inline=True)
        if choices == "YES":
            embed.set_image(url="https://i.imgur.com/WkzrLsa.gif")
            embed.add_field(name="Ответ", value="Да", inline=True)
            await ctx.send(embed=embed)

        if choices == "NO":
            embed.set_image(url="https://i.imgur.com/Yiuu8Jn.gif")
            embed.add_field(name="Ответ", value="Нет", inline=True)
            await ctx.send(embed=embed)

        if choices == "HOHOHO":
            embed.set_image(url="https://c.tenor.com/e8urEO5XU-kAAAAd/hohho-ho.gif")
            embed.add_field(name="Ответ", value="Хо-хо-хо", inline=True)
            await ctx.send(embed=embed)

    @guild_only()
    @cooldown(1, 5, BucketType.user)
    @slash_command(name="ben", description="Задать вопрос бену")
    async def _ben(self, inter: ApplicationCommandInteraction, text):
        random_text = ['YES', 'NO', 'HOHOHO']
        choices = choice(random_text)

        embed = Embed(color=Color.dark_theme(), title="Говорящий Бен", description="",
                                  timestamp=inter.message.created_at)
        embed.add_field(name="Вопрос", value=text, inline=True)
        if choices == "YES":
            embed.set_image(url="https://i.imgur.com/WkzrLsa.gif")
            embed.add_field(name="Ответ", value="Да", inline=True)
            await inter.send(embed=embed)

        if choices == "NO":
            embed.set_image(url="https://i.imgur.com/Yiuu8Jn.gif")
            embed.add_field(name="Ответ", value="Нет", inline=True)
            await inter.send(embed=embed)

        if choices == "HOHOHO":
            embed.set_image(url="https://c.tenor.com/e8urEO5XU-kAAAAd/hohho-ho.gif")
            embed.add_field(name="Ответ", value="Хо-хо-хо", inline=True)
            await inter.send(embed=embed)

def setup(client):
    client.add_cog(Ben(client))