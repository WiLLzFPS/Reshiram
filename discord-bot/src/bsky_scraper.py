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

# Get all posts but limit to 1
response = client.get_author_feed(author_handle, limit=1)

# Access the first post in the feed
first_post = response.feed[0].post  # Access the first post

# Get post text
post_text = first_post.record.text

# Get post image
post_image = None
if hasattr(first_post.record, "embed") and hasattr(first_post.record.embed, "images"):
    post_image = first_post.record.embed.images[0].image.ref.link  # Access the image reference

# Construct the full image URL
post_image_url = None
if post_image:
    post_image_url = f"https://cdn.bsky.app/img/feed_fullsize/plain/{post_image}"

# Print the post details
print(f"Post Text: {post_text}")
if post_image_url:
    print(f"Post Image URL: {post_image_url}")