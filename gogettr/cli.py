import click
from gogettr import PublicClient
import json
import logging

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
log_hander = logging.FileHandler("gogettr.log")
logger.addHandler(log_hander)

client = PublicClient()


@click.group()
def cli():
    pass


@cli.command()
@click.argument("username")
@click.option("--max", help="the maximum number of activities to pull", type=int)
@click.option("--until", help="the ID of the earliest activity to pull for the user")
@click.option(
    "--type",
    help="",
    type=click.Choice(["posts", "comments", "likes"]),
    default="posts",
)
def user(username, max: int = None, until: str = None, type: str = None):
    """Pull the posts, likes, or comments made by a user."""
    for post in client.user_activity(username, max=max, until=until, type=type):
        print(json.dumps(post))


@cli.command()
@click.option(
    "--first", help="the ID of the first post to pull", type=str, default="p1"
)
@click.option("--last", help="the ID of the last post to pull", type=str)
@click.option("--max", help="the maximum number of posts to pull", type=int)
@click.option(
    "--rev",
    help="increment reverse chronologically (i.e., from last to first)",
    is_flag=True,
)
@click.option(
    "--type",
    help="",
    type=click.Choice(["posts", "comments"]),
    default="posts",
)
def all(first=None, last=None, max: int = None, rev=False, type: str = None):
    """Pull all posts (or comments) sequentially.

    Note that if iterating chronologically and both max and last are unset, then this command will run forever (as it will iterate through all post IDs to infinity). To prevent this, either specify a max, last post, or iterate reverse chronologically."""
    for post in client.all(
        first=first, last=last, max=max, order="down" if rev else "up", type=type
    ):
        print(json.dumps(post))


@cli.command()
@click.argument("username")
def user_info(username):
    """Pull given user's information."""
    print(json.dumps(client.user_info(username)))


@cli.command()
@click.argument("username")
@click.option("--max", help="the maximum number of users to pull", type=int)
def user_followers(username, max: int = None):
    """Pull all a user's followers."""
    for user in client.user_relationships(username, max=max, type="followers"):
        print(json.dumps(user))


@cli.command()
@click.argument("username")
@click.option("--max", help="the maximum number of users to pull", type=int)
def user_following(username, max: int = None):
    """Pull all users a given user follows."""
    for user in client.user_relationships(username, max=max, type="following"):
        print(json.dumps(user))


@cli.command()
@click.option("--max", help="the maximum number of posts to pull", type=int)
@click.option("--until", help="the ID of the earliest post to pull")
def trends(max: int = None, until: str = None):
    """Pull all the trends (posts displayed on the home page)."""
    for post in client.trends(max=max, until=until):
        print(json.dumps(post))


@cli.command()
@click.option("--max", help="the maximum number of users to pull", type=int)
def suggested(max: int = None):
    """Pull the suggested users (users displayed on the home page)."""
    for user in client.suggested(max=max):
        print(json.dumps(user))


@cli.command()
@click.option("--max", help="the maximum number of hashtags to pull", type=int)
def hashtags(max: int = None):
    """Pull the suggested hashtags (the top suggestions are displayed on the front page).

    Note that while the first five or so hashtags have expanded information associated with them, later results do not."""
    for hashtag in client.hashtags(max=max):
        print(json.dumps(hashtag))
