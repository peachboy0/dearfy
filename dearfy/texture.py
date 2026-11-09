from pathlib import Path

import dearpygui.dearpygui as dpg
from PIL import Image
from typing_extensions import Self, Unpack  # noqa: UP035

from dearfy.base import Item, ItemKwargs
from dearfy.functions import get_method_needed
from dearfy.typing import FilePath, ImageData, Tag

# ! Static Texture Item Class

class StaticTexture(Item):
    REPR_HIDDEN_KWARGS = ('default_value', )
    REFERENCE_METHOD = dpg.add_static_texture
    VALIDATORS_KWARGS = ()

    def __init__(self,
        width: int,
        height: int,
        default_value: ImageData,
        *,
        parent: Tag | None = None,
        **kwargs: Unpack[ItemKwargs],
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            default_value=default_value,
            parent=parent,
            **kwargs
        )

    def __dearfy_init__(self) -> None:
        kwargs = get_method_needed(dpg.add_static_texture, **self._config)
        with dpg.texture_registry(show=True):
            self._config['tag'] = dpg.add_static_texture(**kwargs)
        super().__dearfy_init__()

    @classmethod
    def from_file(cls, filepath: FilePath) -> Self:
        width, height, channels, data = dpg.load_image(str(Path(filepath).resolve(strict=True)))
        return cls(width, height, data)