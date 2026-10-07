import dearpygui.dearpygui as dpg
from typing_extensions import Unpack

from dearfy.base.handler import ItemHandler, ItemHandlerKwargs
from dearfy.functions import get_method_needed
from dearfy.typing import Tag

# ! Toggle Open Item Handler Class

class ToggleOpenItemHandler(ItemHandler):
    REFERENCE_METHOD = dpg.add_item_toggled_open_handler

    def __init__(self,
        two_way: bool = False,
        **kwargs: Unpack[ItemHandlerKwargs]
    ) -> None:
        super().__init__(
            two_way=two_way,
            **kwargs
        )

    def __dearfy_handler_init__(self, parent: Tag) -> None:
        with dpg.item_handler_registry() as handler:
            kwargs = get_method_needed(dpg.add_item_toggled_open_handler, **self._config)
            kwargs.pop('parent', None)
            self._config['tag'] = dpg.add_item_toggled_open_handler(**kwargs)
        dpg.bind_item_handler_registry(parent, handler) 