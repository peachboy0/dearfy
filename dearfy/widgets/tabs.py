import dearpygui.dearpygui as dpg
from typing_extensions import Unpack

from dearfy.base import Item, ItemKwargs, Showable
from dearfy.field import field
from dearfy.functions import get_method_needed
from dearfy.typing import Callback, Position, Tag
from dearfy.validator import ValidateKwargsAction

# ! Tab Bar Item Class

class TabBar(Item, Showable):
    REFERENCE_METHOD = dpg.add_tab_bar
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        indent: int = -1,
        parent: Tag | None = None,
        before: Tag | None = None,
        callback: Callback | None = None,
        show: bool = True,
        pos: Position | None = None,
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        reorderable: bool = False,
        tab_list_popup_button: bool = False,
        no_close_with_middle_click: bool = False,
        no_scrolling_buttons: bool = False,
        no_tooltip: bool = False,
        draw_selected_overline: bool = False,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            indent=indent,
            parent=field(parent, 0),
            before=field(before, 0),
            callback=callback,
            show=show,
            pos=field(pos, default_factory=list),
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            reorderable=reorderable,
            tab_list_popup_button=tab_list_popup_button,
            no_close_with_middle_click=no_close_with_middle_click,
            no_scrolling_buttons=no_scrolling_buttons,
            no_tooltip=no_tooltip,
            draw_selected_overline=draw_selected_overline,
            **kwargs
        )

    def __dearfy_init__(self):
        kwargs = get_method_needed(dpg.add_tab_bar, **self._config)
        if self.containered:
            with dpg.tab_bar(**kwargs) as tag:
                super().__dearfy_init__()
        else:
            tag = dpg.add_tab_bar(**kwargs)
            super().__dearfy_init__()
        self._config['tag'] = tag

# ! Tab Item Class

class Tab(Item):
    REFERENCE_METHOD = dpg.add_tab
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        indent: int = -1,
        parent: int | str = 0,
        before: int | str = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        drop_callback: Callback | None = None,
        show: bool = True,
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        closable: bool = False,
        no_tooltip: bool = False,
        order_mode: int = 0,
        unsaved_document: bool = False,
        no_close_with_middle_click: bool = False,
        no_reorder: bool = False,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            indent=indent,
            parent=field(parent, 0),
            before=field(before, 0),
            payload_type=payload_type,
            drop_callback=drop_callback,
            show=show,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            closable=closable,
            no_tooltip=no_tooltip,
            order_mode=order_mode,
            unsaved_document=unsaved_document,
            no_close_with_middle_click=no_close_with_middle_click,
            no_reorder=no_reorder,
            **kwargs
        )

    def __dearfy_init__(self):
        kwargs = get_method_needed(dpg.add_tab, **self._config)
        if self.containered:
            with dpg.tab(**kwargs) as tag:
                super().__dearfy_init__()
        else:
            tag = dpg.add_tab(**kwargs)
            super().__dearfy_init__()
        self._config['tag'] = tag