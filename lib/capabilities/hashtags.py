from typing import Iterator, Literal
from gogettr.capabilities.base import Capability
from gogettr.utils import merge


class Hashtags(Capability):
    def pull(self, max: int = None) -> Iterator[dict]:
        """Pull the suggested hashtags.

        :param int max: the maximum number of hashtags to pull"""

        # https://api.gettr.com/s/hashtag/suggest?max=20&offset=20
        url = "/s/hashtag/suggest"

        n = 0  # Number of hashtags emitted

        for data in self.client.get_paginated(
            url,
            params={
                "max": 20,
            },
            offset_step=20,
        ):
            for hashtag in data["data"]["list"]:
                # Verify that we haven't passed the max number of posts
                if max is not None and n >= max:
                    return

                n += 1
                yield merge(dict(hashtag=hashtag), data["aux"]["htinfo"][hashtag])
