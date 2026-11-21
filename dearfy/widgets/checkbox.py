import dearpygui.dearpygui as dpg
from typing_extensions import Unpack

from dearfy.base import (
    Callbackable,
    DragCallbackable,
    DropCallbackable,
    Enableable,
    FilterKeyable,
    Indentable,
    Item,
    ItemKwargs,
    Positional,
    Showable,
    Sourceable,
    TrackOffsetable,
    Variable,
)
from dearfy.field import field
from dearfy.functions import get_method_needed
from dearfy.typing import Callback, Position, Tag
from dearfy.validator import ValidateKwargsAction

# ! Checkbox Class

class Checkbox(
    Item,
    Showable,
    Enableable,
    Variable[bool],
    Callbackable,
    DragCallbackable,
    DropCallbackable,
    Positional,
    TrackOffsetable,
    FilterKeyable,
    Indentable,
    Sourceable,
):
    REPR_HIDDEN_KWARGS = ('value', 'default_value', 'callback', 'drag_callback', 'drop_callback')
    REFERENCE_METHOD = dpg.add_checkbox
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
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
        default_value: bool = False,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        """Adds a checkbox.

        Args:
            indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style. Defaults to -1.
            parent (Tag | None, optional): Parent to add this item to (runtime adding). Defaults to None.
            before (Tag | None, optional): This item will be displayed before the specified item in the parent. Defaults to None.
            source (Tag | None, optional): Overrides 'id' as value storage key. Defaults to None.
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback. Defaults to '$'.
            callback (Callback | None, optional): Registers a callback. Defaults to None.
            drag_callback (Callback | None, optional): Registers a drag callback for drag and drop. Defaults to None.
            drop_callback (Callback | None, optional): Registers a drop callback for drag and drop. Defaults to None.
            show (bool, optional): Attempt to render widget. Defaults to True.
            enabled (bool, optional): Turns off functionality of widget and applies the disabled theme. Defaults to True.
            pos (Position | None, optional): Places the item relative to window coordinates, [0,0] is top left. Defaults to None.
            filter_key (str, optional): Used by filter widget. Defaults to ''.
            tracked (bool, optional): Scroll tracking. Defaults to False.
            track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom. Defaults to 0.5.
            default_value (bool, optional): Sets the default value of the checkmark. Defaults to False.
        """
        super().__init__(
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
            **kwargs
        )

    def __dearfy_init__(self) -> None:
        kwargs = get_method_needed(dpg.add_checkbox, **self._config)
        self._config['tag'] = dpg.add_checkbox(**kwargs)
        super().__dearfy_init__()