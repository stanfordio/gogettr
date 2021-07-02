from typing import Iterator
from lib.utils import merge
from lib.capabilities.base import Capability


class UserPosts(Capability):
    def pull(self, username: str, max: int = None, until: str = None) -> Iterator[dict]:
        url = f"/u/user/{username}/posts"
        n = 0  # Number of posts emitted

        cont = True
        while cont:
            data = self.client.get(
                url,
                params={
                    "offset": n,
                    "max": 20 if max is None else min(20, max - n),
                    "dir": "fwd",
                    "incl": "posts|stats|userinfo|shared|liked",
                    "fp": "f_uo",  # TODO: Figure out what this is. Seems media related?
                },
                key="result",
            )

            # Check if we've run out of posts to pull
            if len(data["data"]["list"]) == 0:
                break

            for event in data["data"]["list"]:
                id = event["activity"]["tgt_id"]

                # Information about posts is spread across three objects, so we merge them together here.
                post = merge(event, data["aux"]["post"][id], data["aux"]["s_pst"][id])

                # Verify that we haven't passed the `until` post
                if until is not None and until > id:
                    cont = False
                    break

                n += 1
                yield post

            # Check if we've collected the maximum number of posts
            if max is not None and max <= n:
                break
