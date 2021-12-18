# Import Things
import os

from dotenv import load_dotenv

import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import Bot
from nextcord.voice_client import VoiceClient

load_dotenv()

# Load some config from .env
TOKEN = os.getenv('BOT_TOKEN')
ACTIVITY = os.getenv('MESSAGE')

# Enable Discord Intents
intents = nextcord.Intents.default()
intents.members = True

print("Starting bot...")

#Define Client / Bot
client = commands.Bot(command_prefix="*", intents=intents)

print("Bot started")
print("Connecting to Discord...")

# Set Status On Bot
@client.event
async def on_ready():
    print("Bot connected and Online\n")
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=ACTIVITY))

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients)
    audio_source = discord.FFmpegPCMAudio('sound.wav')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

# Run Bot
client.run(TOKEN)
