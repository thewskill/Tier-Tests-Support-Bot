import discord
from datetime import datetime

def create_ticket_close_embed(closed_by):
    embed = discord.Embed(
        title="🔒 Ticket Closed",
        description=f"This ticket has been closed by {closed_by.mention}.",
        color=discord.Color.red()
    )
    embed.set_footer(text=f"Closed at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    return embed
