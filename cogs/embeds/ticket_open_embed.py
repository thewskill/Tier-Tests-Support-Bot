import discord
from datetime import datetime

def create_ticket_open_embed(reason, user):
    embed = discord.Embed(
        title="✅ Ticket Opened",
        description=f"Reason: **{reason}**",
        color=discord.Color.green()
    )
    embed.add_field(name="User", value=user.mention)
    embed.set_footer(text=f"Opened at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    return embed
