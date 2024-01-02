from collections.abc import Callable, Mapping
from typing import Any

from pydantic import BaseModel, ValidationError

from src.framework.helpers.get_annotations import get_annotations
from src.framework.helpers.get_sliced_dict import get_sliced_dict
from src.framework.routes.application.ports import IAnnotationValidator


class AnnotationValidator(IAnnotationValidator):
    errors = {}

    def _validate_annotation(
        self, value: Any, annotation: Any, metadata: dict
    ) -> None:
        if isinstance(value, annotation):
            return

        if issubclass(annotation, BaseModel):
            if isinstance(value, Mapping):
                try:
                    annotation(**value)
                    return
                except ValidationError:
                    self.errors |= {
                        "message": "Data is not for a BaseModel subclass",
                        "metadata": metadata,
                    }
                    return
            else:
                self.errors |= {
                    "message": f"Value {value} doesn't support mapping",
                    "metadata": metadata,
                }
                return

        self.errors |= {
            "message": f"Value {value} is not of type {type(annotation)}",
            "metadata": metadata,
        }

    def _validate_args(self, args: tuple, annotations: dict) -> None:
        for value, annotation in zip(args, annotations.values(), strict=False):
            self._validate_annotation(
                value,
                annotation,
                metadata={
                    "value": value,
                },
            )

    def _validate_kwargs(self, kwargs: dict, annotations: dict) -> None:
        for name, value in kwargs.items():
            if annotation := annotations.get(name):
                self._validate_annotation(
                    value,
                    annotation,
                    metadata={
                        "value": value,
                        "name": name,
                    },
                )
            else:
                raise ValueError(f"Argument for {name} does not exist")

    def validate(self, func: Callable, args: Any, kwargs: Any) -> dict:
        annotations = get_annotations(func)
        kwargs_annotations = get_sliced_dict(annotations, len(args))

        self._validate_args(args, annotations)
        self._validate_kwargs(kwargs, kwargs_annotations)
        return self.errors
