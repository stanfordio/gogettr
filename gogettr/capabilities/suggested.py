from typing import Iterator, Literal
from gogettr.capabilities.base import Capability


class Suggested(Capability):
    def pull(self, max: int = None) -> Iterator[dict]:
        """Pull the suggested users.

        :param int max: the maximum number of followers to pull"""

        # https://api.gettr.com/s/usertag/suggest?offset=0&max=16&incl=userinfo%7Cfollowings
        url = "/s/usertag/suggest"

        n = 0  # Number of users emitted

        for data in self.client.get_paginated(
            url,
            params={
                "max": 16,
                "incl": "userinfo|followings",
            },
            offset_step=16,
        ):
            for username in data["data"]["list"]:
                # Verify that we haven't passed the max number of posts
                if max is not None and n >= max:
                    return

                n += 1
                yield data["aux"]["uinf"][username]
