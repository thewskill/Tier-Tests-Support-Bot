import discord
from discord.ui import View, button
from modals.reason_modal import ReasonModal

class TicketButtons(View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @button(emoji="🛠️", custom_id="support", style=discord.ButtonStyle.secondary)
    async def support(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(ReasonModal(self.bot, "Support"))

    @button(emoji="🤝", custom_id="partnership", style=discord.ButtonStyle.secondary)
    async def partnership(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(ReasonModal(self.bot, "Partnership"))

    @button(emoji="🧑‍💼", custom_id="staff", style=discord.ButtonStyle.secondary)
    async def staff(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(ReasonModal(self.bot, "Apply for Staff"))
