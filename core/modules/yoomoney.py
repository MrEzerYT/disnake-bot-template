from disnake.ext.commands import slash_command, Cog; from disnake import Embed; from disnake.ui import View, Button
from yoomoney import Quickpay

class YooPayment(Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="paycreate", description = "Создать счёт для оплаты в РФ")
    async def paycreate(self, inter, sum: int, title, comment):
        quickpay = Quickpay(
            receiver = int(self.bot.config.yoomoney_id),
            quickpay_form = "shop",
            targets = title.strip(),
            paymentType = "SB",
            sum = sum,
            label = comment.strip(),
        )

        embed = Embed(title = "Счёт для оплаты", description = "Ваш счёт для оплаты успешно создан!")
        embed.add_field(name = "Сумма", value=f"{sum} руб.", inline = True)
        embed.add_field(name = "Комментарий", value=f"{comment}", inline = True)

        view = View()
        view.add_item(Button(label = "Оплатить", emoji="💳", url = quickpay.base_url))

        await inter.send(embed = embed, view = view)

def setup(bot):
    bot.add_cog(YooPayment(bot))