import itertools as it


def get_sliced_dict(_dict: dict, stop: int, start: int | None = None) -> dict:
    return dict(it.islice(_dict.items(), stop, start))
