import inspect
from collections.abc import Callable


def get_non_magic_methods(self) -> list[Callable]:
    return [getattr(self, method) for method in dir(self)
            if (inspect.ismethod(getattr(self, method))
                and not method.startswith('__'))]
