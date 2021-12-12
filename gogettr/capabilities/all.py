from concurrent.futures import ThreadPoolExecutor
from itertools import count, islice
from collections import deque
import logging
from typing import Iterator, Literal

from gogettr.capabilities.base import Capability
from gogettr.errors import GettrApiError
from gogettr.utils import b36decode, b36encode, extract, merge


class All(Capability):
    def pull(
        self,
        first: str = None,
        last: str = None,
        max: int = None,
        type: Literal["posts", "comments"] = "posts",
        order: Literal["up", "down"] = "up",
        workers: int = 10,
    ) -> Iterator[dict]:
        """Pulls all the posts from the API sequentially.

        :param str first: the id of the earliest post to include
        :param str last: the id of the last post to include
        :param int max: the maximum number of posts to pull
        :param str type: whether to pull posts or comments
        :order ["up" | "down"] order: whether to go from first to last (chronological)
            or last to first (reverse chronological)
        :param int workers: number of workers to run in parallel threads
        """

        assert type in ["posts", "comments"]

        n = 0  # How many posts we've emitted
        post_ids = self._post_id_generator(first, last, type, order)

        with ThreadPoolExecutor(max_workers=workers) as ex:
            # Submit initial work
            futures = deque(
                ex.submit(self._pull_post, post_id)
                for post_id in islice(post_ids, workers * 2)
            )

            while futures:
                result = futures.popleft().result()

                # Yield the result if it's valid
                if result is not None:
                    n += 1
                    yield result

                # Exit if we've hit the max number of posts
                if max is not None and n >= max:
                    return

                # Schedule more work, if available
                try:
                    futures.append(ex.submit(self._pull_post, next(post_ids)))
                except StopIteration:
                    # No more unscheduled post IDs to process
                    pass

    def _post_id_generator(
        self,
        first: str = None,
        last: str = None,
        type: Literal["posts", "comments"] = "posts",
        order: Literal["up", "down"] = "up",
    ) -> Iterator[str]:
        """Returns a generator of GETTR post IDs to pull."""

        # We remove the first character from the post IDs below because they are
        # always `p` and not part of the numbering scheme
        if order == "up":
            start_at = b36decode(first[1:]) if first is not None else 1
            end_at = b36decode(last[1:]) if last is not None else None
        else:
            if last is None:
                raise ValueError(
                    "the last post (i.e., the starting post) must be defined when"
                    "pulling posts reverse chronologically (we need to know where to start!)"
                )
            start_at = b36decode(last[1:])
            end_at = b36decode(first[1:]) if first is not None else 1

        for id in count(start_at, 1 if order == "up" else -1):
            yield ("p" if type == "posts" else "c") + b36encode(id)

            if end_at is not None and id == end_at:
                return

    def _pull_post(self, post_id: str) -> dict:
        """Attempt to pull the given post from GETTR."""

        try:
            data = self.client.get(
                f"/u/post/{post_id}",
                params={
                    "incl": "poststats|userinfo|posts|commentstats",
                },
                key="result",
            )
        except GettrApiError as e:
            logging.warning("Hit API error while pulling: %s", e)
            return
        if "txt" in data and data["data"]["txt"] == "Content Not Found":
            # Yes, this is how they do it. It's just a string.
            logging.info("Post %s not found...", post_id)
            return

        user_id = extract(data, ["data", "uid"])
        if user_id is None:
            return

        # At this point we know the post exists. Let's assemble and return it.
        post = merge(
            data["data"],
            dict(
                uinf=extract(data, ["aux", "uinf", user_id]),
                shrdpst=extract(data, ["aux", "shrdpst"]),
                s_pst=extract(data, ["aux", "s_pst"]),
                s_cmst=extract(data, ["aux", "s_cmst"]),
                post=extract(data, ["aux", "post"]),
            ),
        )

        return post
