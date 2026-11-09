import dearpygui.dearpygui as dpg
from typing_extensions import Unpack

from dearfy.base import Item, ItemKwargs, Showable
from dearfy.field import field
from dearfy.functions import get_method_needed
from dearfy.typing import Callback, Position, Tag
from dearfy.validator import ValidateKwargsAction

# ! Child Window (Scrollable Container) Item Class

class ChildWindow(Item, Showable):
    REPR_HIDDEN_KWARGS = ('drag_callback', )
    REFERENCE_METHOD = dpg.add_child_window
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        width: int = 0,
        height: int = 0,
        indent: int = -1,
        parent: Tag | None = None,
        before: Tag | None = None,
        payload_type: str = '$$DPG_PAYLOAD',
        drag_callback: Callback | None = None,
        show: bool = True,
        pos: Position | None = None,
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        border: bool = True,
        autosize_x: bool = False,
        autosize_y: bool = False,
        no_scrollbar: bool = False,
        horizontal_scrollbar: bool = False,
        menubar: bool = False,
        no_scroll_with_mouse: bool = False,
        flattened_navigation: bool = True,
        always_use_window_padding: bool = False,
        resizable_x: bool = False,
        resizable_y: bool = False,
        always_auto_resize: bool = False,
        frame_style: bool = False,
        auto_resize_x: bool = False,
        auto_resize_y: bool = False,
        **kwargs: Unpack[ItemKwargs],
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            indent=indent,
            parent=field(parent, 0),
            before=field(before, 0),
            payload_type=payload_type,
            drag_callback=drag_callback,
            show=show,
            pos=field(pos, default_factory=list),
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            border=border,
            autosize_x=autosize_x,
            autosize_y=autosize_y,
            no_scrollbar=no_scrollbar,
            horizontal_scrollbar=horizontal_scrollbar,
            menubar=menubar,
            no_scroll_with_mouse=no_scroll_with_mouse,
            flattened_navigation=flattened_navigation,
            always_use_window_padding=always_use_window_padding,
            resizable_x=resizable_x,
            resizable_y=resizable_y,
            always_auto_resize=always_auto_resize,
            frame_style=frame_style,
            auto_resize_x=auto_resize_x,
            auto_resize_y=auto_resize_y,
            **kwargs
        )

    def __dearfy_init__(self) -> None:
        if self.containered:
            kwargs = get_method_needed(dpg.add_child_window, **self._config)
            with dpg.child_window(**kwargs) as tag:
                super().__dearfy_init__()
        else:
            kwargs = get_method_needed(dpg.add_child_window, **self._config)
            tag = dpg.add_child_window(**kwargs)
            super().__dearfy_init__()
        self._config['tag'] = tag