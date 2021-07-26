"""Defines the ApiClient class, which provides a standard interface for interacting with
the GETTR API."""

import itertools
import logging
import time
from typing import Callable, Iterator

import requests
from requests.exceptions import ReadTimeout

from gogettr.errors import GettrApiError

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)


class ApiClient:
    """A standard and safe way to interact with the GETTR API. Catches errors, supports
    retries, etc."""

    def __init__(self, api_base_url: str = None):
        """Initializes the API client. Optionally takes in a base URL for the GETTR api."""
        self.api_base_url = api_base_url or "https://api.gettr.com"

    def get(
        self, url: str, params: dict = None, retries: int = 3, key: str = "result"
    ) -> dict:
        """Makes a request to the given API endpoint and returns the 'results' object.
        Supports retries. Soon will support authentication."""
        tries = 0
        errors = []  # keeps track of the errors we've encountered

        def handle_error(issue):
            logging.warning(
                "Unable to pull from API: %s. Waiting %s seconds before retrying (%s/%s)...",
                issue,
                4 ** tries,
                tries,
                retries,
            )
            time.sleep(4 ** tries)
            errors.append(issue)

        while tries < retries:
            logging.info("Requesting %s (params: %s)...", url, params)
            tries += 1

            try:
                resp = requests.get(
                    self.api_base_url + url,
                    params=params,
                    timeout=10,
                    headers={"User-Agent": USER_AGENT},
                )
            except ReadTimeout as err:
                handle_error({"timeout": err})
                continue
            except Exception as e:
                handle_error({"error": str(e)})
                continue

            logging.info("%s gave response: %s", url, resp.text)

            if resp.status_code in [429, 500, 502, 503, 504]:
                handle_error({"status_code": resp.status_code})
                continue

            logging.debug("GET %s with params %s yielded %s", url, params, resp.content)

            data = resp.json()
            if key in data:
                return data[key]

            # Couldn't find the key, so it's an error.
            errors.append(data)  # Retry but without sleep.

        raise GettrApiError(errors[-1])  # Throw with most recent error

    def get_paginated(
        self,
        *args,
        offset_param: str = "offset",
        offset_start: int = 0,
        offset_step: int = 20,
        result_count_func: Callable[[dict], int] = lambda k: len(k["data"]["list"]),
        **kwargs
    ) -> Iterator[dict]:
        """Paginates requests to the given API endpoint."""
        for i in itertools.count(start=offset_start, step=offset_step):
            params = kwargs.get("params", {})
            params[offset_param] = i
            kwargs["params"] = params
            data = self.get(*args, **kwargs)
            yield data

            # End if no more results
            if result_count_func(data) == 0:
                return
