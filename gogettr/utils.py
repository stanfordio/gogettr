"""Defines small utility functions to be used internally in GoGettr."""

from typing import Any, Iterator


def merge(*dicts):
    """Merges the given dictionaries into a single dictionary, ignoring overlapping keys."""

    out = dict()
    for dictionary in dicts:
        if dictionary is None:
            return out
        for (key, val) in dictionary.items():
            out[key] = val
    return out


def extract(obj: dict, path: Iterator[str], default: Any = None):
    """Tries to get the object at `path` out of the object, returning `default`
    if not found."""
    for key in path:
        if isinstance(obj, dict) and key in obj:
            obj = obj[key]
        else:
            return default
    return obj


# Following two functions adapted from
# https://stackoverflow.com/questions/1181919/python-base-36-encoding
def b36encode(number: int) -> str:
    """Convert the number to base36."""
    alphabet, base36 = ["0123456789abcdefghijklmnopqrstuvwxyz", ""]

    while number:
        number, i = divmod(number, 36)
        base36 = alphabet[i] + base36

    return base36 or alphabet[0]


def b36decode(number: str) -> int:
    """Convert the base36 number to an integer."""
    return int(number, 36)
