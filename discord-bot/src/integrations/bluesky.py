from dotenv import load_dotenv  # type: ignore
import os
from atproto import Client
from .integration_manager import register_integration

# Load environment variables from .env file
load_dotenv()

# Toine Lay account handle
author_handle = "toinelay.bsky.social"

# Load the value from an environment variable
BSKY_PSWD = os.getenv("BSKY_PSWD")

# Initialize the client
client = Client()
client.login('willz-fps.bsky.social', BSKY_PSWD)

@register_integration("bluesky")
def fetch_latest_post():
    """Fetch the latest Bluesky post."""
    response = client.get_author_feed(author_handle, limit=1)
    first_post = response.feed[0].post  # Access the first post

    # Get post text
    post_text = first_post.record.text

    # Get the post ID
    post_id = first_post.uri.split("/")[-1]  # Extract the post ID from the URI

    # Construct the Bluesky post URL
    post_url = f"https://bsky.app/profile/{author_handle}/post/{post_id}"

    return post_text, post_url