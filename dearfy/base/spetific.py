from __future__ import annotations

import dearpygui.dearpygui as dpg
from typing_extensions import Generic, TypeVar  # noqa: UP035

from dearfy.base.item import Item
from dearfy.base.require_bases import RequireBasesMeta, require_bases

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
