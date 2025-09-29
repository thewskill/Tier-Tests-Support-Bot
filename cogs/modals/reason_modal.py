import discord
from discord.ui import Modal, TextInput
from utils.ticket_utils import create_ticket_channel

class ReasonModal(Modal):
    def __init__(self, bot, ticket_type):
        super().__init__(title=f"{ticket_type} Ticket")
        self.bot = bot
        self.ticket_type = ticket_type
        self.reason = TextInput(label="Reason", style=discord.TextStyle.paragraph, required=True, max_length=500)
        self.add_item(self.reason)

    async def on_submit(self, interaction: discord.Interaction):
        await create_ticket_channel(self.bot, interaction, self.ticket_type, self.reason.value)
