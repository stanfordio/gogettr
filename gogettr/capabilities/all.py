from typing import Iterator, Literal
from gogettr.utils import b36decode, b36encode, merge
from gogettr.capabilities.base import Capability
from gogettr.errors import GettrApiError
import logging


class All(Capability):
    def pull(
        self,
        first: str = None,
        last: str = None,
        max: int = None,
        type: Literal["posts", "comments"] = "posts",
        order: Literal["up", "down"] = "up",
    ) -> Iterator[dict]:
        """Pulls all the posts from the API sequentially.

        :param str first: the id of the earliest post to include
        :param str last: the id of the last post to include
        :param int max: the maximum number of posts to pull
        :param str type: whether to pull posts or comments
        :order ["up" | "down"] order: whether to go from first to last (chronological) or last to first (reverse chronological)
        """

        assert type in ["posts", "comments"]

        # We remove the first character from the post IDs below because they are always `p` and not part of the numbering scheme
        if order == "up":
            post_id = b36decode(first[1:]) if first is not None else 1
            end_at = b36decode(last[1:]) if last is not None else None
        else:
            if last is None:
                raise ValueError(
                    "the last post (i.e., the starting post) must be defined when pulling posts reverse chronologically (we need to know where to start!)"
                )
            post_id = b36decode(last[1:])
            end_at = b36decode(first[1:]) if first is not None else 1

        n = 0  # How many posts we've emitted

        while (
            end_at is None
            or (order == "up" and post_id <= end_at)
            or (order == "down" and post_id >= end_at)
        ) and (max is None or n < max):
            try:
                data = self.client.get(
                    f"/u/post/{'p' if type == 'posts' else 'c'}{b36encode(post_id)}",
                    params={
                        "incl": "poststats|userinfo|posts|commentstats",
                    },
                    key="result",
                )
            except GettrApiError as e:
                logging.warning("Hit API error while pulling: %s", e)

            if order == "up":
                post_id += 1
            else:
                post_id -= 1

            if data["data"]["txt"] == "Content Not Found":
                # Yes, this is how they do it. It's just a string.
                continue

            # At this point we know the post exists. Let's assemble and yield it.
            user_id = data["data"]["uid"]
            post = merge(
                data["data"],
                dict(
                    uinf=data["aux"]["uinf"][user_id],
                    shrdpst=data["aux"].get("shrdpst"),
                    s_pst=data["aux"].get("s_pst"),
                    s_cmst=data["aux"].get("s_cmst"),
                    post=data["aux"].get("post"),
                ),
            )

            n += 1
            yield post
