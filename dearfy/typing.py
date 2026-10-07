from os import PathLike
from pathlib import Path, PosixPath, PurePath, PurePosixPath, PureWindowsPath, WindowsPath

import dearpygui.dearpygui as dpg
from typing_extensions import Any, Callable, Iterable, Literal, LiteralString, TypeAlias, deprecated  # noqa: UP035

# ! Warning Types

class ExperimentalWarning(Warning):
    pass

class experimental(deprecated):
    def __init__(self, message: LiteralString, /, *, category: type[Warning] | None = None, stacklevel: int = 1):
        _category = category if (category is not None) else ExperimentalWarning
        super().__init__(message, category=_category, stacklevel=stacklevel)

# ! Constant for Type

FONT_RANGE_HINT: dict[str, int] = {
    'default': dpg.mvFontRangeHint_Default,
    'japanese': dpg.mvFontRangeHint_Japanese,
    'chinese-full': dpg.mvFontRangeHint_Chinese_Full,
    'chinese-simple': dpg.mvFontRangeHint_Chinese_Simplified_Common,
    'chinese-simplified-common': dpg.mvFontRangeHint_Chinese_Simplified_Common,
    'cyrillic': dpg.mvFontRangeHint_Cyrillic,
    'thai': dpg.mvFontRangeHint_Thai,
    'vietnamese': dpg.mvFontRangeHint_Vietnamese
}

# ! Typing

FilePath: TypeAlias     = str | PathLike[str] | Path | PosixPath | WindowsPath | PurePath | PurePosixPath | PureWindowsPath

# ! DearPyGUI Typing

Tag: TypeAlias          = str | int
Position: TypeAlias     = tuple[int, int] | Iterable[int]
Size: TypeAlias         = tuple[int, int] | Iterable[int]
Color: TypeAlias        = tuple[int, int, int, int] | Iterable[int]

FontChar: TypeAlias = int
FontRange: TypeAlias = tuple[FontChar, FontChar]
FontRangeHint: TypeAlias = Literal[
    'default',
    'japanese',
    'chinese-full', 'chinese-simple', 'chinese-simplified-common',
    'cyrillic',
    'thai',
    'vietnamese'
]

Callback: TypeAlias     = \
    Callable[[str], Any] | Callable[[str, Any | None], Any] | Callable[[str, Any | None, Any | None], Any] | str | tuple[str, str]