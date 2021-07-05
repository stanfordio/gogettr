from gogettr.utils import merge
from gogettr.capabilities.base import Capability


class UserInfo(Capability):
    def pull(
        self,
        username: str,
    ) -> dict:
        """Pull the given user's information.

        :param str username: the username of the desired user"""

        url = f"/s/uinf/{username}"

        data = self.client.get(
            url,
            key="result",
        )

        return merge(data["data"], dict(aux=data["aux"]))
