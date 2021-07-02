import click
from lib import PublicClient
import json

client = PublicClient()


@click.group()
def cli():
    pass


@cli.command()
@click.argument("username")
@click.option("--max", help="the maximum number of posts to pull", type=int)
@click.option("--until", help="the ID of the earliest post to pull for the user")
def user_posts(username, max: int = None, until: str = None):
    """Pull posts by a user."""
    for post in client.user_posts(username, max=max, until=until):
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
