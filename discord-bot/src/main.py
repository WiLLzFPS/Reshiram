import os
import discord  # type: ignore
from dotenv import load_dotenv  # type: ignore
from bsky_scraper import get_latest_bsky_post  # Import the function from bsky_scraper

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
            # Fetch the latest Bluesky post
            try:
                post_text, post_url = get_latest_bsky_post()

                # Create an embed for the post
                embed = discord.Embed(
                    title="New Toine Lay Post!",
                    description=post_text,
                    color=discord.Color.blue(),
                    url=post_url  # Embed the link to the Bluesky post
                )

                # Add the link to the embed
                embed.add_field(name="View Post", value=f"[Click here to view the post]({post_url})", inline=False)

                # Send the embed to the channel
                await channel.send(embed=embed)

            except Exception as e:
                # Handle errors and send a message to the channel
                print(f"Error fetching Bluesky post: {e}")
                await channel.send("Failed to fetch the latest Bluesky post.")

# Creates bot and runs it
client = Client(intents=intents)
client.run(TOKEN)