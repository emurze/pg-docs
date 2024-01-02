import inspect
from contextlib import suppress
from typing import Any


def get_annotations(obj: Any) -> dict:
    annotations = inspect.get_annotations(obj)
    with suppress(KeyError):
        annotations.pop("return")
    return annotations


def get_return_annotation(obj: Any) -> type | None:
    annotations = inspect.get_annotations(obj)
    return annotations.get("return")
