import dearpygui.dearpygui as dpg
from typing_extensions import Unpack

from dearfy.base import Item, ItemKwargs, Showable
from dearfy.field import field
from dearfy.functions import get_method_needed
from dearfy.typing import Position, Tag
from dearfy.validator import ValidateKwargsAction

# ! Separator Item Class

class Separator(Item, Showable):
    REFERENCE_METHOD = dpg.add_separator
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        indent: int = -1,
        parent: Tag | None = None,
        before: Tag | None = None,
        show: bool = True,
        pos: Position | None = None,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            indent=indent,
            parent=field(parent, 0),
            before=field(before, 0),
            show=show,
            pos=field(pos, default_factory=list),
            **kwargs
        )

    def __dearfy_init__(self) -> None:
        kwargs = get_method_needed(dpg.add_separator, **self._config)
        self._config['tag'] = dpg.add_separator(**kwargs)
        super().__dearfy_init__()