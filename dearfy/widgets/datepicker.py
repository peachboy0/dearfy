from datetime import datetime

import dearpygui.dearpygui as dpg
from typing_extensions import Unpack

from dearfy.base import Enableable, Item, ItemKwargs, Showable, Variable
from dearfy.field import field
from dearfy.functions import get_method_needed
from dearfy.typing import Callback, DateLike, DatePickerValue, Position, Tag
from dearfy.validator import ValidateKwargsAction, ValidateKwargsDate

# ! Date Picker Widget Class

class DatePicker(Item, Showable, Enableable, Variable):
    REPR_HIDDEN_KWARGS = ('callback', 'drag_callback', 'drop_callback', 'default_value')
    REFERENCE_METHOD = dpg.add_date_picker
    VALIDATORS_KWARGS = (ValidateKwargsAction, ValidateKwargsDate)

    def __init__(self,
        indent: int = -1,
        parent: Tag | None = None,
        before: Tag | None = None,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callback | None = None,
        drag_callback: Callback | None = None,
        drop_callback: Callback | None = None,
        show: bool = True,
        pos: Position | None = None,
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: DateLike | None = None,
        level: int = 0,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            indent=indent,
            parent=field(parent, 0),
            before=field(before, 0),
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=field(pos, default_factory=list),
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=field(
                default_value,
                nullable=False,
                default_factory=datetime.now,
                default_wrapped=True,
                wrap=ValidateKwargsDate._validate_value
            ),
            level=level,
            **kwargs
        )

    def __dearfy_init__(self) -> None:
        kwargs = get_method_needed(dpg.add_date_picker, **self._config)
        self._config['tag'] = dpg.add_date_picker(**kwargs)
        super().__dearfy_init__()

    @property
    def value(self) -> datetime:
        value: DatePickerValue = dpg.get_value(self.tag)
        return datetime(value['year'] + 1900, value['month'] + 1, value['month_day'])

    @value.setter
    def value(self, value: DateLike) -> None:
        dpg.set_value(self.tag, ValidateKwargsDate._validate_value(value))