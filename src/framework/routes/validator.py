from collections.abc import Callable
from typing import Any

from pydantic import BaseModel, ValidationError, PydanticUserError

from src.framework.helpers.get_annotations import get_annotations
from src.framework.helpers.get_sliced_dict import get_sliced_dict
from src.framework.routes.application.dto import ValidatedDTO
from src.framework.routes.application.ports import IAnnotationValidator


class DefaultAnnotationValidator(IAnnotationValidator):
    @staticmethod
    def _validate_annotation(value: Any, annotation: Any) -> dict:
        if isinstance(value, annotation):
            return {"value": value}

        if issubclass(annotation, BaseModel):
            try:
                value = annotation(**value)
                return {"value": value}
            except (ValidationError, PydanticUserError) as err:
                return {"error": f"{err}"}
        else:
            return {"error": f"{value} is not of type {type(annotation)}"}

    def _validate_args(self, args: tuple, annotations: dict) -> dict:
        valid_args, errors = [], []

        # if difference < 0: ...

        for value, annotation in zip(args, annotations.values(), strict=False):
            if data := self._validate_annotation(value, annotation):
                if value := data.get("value"):
                    valid_args.append(value)
                if error := data.get("error"):
                    errors.append(error)

        return {"args": valid_args, "errors": errors}

    def _validate_kwargs(self, kwargs: dict, annotations: dict) -> dict:
        valid_kwargs, errors = {}, []

        for name, value in kwargs.items():
            if annotation := annotations.get(name):
                if data := self._validate_annotation(value, annotation):
                    if value := data.get("value"):
                        valid_kwargs[name] = value
                    if error := data.get("error"):
                        errors.append(error)
            else:
                errors.append("This argument wasn't defined in function.")

        return {"kwargs": valid_kwargs, "errors": errors}

    def validate(self, func: Callable, args: Any, kwargs: Any) -> ValidatedDTO:
        annotations = get_annotations(func)
        kwargs_annotations = get_sliced_dict(annotations, len(args))

        args_data = self._validate_args(args, annotations)
        kwargs_data = self._validate_kwargs(kwargs, kwargs_annotations)

        validated_data = {
            "args": args_data["args"],
            "kwargs": kwargs_data["kwargs"],
            "errors": args_data["errors"] + kwargs_data["errors"],
        }
        return ValidatedDTO(**validated_data)
