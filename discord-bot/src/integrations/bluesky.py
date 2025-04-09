from dotenv import load_dotenv  # type: ignore
import os
import requests
from .integration_manager import register_integration

# Load environment variables from .env file
load_dotenv()

# Toine Lay account handle
author_handle = "toinelay.bsky.social"

# Load the value from environment variables
BSKY_USERNAME = os.getenv("BSKY_USERNAME")
BSKY_PSWD = os.getenv("BSKY_PSWD")

# Bluesky API endpoints
BASE_URL = "https://bsky.social/xrpc"
LOGIN_ENDPOINT = f"{BASE_URL}/com.atproto.server.createSession"
FEED_ENDPOINT = f"{BASE_URL}/app.bsky.feed.getAuthorFeed"

# Track the last sent post ID
last_sent_post_id = None

# Authenticate with the Bluesky API
def authenticate():
    response = requests.post(
        LOGIN_ENDPOINT,
        json={"identifier": BSKY_USERNAME, "password": BSKY_PSWD},
    )
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()["accessJwt"]  # Extract the access token

# Fetch the latest post
@register_integration("bluesky")
def fetch_latest_post():
    global last_sent_post_id

    # Authenticate and get the access token
    access_token = authenticate()

    # Fetch the latest post from the user's feed
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"actor": author_handle, "limit": 1}
    response = requests.get(FEED_ENDPOINT, headers=headers, params=params)
    response.raise_for_status()  # Raise an error for bad responses

    # Parse the response
    feed = response.json().get("feed", [])
    if not feed:
        return None, None  # No posts available

    # Access the first post
    first_post = feed[0]["post"]

    # Get post text
    post_text = first_post["record"]["text"]

    # Get the post ID
    post_id = first_post["uri"].split("/")[-1]  # Extract the post ID from the URI

    # Check if the post is new
    if post_id == last_sent_post_id:
        return None, None  # No new post

    # Update the last sent post ID
    last_sent_post_id = post_id

    # Construct the Bluesky post URL
    post_url = f"https://bsky.app/profile/{author_handle}/post/{post_id}"

    return post_text, post_url