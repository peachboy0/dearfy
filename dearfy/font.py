import loguru
import dearpygui.dearpygui as dpg
# > System
from pathlib import Path
# > Dearfy
from dearfy.field import field
from dearfy.base import Item, ItemKwargs
from dearfy.functions import get_method_needed
from dearfy.typing import Tag, FilePath, FontChar, FontRange, FontRangeHint, FONT_RANGE_HINT
# > Local Imports
from typing_extensions import Unpack, Iterable, deprecated

# ! Font Class

class Font(Item):
    REFERENCE_METHOD = dpg.add_font
    VALIDATORS_KWARGS = ()

    def __init__(self,
        file: FilePath,
        size: int,
        *,
        parent: Tag | None = None,
        pixel_snapH: bool = False,
        pixel_snapV: bool = False,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            file=str(Path(file).resolve()),
            size=size,
            parent=field(parent, 0),
            pixel_snapH=pixel_snapH,
            pixel_snapV=pixel_snapV,
            **kwargs
        )

    def __dearfy_init__(self) -> None:
        kwargs = get_method_needed(dpg.add_font, **self._config)
        with dpg.font_registry():
            self._config['tag'] = dpg.add_font(**kwargs)
        super().__dearfy_init__()

# ! Spetific Font Class

@deprecated('Use class `Font` (operates automatically)')
class SpetificFont(Item):
    REFERENCE_METHOD = dpg.add_font
    VALIDATORS_KWARGS = ()

    def __init__(self,
        file: FilePath,
        size: int,
        *,
        font_chars: Iterable[FontChar] | None = None,
        font_ranges: Iterable[FontRange] | None = None,
        font_range_hints: Iterable[FontRangeHint] | None = None,
        parent: Tag | None = None,
        pixel_snapH: bool = False,
        pixel_snapV: bool = False,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            file=str(Path(file).resolve()),
            size=size,
            parent=field(parent, 0),
            pixel_snapH=pixel_snapH,
            pixel_snapV=pixel_snapV,
            **kwargs
        )
        self._fonts_chars = field(font_chars, default_factory=list, nullable=False)
        self._fonts_ranges = field(font_ranges, default_factory=list, nullable=False)
        self._fonts_range_hints = field(font_range_hints, default_factory=list, nullable=False)
    
    def __dearfy_init__(self) -> None:
        kwargs = get_method_needed(dpg.add_font, **self._config)
        with dpg.font_registry():
            loguru.logger.trace(f'{self}.__dearfy_init__(): Font registry...')
            if (len(self._fonts_chars) + len(self._fonts_ranges) + len(self._fonts_range_hints)) > 0:
                loguru.logger.trace(f'{self}._fonts_chars = {self._fonts_chars!r}')
                loguru.logger.trace(f'{self}._fonts_ranges = {self._fonts_ranges!r}')
                loguru.logger.trace(f'{self}._fonts_range_hints = {self._fonts_range_hints!r}')
                with dpg.font(**kwargs) as tag:
                    if len(self._fonts_chars) > 0:
                        dpg.add_font_chars(self._fonts_chars)
                    if len(self._fonts_ranges) > 0:
                        for first_char, last_char in self._fonts_ranges:
                            dpg.add_font_range(first_char, last_char)
                    if len(self._fonts_range_hints) > 0:
                        for range_hint_key in self._fonts_range_hints:
                            dpg.add_font_range_hint(FONT_RANGE_HINT[range_hint_key])
            else:
                tag = dpg.add_font(**kwargs)
            self._config['tag'] = tag
        super().__dearfy_init__()

