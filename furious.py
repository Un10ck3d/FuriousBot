# Import Things
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

# Load some config from .env
TOKEN = os.getenv('BOT_TOKEN')
ACTIVITY = os.getenv('MESSAGE')

# Enable Discord Intents
intents = discord.Intents.default()
intents.members = True

print("Starting bot...")

#Define Client / Bot
client = commands.Bot(command_prefix="!", intents=intents)

print("Bot started")
print("Connecting to Discord...")

# Set Status On Bot
@client.event
async def on_ready():
    print("Bot connected and Online\n")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=ACTIVITY))


# Run Bot
client.run(TOKEN)
