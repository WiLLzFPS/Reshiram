import os
import discord  # type: ignore
from dotenv import load_dotenv  # type: ignore
from integrations.integration_manager import get_integration

# Import all integrations to ensure they are registered
import integrations.bluesky 

# Load environment variables from .env file
load_dotenv()

# Load the token from an environment variable
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Gains access to bot intents given through developer portal
intents = discord.Intents.default()
intents.message_content = True

# Discord bot setup
class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        
        # Get channel name
        channel = discord.utils.get(self.get_all_channels(), name="general")
        if channel:
            # Fetch the latest post from the desired integration
            try:
                # Specify the integration to use
                integration_name = "bluesky"
                fetch_post = get_integration(integration_name)
                post_text, post_url = fetch_post()

                # Send the first message with the text "New Post!"
                await channel.send("New Post!")

                # Send the post URL as a separate message
                await channel.send(post_url)

            except Exception as e:
                # Handle errors and send a message to the channel
                print(f"Error fetching post: {e}")
                await channel.send("Failed to fetch the latest post.")

# Creates bot and runs it
client = Client(intents=intents)
client.run(TOKEN)