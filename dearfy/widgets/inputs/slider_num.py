import dearpygui.dearpygui as dpg
from typing_extensions import Unpack

from dearfy.base import Enableable, Item, ItemKwargs, Showable, Variable
from dearfy.field import field
from dearfy.functions import get_method_needed
from dearfy.typing import Callback, Position, Tag
from dearfy.validator import ValidateKwargsAction

# ! Input Slider INT Item Class

class SliderInt(Item, Enableable, Showable, Variable[int]):
    REFERENCE_METHOD = dpg.add_slider_int
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        width: int = 0,
        height: int = 0,
        indent: int = -1,
        parent: Tag | None = None,
        before: Tag | None = None,
        source: Tag | None = None,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callback | None = None,
        drag_callback: Callback | None = None,
        drop_callback: Callback | None = None,
        show: bool = True,
        enabled: bool = True,
        pos: Position | None = None,
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: int = 0,
        vertical: bool = False,
        no_input: bool = False,
        clamped: bool = False,
        min_value: int = 0,
        max_value: int = 100,
        format: str = '%d',
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            indent=indent,
            parent=field(parent, 0),
            before=field(before, 0),
            source=field(source, 0),
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=field(pos, default_factory=list),
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            vertical=vertical,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
            **kwargs
        )

    def __dearfy_init__(self):
        kwargs = get_method_needed(dpg.add_slider_int, **self._config)
        self._config['tag'] = dpg.add_slider_int(**kwargs)
        super().__dearfy_init__()

# ! Input Slider FLOAT Item Class

class SliderFloat(Item, Enableable, Showable, Variable[float]):
    REFERENCE_METHOD = dpg.add_slider_float
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        width: int = 0,
        height: int = 0,
        indent: int = -1,
        parent: Tag | None = None,
        before: Tag | None = None,
        source: Tag | None = None,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callback | None = None,
        drag_callback: Callback | None = None,
        drop_callback: Callback | None = None,
        show: bool = True,
        enabled: bool = True,
        pos: Position | None = None,
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: int = 0,
        vertical: bool = False,
        no_input: bool = False,
        clamped: bool = False,
        min_value: int = 0,
        max_value: int = 100,
        format: str = '%.3f',
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            indent=indent,
            parent=field(parent, 0),
            before=field(before, 0),
            source=field(source, 0),
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=field(pos, default_factory=list),
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            vertical=vertical,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
            **kwargs
        )

    def __dearfy_init__(self):
        kwargs = get_method_needed(dpg.add_slider_float, **self._config)
        self._config['tag'] = dpg.add_slider_float(**kwargs)
        super().__dearfy_init__()

# ! Input Slider DOUBLE Item Class

class SliderDouble(Item, Enableable, Showable, Variable[float]):
    REFERENCE_METHOD = dpg.add_slider_double
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        width: int = 0,
        height: int = 0,
        indent: int = -1,
        parent: Tag | None = None,
        before: Tag | None = None,
        source: Tag | None = None,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callback | None = None,
        drag_callback: Callback | None = None,
        drop_callback: Callback | None = None,
        show: bool = True,
        enabled: bool = True,
        pos: Position | None = None,
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: int = 0,
        vertical: bool = False,
        no_input: bool = False,
        clamped: bool = False,
        min_value: int = 0,
        max_value: int = 100,
        format: str = '%.6f',
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            indent=indent,
            parent=field(parent, 0),
            before=field(before, 0),
            source=field(source, 0),
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            pos=field(pos, default_factory=list),
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            vertical=vertical,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
            **kwargs
        )

    def __dearfy_init__(self):
        kwargs = get_method_needed(dpg.add_slider_double, **self._config)
        self._config['tag'] = dpg.add_slider_double(**kwargs)
        super().__dearfy_init__()