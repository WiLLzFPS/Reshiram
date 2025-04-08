from .integration_manager import register_integration

# Fetch the latest Reddit post (example)
@register_integration("reddit")
def fetch_latest_post():
    # Example logic for fetching a Reddit post
    post_text = "Example Reddit Post"
    post_url = "https://reddit.com/example-post"
    return post_text, post_url