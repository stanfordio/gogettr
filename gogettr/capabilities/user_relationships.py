from typing import Iterator, Literal
from gogettr.capabilities.base import Capability


class UserRelationships(Capability):
    def pull(
        self,
        username: str,
        max: int = None,
        type: Literal["following", "followers"] = "following",
    ) -> Iterator[dict]:
        """Pull the given users' followers or the users a given user follows.

        :param str username: the username of the desired user
        :param int max: the maximum number of followers to pull
        :param str type: whether to pull followers or following"""

        # https://api.gettr.com/u/user/dineshdsouza/followers/?offset=0&max=10&incl=userstats|userinfo
        assert type in ["following", "followers"]

        if type == "following":
            url = f"/u/user/{username}/followings"
        elif type == "followers":
            url = f"/u/user/{username}/followers"

        n = 0  # Number of users emitted

        for data in self.client.get_paginated(
            url,
            params={
                "max": 500,  # They don't seem to limit this!
                "incl": "userstats|userinfo",
            },
            offset_step=500,
        ):

            # Check if we've run out of users to pull
            if len(data["data"]["list"]) == 0:
                return

            for username in data["data"]["list"]:
                # Verify that we haven't passed the max number of posts
                if max is not None and n >= max:
                    return

                n += 1
                yield data["aux"]["uinf"][username]
