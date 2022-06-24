from gogettr.capabilities.base import Capability
from gogettr.utils import merge
from typing import Iterator


class Live(Capability):
    def pull(self, max: int = None, lang: str = "all") -> Iterator[dict]:

        url = "/u/posts/livenow"
        n = 0

        for data in self.client.get_paginated(
            url,
            params={
                "lang": lang,
                "incl": "posts|stats|userinfo|shared|liked",
                "max": 20,
            },
            offset_step=20,
            offset_start=0,
        ):
            for post in data["data"]["list"]:
                id = post["activity"]["tgt_id"]

                # Information about posts is spread across four objects, so we merge them together here.
                post = merge(
                    post,
                    data["aux"]["post"].get(id),
                    data["aux"]["s_pst"].get(id),
                    {"uinf": data["aux"]["uinf"].get(post["activity"]["tgt_oid"])},
                )

                # Verify that we haven't passed the max number of posts
                if max is not None and n >= max:
                    return

                n += 1
                yield post
