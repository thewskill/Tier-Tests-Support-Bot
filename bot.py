import discord
from discord.ext import commands
from config import TOKEN

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

initial_extensions = [
    "cogs.ticket"
]

for ext in initial_extensions:
    bot.load_extension(ext)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(TOKEN)
