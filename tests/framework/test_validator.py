from typing import Any, Callable

import pytest
from pydantic import BaseModel

from src.framework.routes.application.dto import ValidatedDTO
from src.framework.routes.validator import DefaultAnnotationValidator


class Post(BaseModel):
    id: int
    title: str


@pytest.mark.parametrize(
    "value, annotation, res",
    (
        ("string", str, {"value": "string"}),
        (Post(id=1, title="Post"), Post, {"value": Post(id=1, title="Post")}),
        ({"id": 1, "title": "P"}, Post, {"value": Post(id=1, title="P")}),
    ),
)
def test_validate_annotation(value: Any, annotation: type, res: Any) -> None:
    rs = DefaultAnnotationValidator._validate_annotation(value, annotation)
    assert rs == res


@pytest.mark.parametrize(
    "value, annotation",
    (("string", int), ({"id": "hello", "title": "Post 1"}, Post)),
)
def test_validate_annotation_errors(value: Any, annotation: type) -> None:
    rs = DefaultAnnotationValidator._validate_annotation(value, annotation)
    assert rs.get("error")


@pytest.mark.parametrize(
    "args, annotations, res",
    (
        ([1, 2], {"a": int, "b": int}, {"args": [1, 2], "error_amount": 0}),
        ([1, 2], {"a": int, "b": str}, {"args": [1], "error_amount": 1}),
        ([1.0, 2.0], {"a": int, "b": int}, {"args": [], "error_amount": 2}),
        ([1.0, 2.0, 3], {"a": int, "b": int}, {"args": [], "error_amount": 2}),
    ),
)
def test_validate_args(args: tuple, annotations: dict, res: Any) -> None:
    default_validator = DefaultAnnotationValidator()
    validated_data = default_validator._validate_args(args, annotations)

    assert validated_data["args"] == res["args"]
    assert len(validated_data["errors"]) == res["error_amount"]


@pytest.mark.parametrize(
    "kwargs, annotations, res",
    (
        ({"name": "value"}, {"d": str}, {"kwargs": {}, "error_amount": 1}),
        (
            {"name": "value"},
            {"name": str},
            {"kwargs": {"name": "value"}, "error_amount": 0},
        ),
        (
            {"name": "value", "name2": "value2"},
            {"name": str, "name2": int},
            {"kwargs": {"name": "value"}, "error_amount": 1},
        ),
        (
            {"name": "value", "name2": "value2"},
            {"name": int, "name2": int},
            {"kwargs": {}, "error_amount": 2},
        ),
    ),
)
def test_validate_kwargs(kwargs: dict, annotations: dict, res: Any) -> None:
    default_validator = DefaultAnnotationValidator()
    validated_data = default_validator._validate_kwargs(kwargs, annotations)

    assert validated_data["kwargs"] == res["kwargs"]
    assert len(validated_data["errors"]) == res["error_amount"]


def sample_func(a: int, b: int, post: Post) -> None:
    pass


@pytest.mark.parametrize(
    "func, args, kwargs, dto",
    (
        (
            sample_func,
            (1, 2),
            {"post": {"id": 3, "title": "Post 3"}},
            ValidatedDTO(
                args=[1, 2],
                kwargs={"post": Post(id=3, title="Post 3")},
            ),
        ),
    ),
)
def test_validate(func: Callable, args: tuple, kwargs: dict, dto: Any) -> None:
    default_validator = DefaultAnnotationValidator()
    validated_dto = default_validator.validate(sample_func, args, kwargs)
    assert validated_dto == dto
