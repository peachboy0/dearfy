import dearpygui.dearpygui as dpg
from typing_extensions import Unpack

from dearfy.base import Item, ItemKwargs
from dearfy.exceptions import DearfyNoContentException
from dearfy.field import field
from dearfy.functions import get_method_needed
from dearfy.typing import Size, Tag
from dearfy.validator import ValidateKwargsAction

# ! Popup Item Class

class Popup(Item):
    REFERENCE_METHOD = dpg.popup
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        parent: Tag,
        mousebutton: int = dpg.mvMouseButton_Right,
        modal: bool = False,
        tag: Tag | None = None,
        min_size: Size | None = None,
        max_size: Size | None = None,
        no_move: bool = False,
        no_background: bool = False,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            parent=parent,
            mousebutton=mousebutton,
            modal=modal,
            tag=field(tag, default=0),
            min_size=field(min_size, default=[100, 100]),
            max_size=field(max_size, default=[30000, 30000]),
            no_move=no_move,
            no_background=no_background,
            **kwargs
        )

    def __dearfy_init__(self) -> None:
        kwargs = get_method_needed(dpg.add_window, **self._config)
        if not self.containered:
            raise DearfyNoContentException("The object has no content.")
        with dpg.popup(**kwargs) as tag:
            self.__dearfy_init__()
        self._config['tag'] = tag
        