import logging
import requests
import time


class ApiClient:
    def __init__(self, api_base_url: str = None):
        """Initializes the API client. Optionally takes in a base URL for the GETTR api."""
        self.api_base_url = api_base_url or "https://api.gettr.com"

    def get(
        self, url: str, params: dict = None, retries: int = 3, key: str = "results"
    ) -> dict:
        """Makes a request to the given API endpoint and returns the 'results' object. Supports retries. Soon will support authentication."""
        tries = 0

        while tries < retries:
            resp = requests.get(self.api_base_url + url, params=params)
            tries += 1
            if resp.status_code != 200 or key not in resp.json():
                logging.warning(
                    "Unable to pull from API; waiting %s seconds before retrying (attempt %s/%s)...",
                    4 ** tries,
                    tries,
                    retries,
                )
                time.sleep(4 ** tries)
                continue

            logging.debug("GET %s with params %s yielded %s", url, params, resp.content)
            return resp.json()[key]

        raise RuntimeError("unable to pull from Gettr")
