from gogettr.capabilities.base import Capability


class RegistrationStatus(Capability):
    def is_registered(
        self,
        username: str,
    ) -> bool:
        """Checks if the given username is registered on GETTR.

        :param str username: username to check"""

        url = f"/s/user/{username}/exists"

        data = self.client.get(
            url,
        )
        return data
