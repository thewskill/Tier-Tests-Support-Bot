import discord
from datetime import datetime

def create_ticket_log_embed(action, user, reason, channel):
    embed = discord.Embed(
        title=f"📋 Ticket {action}",
        color=discord.Color.orange() if action == "Opened" else discord.Color.red()
    )
    embed.add_field(name="User", value=user.mention)
    embed.add_field(name="Channel", value=channel.mention)
    embed.add_field(name="Reason", value=reason or "No reason provided", inline=False)
    embed.set_footer(text=f"{action} at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    return embed
