import discord
from discord.ext import commands
from embeds.ticket_embed import create_ticket_embed
from views.ticket_buttons import TicketButtons

class TicketCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ticket")
    async def ticket_command(self, ctx):
        embed = create_ticket_embed()
        view = TicketButtons(self.bot)
        await ctx.send(embed=embed, view=view)

def setup(bot):
    bot.add_cog(TicketCog(bot))
