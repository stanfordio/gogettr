from typing import Iterator, Literal
from lib.utils import b36decode, b36encode, merge
from lib.capabilities.base import Capability


class AllPosts(Capability):
    def pull(
        self,
        first: str = None,
        last: str = None,
        max: int = None,
        order: Literal["up", "down"] = "up",
    ) -> Iterator[dict]:
        """Pulls all the posts from the API sequentially.

        :param str first: the id of the earliest post to include
        :param str last: the id of the last post to include
        :param int max: the maximum number of posts to pull
        :order ["up" | "down"] order: whether to go from first to last (chronological) or last to first (reverse chronological)
        """

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
            data = self.client.get(
                f"/u/post/p{b36encode(post_id)}",
                params={
                    "incl": "poststats|userinfo",
                },
                key="result",
            )

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
                    shrdpst=data["aux"]["shrdpst"],
                    s_pst=data["aux"]["s_pst"],
                ),
            )
            n += 1
            yield post
