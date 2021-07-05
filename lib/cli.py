import click
from lib import PublicClient
import json

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
def all_posts(first=None, last=None, max: int = None, rev=False):
    """Pull all posts sequentially."""
    for post in client.all_posts(
        first=first, last=last, max=max, order="down" if rev else "up"
    ):
        print(json.dumps(post))


@cli.command()
@click.argument("username")
def user_info(username):
    """Pull given user's information."""
    print(json.dumps(client.user_info(username)))
