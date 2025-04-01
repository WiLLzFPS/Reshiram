import discord  # type: ignore
from config.token import TOKEN

# Creates a client connection to Discord
class Client(discord.Client):
    async def on_ready(self):  # Event handler for when the bot is ready
        print(f'Logged in as {self.user}')
        
        # Message to server test
        channel = discord.utils.get(self.get_all_channels(), name="general")
        if channel:
            await channel.send("Hi!")

# Gains access to bot intents given through developer portal
intents = discord.Intents.default()
intents.message_content = True

# Creates bot and runs it
client = Client(intents=intents)
client.run(TOKEN)