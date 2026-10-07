import dearpygui.dearpygui as dpg
from typing_extensions import Unpack

from dearfy.base.handler import ItemHandler, ItemHandlerKwargs
from dearfy.functions import get_method_needed
from dearfy.typing import Tag

# ! Focus Item Handler Class

class HoverItemHandler(ItemHandler):
    REFERENCE_METHOD = dpg.add_item_hover_handler

    def __init__(self,
        event_type: int | None = None,
        **kwargs: Unpack[ItemHandlerKwargs]
    ) -> None:
        super().__init__(event_type=event_type, **kwargs)

    def __dearfy_handler_init__(self, parent: Tag) -> None:
        with dpg.item_handler_registry() as handler:
            kwargs = get_method_needed(dpg.add_item_hover_handler, **self._config)
            kwargs.pop('parent', None)
            self._config['tag'] = dpg.add_item_hover_handler(**kwargs)
        dpg.bind_item_handler_registry(parent, handler)