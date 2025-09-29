import discord
from config import CATEGORY_ID, LOG_CHANNEL_ID
from embeds.ticket_open_embed import create_ticket_open_embed
from embeds.ticket_log_embed import create_ticket_log_embed
from views.ticket_close_button import CloseTicketView

async def create_ticket_channel(bot, interaction, ticket_type, reason):
    guild = interaction.guild
    category = guild.get_channel(CATEGORY_ID)

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(view_channel=False),
        interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
        guild.me: discord.PermissionOverwrite(view_channel=True, send_messages=True)
    }

    channel = await guild.create_text_channel(
        name=f"{ticket_type.lower()}-{interaction.user.name}",
        overwrites=overwrites,
        category=category,
        reason=f"{ticket_type} ticket opened"
    )

    embed = create_ticket_open_embed(reason, interaction.user)
    view = CloseTicketView(bot, interaction.user)
    await channel.send(content=interaction.user.mention, embed=embed, view=view)

    log_channel = guild.get_channel(LOG_CHANNEL_ID)
    if log_channel:
        log_embed = create_ticket_log_embed("Opened", interaction.user, reason, channel)
        await log_channel.send(embed=log_embed)

    await interaction.response.send_message(f"Your ticket has been created: {channel.mention}", ephemeral=True)
