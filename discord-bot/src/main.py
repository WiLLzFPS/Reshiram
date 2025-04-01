import discord # type: ignore
from config.token import TOKEN

# Creates a client connection to Discord
class Client(discord.Client):
    async def on_ready(self):   # Event handler for when the bot is ran
        print(f'Logged in as {self.user}')

# Gains access to bot intents given through developer portal
intents = discord.Intents.default()
intents.message_content = True

# Creates bot and runs it
client = Client(intents=intents)
client.run(TOKEN)