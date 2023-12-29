from src.framework.helpers.get_annotations import get_annotations
from src.framework.helpers.get_sliced_dict import get_sliced_dict


def test_get_annotations() -> None:
    def some_func(param: str) -> str:
        return param

    annotations = get_annotations(some_func)
    assert annotations.get("return") is None
    assert len(annotations) == 1


def test_sliced_dict() -> None:
    sliced_dict = get_sliced_dict({"a": 1, "b": 2, "c": 3, "d": 4}, 2)
    assert sliced_dict == {"c": 3, "d": 4}
