import discord
from discord.ext import commands

# Create an Intents object with default settings
intents = discord.Intents.default()

# Set up the bot prefix and create a bot instance
bot = commands.Bot(command_prefix='!', intents = intents)

# Event to print a message when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

# Command to send a message to a user in private chat
@bot.command(name='send_message')
async def send_message(ctx, user: discord.User, *, message):
    # Check if the command is invoked in a private chat
    if isinstance(ctx.channel, discord.DMChannel):
        try:
            # Send a private message to the specified user
            await user.send(message)
            await ctx.send(f'Message sent to {user.name}#{user.discriminator}')
        except discord.Forbidden:
            await ctx.send("I don't have permission to send a message to that user.")
    else:
        await ctx.send("This command can only be used in a private chat.")

# Run the bot with your token
bot.run(YOUR_BOT_TOKEN)
