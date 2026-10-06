import dearpygui.dearpygui as dpg
# > Dearfy
from dearfy.field import field
from dearfy.typing import Tag, Callback, Position
from dearfy.base import Item, ItemKwargs, Enableable, Showable
from dearfy.functions import get_method_needed
from dearfy.validator import ValidateKwargsAction
# > Local Imports
from typing_extensions import Unpack

# ! Input Text Class

class InputText(Item, Enableable, Showable):
    REFERENCE_METHOD = dpg.add_input_text
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
        default_value: str = '',
        hint: str = '',
        multiline: bool = False,
        no_spaces: bool = False,
        uppercase: bool = False,
        tab_input: bool = False,
        decimal: bool = False,
        hexadecimal: bool = False,
        readonly: bool = False,
        password: bool = False,
        scientific: bool = False,
        on_enter: bool = False,
        auto_select_all: bool = False,
        ctrl_enter_for_new_line: bool = False,
        no_horizontal_scroll: bool = False,
        always_overwrite: bool = False,
        no_undo_redo: bool = False,
        escape_clears_all: bool = False,
        elide_left: bool = False,
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
            hint=hint,
            multiline=multiline,
            no_spaces=no_spaces,
            uppercase=uppercase,
            tab_input=tab_input,
            decimal=decimal,
            hexadecimal=hexadecimal,
            readonly=readonly,
            password=password,
            scientific=scientific,
            on_enter=on_enter,
            auto_select_all=auto_select_all,
            ctrl_enter_for_new_line=ctrl_enter_for_new_line,
            no_horizontal_scroll=no_horizontal_scroll,
            always_overwrite=always_overwrite,
            no_undo_redo=no_undo_redo,
            escape_clears_all=escape_clears_all,
            elide_left=elide_left,
            **kwargs
        )

    def __dearfy_init__(self) -> None:
        kwargs = get_method_needed(dpg.add_input_text, **self._config)
        self._config['tag'] = dpg.add_input_text(**kwargs)
        super().__dearfy_init__()