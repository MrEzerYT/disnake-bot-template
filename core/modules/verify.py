from disnake.ui import Button, Modal, TextInput, View; from disnake import ModalInteraction, ButtonStyle, Embed, Color, MessageInteraction; from disnake.ext.commands import command, Cog, has_permissions

class VerifyModal(Modal):
    def __init__(self, code):
        self.code = code
        components = [
            TextInput(label="Введите код", placeholder=self.code, custom_id="code")
        ]
        super().__init__(title="Верификация", components=components, custom_id="verify_modal")

    async def callback(self, interaction: ModalInteraction) -> None:
        if self.code == int(interaction.text_values["code"]):
            role = interaction.guild.get_role(self.bot.roles["verify"])
            try:
                await interaction.author.add_roles(role, reason = "Прохождение верификации")
            except:
                await interaction.response.send_message("Вы уже прошли верификацию!", ephemeral=True)
            await interaction.response.send_message("Вы успешно прошли верификацию!", ephemeral=True)
        else:
            await interaction.response.send_message("Неверный код!", ephemeral=True)

class Verify(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_button_click(self, inter: MessageInteraction):
        if inter.component.custom_id == "verify":
            from random import randint
            await inter.response.send_modal(VerifyModal(code=randint(11111, 99999)))

    @has_permissions(administrator=True)
    @command()
    async def verify(self, ctx):
        embed = Embed(title="✅ Пройти верификацию для доступа к серверу.", description="> Чтобы **пройти** верификацию, **Вам** необходимо нажать на кнопку ` ✅ ` под **этим** сообщением.", color=Color.green())
        embed.set_image(url="https://cdn.mrezer.ru/flyrix/verify.gif")
        view = View()
        view.add_item(Button(emoji="✅", custom_id="verify", style=ButtonStyle.green))
        await ctx.send(embed=embed, view=view)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Verify(bot))