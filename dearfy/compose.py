# > Typing
from typing_extensions import Callable, Iterator  # noqa: UP035

from dearfy.base import Item

# ! ...

class Composer:
    def __init__(self, app: object | None = None) -> None:
        self._app = app
        self.composes = []

    def __str__(self) -> str:
        return '{}({})'.format(
            self.__class__.__name__,
            f"[...+{len(self.composes)}]" if len(self.composes) > 0 else "[]"
        )
    
    def __repr__(self) -> str:
        return self.__str__()

    def add_compose(self) -> str:
        ...

class Compose:
    def __init__(self, app: object, method: Callable[..., Iterator[Item]]) -> None:
        self.app = app
        self.method = method

    def __call__(self, *args: object, **kwds: object) -> None:
        pass