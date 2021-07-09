import logging
from typing import Iterator

from gogettr.capabilities.base import Capability
from gogettr.utils import merge


class Search(Capability):
    def pull(self, query: str, max: int = None) -> Iterator[dict]:
        """Search for posts matching the given query.

        :param str query: the query to be passed to GETTR
        :param int max: the maximum number of posts to pull"""

        url = "/u/posts/srch/phrase"
        n = 0  # Number of posts emitted

        for data in self.client.get_paginated(
            url,
            params={
                "max": 2000,
                "q": query,
            },
            offset_step=2000,
        ):
            for event in data["data"]["list"]:
                id = event["activity"]["tgt_id"]
                user = event["activity"]["src_id"]

                if id not in data["aux"]["post"]:
                    # Should we check `s_pst` too? It seems we usually don't need to, but
                    # worth investigating further.
                    logging.warning("Unable to find post data for post %s", id)
                    continue

                # Information about posts is spread across three objects, so we merge them
                # together here.
                post = merge(
                    event,
                    data["aux"]["post"].get(id),
                    data["aux"]["s_pst"].get(id),
                    dict(uinf=data["aux"]["uinf"].get(user)),
                )

                # Verify that we haven't passed the max number of posts
                if max is not None and n >= max:
                    return

                n += 1
                yield post
