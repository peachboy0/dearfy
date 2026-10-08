from os import PathLike
from pathlib import Path, PosixPath, PurePath, PurePosixPath, PureWindowsPath, WindowsPath

import dearpygui.dearpygui as dpg
from typing_extensions import Any, Callable, Iterable, Literal, Protocol, TypeAlias  # noqa: UP035

# ! Warning Types

class ExperimentalWarning(Warning):
    pass

# ! Protocols

class DearfyObject(Protocol):
    def __dearfy_preparing__(self, app: object) -> None: ...
    def __dearfy_preinit__(self) -> None: ...
    def __dearfy_init__(self) -> None: ...
    def __dearfy_postinit__(self) -> None: ...
    def __dearfy_destroy__(self) -> None: ...


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