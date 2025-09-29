import discord
from discord.ui import View, button
from embeds.ticket_close_embed import create_ticket_close_embed
from embeds.ticket_log_embed import create_ticket_log_embed
from config import LOG_CHANNEL_ID

class CloseTicketView(View):
    def __init__(self, bot, user):
        super().__init__(timeout=None)
        self.bot = bot
        self.owner = user

    @button(label="Close Ticket", style=discord.ButtonStyle.danger, emoji="🔒")
    async def close(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.owner and not interaction.user.guild_permissions.manage_channels:
            await interaction.response.send_message("Only the ticket creator or staff can close this ticket.", ephemeral=True)
            return

        embed = create_ticket_close_embed(interaction.user)
        await interaction.channel.send(embed=embed)

        log_channel = interaction.guild.get_channel(LOG_CHANNEL_ID)
        if log_channel:
            log_embed = create_ticket_log_embed("Closed", self.owner, "Closed by button", interaction.channel)
            await log_channel.send(embed=log_embed)

        await interaction.channel.delete()
