from disnake import Embed, Color, MessageInteraction, PermissionOverwrite, SelectOption
from disnake.ext.commands import Cog, command, has_permissions
from disnake.ui import View, Button, StringSelect
from disnake.utils import get

class TicketsDropdown(StringSelect):
    def __init__(self):
        super().__init__(
            placeholder="❓ Выберите причину создания тикета",
            min_values=1,
            max_values=1,
            options=[
                SelectOption(label="Пополнение баланса", emoji="💳", value="balance"),
                SelectOption(label="Ошибки в работе хостинга", emoji="🫨", value="hosting_error"),
                SelectOption(label="Поддержка", emoji="📞", value="support"),
            ],
            custom_id="tickets_dropdown",
        )

class Tickets(Cog):
    def __init__(self, bot):
        self.bot = bot

    @has_permissions(administrator=True)
    @command(name="tickets")
    async def tickets(self, ctx):
        embed = Embed(
            title="📝 Поддержка",
            description="**📌 Задать вопрос у поддержки.** \n\n:calendar_spiral: **График работы Т.П.**:\n\n> Пн-Пт: с 8:00 до 21:00;\n> Сб-Вс: с 10:00 до 20:00. \n> ❓ Поддержка может работать с задержками в период экзаменов, праздничных дней и т.д.",
            color=Color.orange(),
        )
        embed.set_footer(text = self.bot.config.footer_text)
        view = View(timeout=500.0)
        view.add_item(TicketsDropdown())
        await ctx.send(embed=embed, view=view)
        await ctx.message.delete()

    @Cog.listener()
    async def on_dropdown(self, interaction):
        try:
            if interaction.component.custom_id == "tickets_dropdown":
                value = interaction.values[0]
                if value == "balance":
                    await self.create_ticket(interaction, "Пополнение баланса", 1231511804312555561)
                elif value == "hosting_error":
                    await self.create_ticket(interaction, "Ошибки в работе хостинга", 1231511824730427502)
                elif value == "support":
                    await self.create_ticket(interaction, "Поддержка", 1231511888496689162)
        except Exception as e:
            await interaction.response.send_message(embed=Embed(title=":x: Произошла непредвиденная ошибка", description=f"При выполнении операции произошла непредвиденная ошибка, сделайте скриншот ошибки и отправьте его разработчику <@1193846220230242335> в личные сообщения.\n\n👀 **Ошибка:**\n\n```diff\n{e}\n```", color=Color.red()), ephemeral=True)

    async def create_ticket(self, inter, reason: str, categoryid: int):
        member = inter.author
        guild = inter.guild
        category = guild.get_channel(categoryid)

        existing_channel = get(guild.text_channels, name=f"ticket-{member.id}")
        if existing_channel:
            await inter.response.send_message(
                f"{member.mention} у вас уже есть открытый тикет {existing_channel.mention}", ephemeral=True
            )
            return

        overwrites = {
            guild.default_role: PermissionOverwrite(read_messages=False, send_messages=False),
            member: PermissionOverwrite(read_messages=True, send_messages=True),
        }

        role = guild.get_role(int(self.bot.config.support_role_id))  # замените на ID вашей роли поддержки
        if role:
            overwrites[role] = PermissionOverwrite(read_messages=True, send_messages=True)

        channel = await guild.create_text_channel(
            f"ticket-{member.id}", overwrites=overwrites, category=category, reason = f"Был создан запрос в поддержку от @{self.bot.functions.username(member)} » ID: {member.id}"
        )

        view = View()
        view.add_item(Button(label="Закрыть", custom_id="close_ticket"))
        embed = Embed(
            title="Запрос в поддержку",
            description=f"{reason}\nОжидайте ответа от {role.mention}, это может занять от 1 минуты до 1 часа!",
            color=Color.orange(),
        )
        embed.set_footer(text=f"@{self.bot.functions.username(member)} • ID: {member.id}", icon_url=member.avatar.url)
        pinned_message = await channel.send(f"{member.mention} {role.mention}", embed=embed, view=view)
        await pinned_message.pin()

        await inter.response.send_message(f"{member.mention} Ваш тикет: {channel.mention}", ephemeral=True)
        self.bot.logger.debug(f"Я создал тикет {channel.name} с категорией {category.name}")
    @Cog.listener()
    async def on_button_click(self, inter: MessageInteraction):
        if inter.component.custom_id == "close_ticket":
            channel = inter.channel
            if channel.name.startswith("ticket-"):
                await channel.delete(reason="Тикет закрыт.")
                await inter.author.send(embed=Embed(title="Тикет был закрыт.", description="Вы успешно закрыли тикет!", color=Color.orange()))
                self.bot.logger.debug(f"Я закрыл тикет {channel.name}")
            else:
                pass

def setup(bot):
    bot.add_cog(Tickets(bot))
