import dearpygui.dearpygui as dpg
from typing_extensions import Iterable, Unpack  # noqa: UP035

from dearfy.base import Enableable, Item, ItemKwargs, Showable, Variable
from dearfy.field import field
from dearfy.functions import get_method_needed
from dearfy.typing import Callback, Position, Tag
from dearfy.validator import ValidateKwargsAction

# ! Combo Item Class

class Combo(Item, Showable, Enableable, Variable[str]):
    REPR_HIDDEN_KWARGS = ('callback', 'drag_callback', 'drop_callback')
    REFERENCE_METHOD = dpg.add_combo
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        items: Iterable[str] | None = None,
        *,
        width: int = 0,
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
        default_value: str = '',
        popup_align_left: bool = False,
        no_arrow_button: bool = False,
        no_preview: bool = False,
        fit_width: bool = False,
        height_mode: int = 1,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            items=field(items, default_factory=list, nullable=False, wrap=tuple, default_wrapped=True),
            width=width,
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
            popup_align_left=popup_align_left,
            no_arrow_button=no_arrow_button,
            no_preview=no_preview,
            fit_width=fit_width,
            height_mode=height_mode,
            **kwargs
        )

    def __dearfy_init__(self) -> None:
        kwargs = get_method_needed(dpg.add_combo, **self._config)
        self._config['tag'] = dpg.add_combo(**kwargs)
        super().__dearfy_init__()