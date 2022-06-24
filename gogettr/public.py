"""Defines the PublicClient, which is the primary way to interface with the
unauthenticated GETTR API."""
# pylint: disable=W0622 # we have variables called "max", "all", etc.

from functools import wraps

from gogettr.api import ApiClient
from gogettr.capabilities import (
    all,
    hashtags,
    search,
    suggested,
    trends,
    user_activity,
    user_info,
    user_relationships,
    comments,
    live,
)


class PublicClient:
    """A client for all the public GETTR methods. If the API doesn't require an
    account to pull the data, it belongs here."""

    def __init__(self):
        self.api_client = ApiClient()

    @wraps(user_activity.UserActivity.pull)
    def user_activity(self, *args, **kwargs):
        """Wrapper for "user_activity"."""
        return user_activity.UserActivity(self.api_client).pull(*args, **kwargs)

    @wraps(all.All.pull)
    def all(self, *args, **kwargs):
        """Wrapper for "all"."""
        return all.All(self.api_client).pull(*args, **kwargs)

    @wraps(user_info.UserInfo.pull)
    def user_info(self, *args, **kwargs):
        """Wrapper for "user_info"."""
        return user_info.UserInfo(self.api_client).pull(*args, **kwargs)

    @wraps(user_relationships.UserRelationships.pull)
    def user_relationships(self, *args, **kwargs):
        """Wrapper for "user_relationships"."""
        return user_relationships.UserRelationships(self.api_client).pull(
            *args, **kwargs
        )

    @wraps(trends.Trends.pull)
    def trends(self, *args, **kwargs):
        """Wrapper for "trends"."""
        return trends.Trends(self.api_client).pull(*args, **kwargs)

    @wraps(suggested.Suggested.pull)
    def suggested(self, *args, **kwargs):
        """Wrapper for "suggested"."""
        return suggested.Suggested(self.api_client).pull(*args, **kwargs)

    @wraps(hashtags.Hashtags.pull)
    def hashtags(self, *args, **kwargs):
        """Wrapper for "hashtags"."""
        return hashtags.Hashtags(self.api_client).pull(*args, **kwargs)

    @wraps(search.Search.pull)
    def search(self, *args, **kwargs):
        """Wrapper for "search"."""
        return search.Search(self.api_client).pull(*args, **kwargs)

    @wraps(comments.Comments.pull)
    def comments(self, *args, **kwargs):
        """Wrapper for "comments"."""
        return comments.Comments(self.api_client).pull(*args, **kwargs)

    @wraps(live.Live.pull)
    def live(self, *args, **kwargs):
        """Wrapper for "live"."""
        return live.Live(self.api_client).pull(*args, **kwargs)
