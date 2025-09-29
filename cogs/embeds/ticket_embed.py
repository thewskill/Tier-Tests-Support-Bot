import discord

def create_ticket_embed():
    return discord.Embed(
        title="Tier Tests Support",
        description=(
            "Click one of the buttons below to open a ticket.\n\n"
            "🛠️ Support\n"
            "🤝 Partnership\n"
            "🧑‍💼 Apply for Staff"
        ),
        color=discord.Color.blue()
    )
