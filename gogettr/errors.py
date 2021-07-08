"""Defines GoGettr-specific errors."""

from typing import Any


class GettrApiError(RuntimeError):
    """This error is for when the GETTR API experiences an internal
    failure. Sometimes these can be resolved be retrying; sometimes
    not."""

    def __init__(self, issue: Any):
        self.issue = issue
        super().__init__()
