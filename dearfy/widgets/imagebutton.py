import dearpygui.dearpygui as dpg
from typing_extensions import Unpack

from dearfy.base import (
    Callbackable,
    DragCallbackable,
    DropCallbackable,
    Enableable,
    FilterKeyable,
    Heightable,
    Indentable,
    Item,
    ItemKwargs,
    Positional,
    Showable,
    Sourceable,
    TrackOffsetable,
    Widthable,
)
from dearfy.field import field
from dearfy.functions import get_method_needed
from dearfy.typing import Callback, FloatColor, FloatSize, Position, Tag
from dearfy.validator import ValidateKwargsAction

# ! Image Button Item Class

class ImageButton(
    Item,
    Showable,
    Enableable,
    Callbackable,
    DragCallbackable,
    DropCallbackable,
    FilterKeyable,
    Heightable,
    Indentable,
    Positional,
    TrackOffsetable,
    Widthable,
    Sourceable,
):
    REPR_HIDDEN_KWARGS = ('drag_callback', 'drop_callback', 'callback')
    REFERENCE_METHOD = dpg.add_image_button
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        texture_tag: Tag,
        *,
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
        tint_color: FloatColor | None = None,
        background_color: FloatColor | None = None,
        uv_min: FloatSize | None = None,
        uv_max: FloatSize | None = None,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            texture_tag=texture_tag,
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
            tint_color=field(tint_color, default=(255, 255, 255, 255), nullable=False),
            background_color=field(background_color, default=(0, 0, 0, 0), nullable=False),
            uv_min=field(uv_min, default=(0., 0.), nullable=False),
            uv_max=field(uv_max, default=(1., 1.), nullable=False),
            **kwargs
        )

    def __dearfy_init__(self) -> None:
        kwargs = get_method_needed(dpg.add_image_button, **self._config)
        texture_tag = kwargs.pop('texture_tag')
        self._config['tag'] = dpg.add_image_button(texture_tag, **kwargs)
        super().__dearfy_init__()