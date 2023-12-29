import functools
import inspect
import itertools as it
from collections.abc import Callable
from typing import Any
from contextlib import suppress

from pydantic import BaseModel, ValidationError


def get_sliced_dict(_dict: dict, stop: int, start: int | None = None) -> dict:
    return dict(it.islice(_dict.items(), stop, start))


def get_annotations(obj: type) -> dict:
    annotations = inspect.get_annotations(obj)
    with suppress(KeyError):
        annotations.pop('return')
    return annotations


def validate_annotation(value: Any, annotation: Any) -> str:
    if issubclass(annotation, BaseModel):
        try:
            annotation(**value)
        except ValidationError as err:
            return f'{err}'
        else:
            return ''

    if not isinstance(value, annotation):
        return f'{value} is not of type {type(annotation)}'

    return ''


def route(*_, **__) -> Callable:
    def wrapper(func) -> Callable:
        @functools.wraps(func)
        def inner(*args, **kwargs) -> Any:
            annotations = get_annotations(func)
            annot_values = annotations.values()
            errors = []

            for value, annotation in zip(args, annot_values, strict=False):
                if error := validate_annotation(value, annotation):
                    errors.append(error)

            annotations = get_sliced_dict(annotations, len(args))

            for name, value in kwargs.items():
                if annotation := annotations.get(name):
                    if error := validate_annotation(value, annotation):
                        errors.append(error)

            if errors:
                return {'errors': errors}

            return func(*args, **kwargs)

        return inner

    return wrapper
