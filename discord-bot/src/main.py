import discord  # type: ignore
from discord.ext import tasks  # type: ignore
import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore

from config.token import TOKEN

# Toine Lay card leaks account (Bluesky)
ToineLayBsky = "https://bsky.app/profile/toinelay.bsky.social"

# Gains access to bot intents given through developer portal
intents = discord.Intents.default()
intents.message_content = True

# Discord bot setup
class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        
        # Test by sending the latest post immediately when the bot is ready
        channel = discord.utils.get(self.get_all_channels(), name="general")
        if channel:
            await channel.send("Bot is online")
            
# Creates bot and runs it
client = Client(intents=intents)
client.run(TOKEN)

