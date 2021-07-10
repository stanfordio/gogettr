from gogettr.capabilities.base import Capability
from gogettr.utils import merge


class RegistrationStatus(Capability):
    def is_registered(
        self,
        username: str,
    ) -> bool:
        """Checks if username is registered in Gettr

        :param str username: username to check"""

        url = f"/s/user/{username}/exists"

        data = self.client.get(
            url,
        )
        return data
