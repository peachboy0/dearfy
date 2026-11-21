from __future__ import annotations

import dearpygui.dearpygui as dpg
from typing_extensions import Generic, TypeVar  # noqa: UP035

from dearfy.base.item import Item
from dearfy.base.require_bases import RequireBasesMeta, require_bases
from dearfy.typing import Callback, Position, Tag

# ! Type Vars

_T = TypeVar('_T')

# ! Enableable Spetific Class

@require_bases(Item)
class Enableable(metaclass=RequireBasesMeta):
    @property
    def enabled(self) -> bool:
        return bool(dpg.is_item_enabled(self.tag))

    def enable(self) -> None:
        dpg.enable_item(self.tag)

    def disable(self) -> None:
        dpg.disable_item(self.tag)

# ! Showable Spetific Class

@require_bases(Item)
class Showable(metaclass=RequireBasesMeta):
    @property
    def shown(self) -> bool:
        return dpg.is_item_shown(self.tag)

    def show(self) -> None:
        dpg.show_item(self.tag)
    
    def hide(self) -> None:
        dpg.hide_item(self.tag)

# ! Variable Spetific Class

@require_bases(Item)
class Variable(Generic[_T], metaclass=RequireBasesMeta):
    @property
    def value(self) -> _T:
        return dpg.get_value(self._config['tag'])

    @value.setter
    def value(self, v: _T) -> None:
        dpg.set_value(self._config['tag'], v)

# ! Callable Spetific Class

@require_bases(Item)
class Callbackable(metaclass=RequireBasesMeta):
    @property
    def callback(self) -> Callback | None:
        return dpg.get_item_callback(self._config['tag'])

    @callback.setter
    def callback(self, value: Callback | None) -> None:
        dpg.set_item_callback(self._config['tag'], value)

# ! Drag Callable Spetific Class

@require_bases(Item)
class DragCallbackable(metaclass=RequireBasesMeta):
    @property
    def drag_callback(self) -> Callback | None:
        return dpg.get_item_drag_callback(self._config['tag'])

    @drag_callback.setter
    def drag_callback(self, value: Callback | None) -> None:
        dpg.set_item_drag_callback(self._config['tag'], value)

# ! Drop Callable Spetific Class

@require_bases(Item)
class DropCallbackable(metaclass=RequireBasesMeta):
    @property
    def drop_callback(self) -> Callback | None:
        return dpg.get_item_drop_callback(self._config['tag'])

    @drop_callback.setter
    def drop_callback(self, value: Callback | None) -> None:
        dpg.set_item_drop_callback(self._config['tag'], value)

# ! Height Spetific Class

@require_bases(Item)
class Heightable(metaclass=RequireBasesMeta):
    @property
    def height(self) -> int:
        return dpg.get_item_height(self._config['tag'])

    @height.setter
    def height(self, value: int) -> None:
        dpg.set_item_height(self._config['tag'], value)

# ! Width Spetific Class

@require_bases(Item)
class Widthable(metaclass=RequireBasesMeta):
    @property
    def width(self) -> int:
        return dpg.get_item_width(self._config['tag'])

    @width.setter
    def width(self, value: int) -> None:
        dpg.set_item_width(self._config['tag'], value)

# ! Position Spetific Class

@require_bases(Item)
class Positional(metaclass=RequireBasesMeta):
    @property
    def pos(self) -> Position:
        return dpg.get_item_pos(self._config['tag'])

    @pos.setter
    def pos(self, value: Position) -> None:
        dpg.set_item_pos(self._config['tag'])

# ! Track Offset Spetific Class

@require_bases(Item)
class TrackOffsetable(metaclass=RequireBasesMeta):
    @property
    def track_offset(self) -> float | None:
        return dpg.get_item_track_offset(self._config['tag'])

    @track_offset.setter
    def track_offset(self, value: float | None) -> None:
        dpg.set_item_track_offset(self._config['tag'], value)

# ! Filter Key Spetific Class

@require_bases(Item)
class FilterKeyable(metaclass=RequireBasesMeta):
    @property
    def filter_key(self) -> str | None:
        return dpg.get_item_filter_key(self._config['tag'])

    # TODO: С setter что-то непонятное, нету функции

# ! Indent Spetific Class

@require_bases(Item)
class Indentable(metaclass=RequireBasesMeta):
    @property
    def indent(self) -> int:
        return dpg.get_item_indent(self._config['tag'])

    @indent.setter
    def indent(self, value: int | None) -> None:
        dpg.set_item_indent(value)

# ! Source Spetific Class

@require_bases
class Sourceable(metaclass=RequireBasesMeta):
    @property
    def source(self) -> Tag | None:
        return dpg.get_item_source(self._config['tag'])

    @source.setter
    def source(self, value: Tag | None) -> None:
        dpg.set_item_source(self._config['tag'], value)