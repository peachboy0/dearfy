import dearpygui.dearpygui as dpg
# > Dearfy
from dearfy.field import field
from dearfy.typing import Tag, Callback, Position
from dearfy.base import Item, ItemKwargs, Enableable, Showable, Variable
from dearfy.functions import get_method_needed
from dearfy.validator import ValidateKwargsAction
# > Local Imports
from typing_extensions import Unpack

# ! Input Integer Class

class InputInt(Item, Enableable, Showable, Variable[int]):
    REFERENCE_METHOD = dpg.add_input_int
    VALIDATORS_KWARGS = (ValidateKwargsAction, )
    #NODE_CONTAINERABLE = False

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
        min_value: int = 0,
        max_value: int = 100,
        step: int = 1,
        step_fast: int = 100,
        min_clamped: bool = False,
        max_clamped: bool = False,
        on_enter: bool = False,
        readonly: bool = False,
        accept_empty_input: bool = False,
        display_empty_value: bool = False,
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
            min_value=min_value,
            max_value=max_value,
            step=step,
            step_fast=step_fast,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
            accept_empty_input=accept_empty_input,
            display_empty_value=display_empty_value,
            **kwargs
        )

    def __dearfy_init__(self):
        kwargs = get_method_needed(dpg.add_input_int, **self._config)
        self._config['tag'] = dpg.add_input_int(**kwargs)
        super().__dearfy_init__()

# ! Input Float Class

class InputFloat(Item, Enableable, Showable, Variable[float]):
    REFERENCE_METHOD = dpg.add_input_float
    VALIDATORS_KWARGS = (ValidateKwargsAction, )
    #NODE_CONTAINERABLE = False

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
        default_value: float = 0,
        format: str = '%.3f',
        min_value: float = 0,
        max_value: float = 100,
        step: float = 0.1,
        step_fast: float = 1,
        min_clamped: bool = False,
        max_clamped: bool = False,
        on_enter: bool = False,
        readonly: bool = False,
        accept_empty_input: bool = False,
        display_empty_value: bool = False,
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
            format=format,
            min_value=min_value,
            max_value=max_value,
            step=step,
            step_fast=step_fast,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
            accept_empty_input=accept_empty_input,
            display_empty_value=display_empty_value,
            **kwargs
        )

    def __dearfy_init__(self):
        kwargs = get_method_needed(dpg.add_input_float, **self._config)
        self._config['tag'] = dpg.add_input_float(**kwargs)
        super().__dearfy_init__()

# ! Input Float Class

class InputDouble(Item, Enableable, Showable, Variable[float]):
    REFERENCE_METHOD = dpg.add_input_double
    VALIDATORS_KWARGS = (ValidateKwargsAction, )
    #NODE_CONTAINERABLE = False

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
        default_value: float = 0,
        format: str = '%.3f',
        min_value: float = 0,
        max_value: float = 100,
        step: float = 0.1,
        step_fast: float = 1,
        min_clamped: bool = False,
        max_clamped: bool = False,
        on_enter: bool = False,
        readonly: bool = False,
        accept_empty_input: bool = False,
        display_empty_value: bool = False,
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
            format=format,
            min_value=min_value,
            max_value=max_value,
            step=step,
            step_fast=step_fast,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
            accept_empty_input=accept_empty_input,
            display_empty_value=display_empty_value,
            **kwargs
        )

    def __dearfy_init__(self):
        kwargs = get_method_needed(dpg.add_input_double, **self._config)
        self._config['tag'] = dpg.add_input_double(**kwargs)
        super().__dearfy_init__()
