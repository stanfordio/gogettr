"""
Pull comments from a specific Gettr post
@author Konrad Iturbe
"""
from typing import Iterator

from gogettr.capabilities.base import Capability
from gogettr.utils import merge


class Comments(Capability):
    """
    @param post_id: comment ID from URL slug, as string, eg: "p2vhax"
    @param max: maximum number of comment posts to pull
    """
    def pull(self, post_id: str, max: int = None) -> Iterator[dict]:
        
        url = "/u/post/%s/comments" % post_id
        n = 0

        for data in self.client.get_paginated(
            url,
            params={
                "max": 20,
                "offset": "0",
                "dir": "rev",
                "incl": "posts|stats|userinfo|shared|liked"
            },
            offset_step=20,
        ):
            for comment in data["data"]["list"]:
                if max is not None and n >= max:
                    return

                n += 1
                yield merge(dict(comment=comment), data["aux"]["s_cmst"][comment["_id"]]) # Merge Engagement data with content
