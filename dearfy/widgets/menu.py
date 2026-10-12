import dearpygui.dearpygui as dpg
from typing_extensions import Unpack

from dearfy.base import Enableable, Item, ItemKwargs, Showable
from dearfy.field import field
from dearfy.functions import get_method_needed
from dearfy.typing import Callback, Tag
from dearfy.validator import ValidateKwargsAction

# ! Menu Bar Item Class

class MenuBar(Item, Showable):
    REFERENCE_METHOD = dpg.add_menu_bar
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        indent: int = -1,
        parent: Tag | None = None,
        show: bool = True,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            indent=indent,
            parent=field(parent, 0),
            show=show,
            **kwargs
        )

    def __dearfy_init__(self) -> None:
        kwargs = get_method_needed(dpg.add_menu_bar, **self._config)
        if self.containered:
            with dpg.menu_bar(**kwargs) as tag:
                super().__dearfy_init__()
            self._config['tag'] = tag
        else:
            tag = dpg.add_menu_bar(**kwargs)
            super().__dearfy_init__()
        self._config['tag'] = tag

# ! Menu Item Class

class Menu(Item, Showable, Enableable):
    REFERENCE_METHOD = dpg.add_menu
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        indent: int = -1,
        parent: Tag | None = None,
        before: Tag | None = None,
        payload_type: str = '$$DPG_PAYLOAD',
        drop_callback: Callback | None = None,
        show: bool = True,
        enabled: bool = True,
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            indent=indent,
            parent=field(parent, 0),
            before=field(before, 0),
            payload_type=payload_type,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            **kwargs
        )

    def __dearfy_init__(self) -> None:
        kwargs = get_method_needed(dpg.add_menu, **self._config)
        if self.containered:
            with dpg.menu(**kwargs) as tag:
                super().__dearfy_init__()
            self._config['tag'] = tag
        else:
            tag = dpg.add_menu(**kwargs)
            super().__dearfy_init__()
        self._config['tag'] = tag