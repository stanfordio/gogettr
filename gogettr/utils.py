def merge(*dicts):
    """Merges the given dictionaries into a single dictionary, ignoring overlapping keys."""

    d = dict()
    for dictionary in dicts:
        for (k, v) in dictionary.items():
            d[k] = v
    return d


# Following two functions adapted from https://stackoverflow.com/questions/1181919/python-base-36-encoding
def b36encode(number: int) -> str:
    """Convert the number to base36."""
    alphabet, base36 = ["0123456789abcdefghijklmnopqrstuvwxyz", ""]

    while number:
        number, i = divmod(number, 36)
        base36 = alphabet[i] + base36

    return base36 or alphabet[0]


def b36decode(number: int):
    """Convert the base36 number to an integer."""
    return int(number, 36)
