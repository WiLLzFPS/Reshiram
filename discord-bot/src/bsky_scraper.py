from dotenv import load_dotenv  # type: ignore
import os
import atproto_client  # type: ignore

# Load environment variables from .env file
load_dotenv()

# Toine Lay account handle
author_handle = "toinelay.bsky.social"

# Load the value from an environment variable
BSKY_PSWD = os.getenv("BSKY_PSWD")

# Initialize the client
client = atproto_client.Client()
client.login('willz-fps.bsky.social', BSKY_PSWD)

# Function to fetch the latest Bluesky post
def get_latest_bsky_post():
    response = client.get_author_feed(author_handle, limit=1)
    first_post = response.feed[0].post  # Access the first post

    # Get post text
    post_text = first_post.record.text

    # Get the post ID
    post_id = first_post.uri.split("/")[-1]  # Extract the post ID from the URI

    # Construct the Bluesky post URL
    post_url = f"https://bsky.app/profile/{author_handle}/post/{post_id}"

    # Print the post text and URL
    print(f"Post Text: {post_text}")
    print(f"Post URL: {post_url}")

    return post_text, post_url