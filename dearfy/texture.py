from array import array
from pathlib import Path

try:
    import numpy as np
except ImportError:
    np = None

import dearpygui.dearpygui as dpg
from PIL import Image
from typing_extensions import Self, Unpack  # noqa: UP035

from dearfy.base import Item, ItemKwargs
from dearfy.field import field
from dearfy.functions import get_method_needed
from dearfy.typing import FilePath, ImageFloatData, Tag

# ! Static Texture Item Class

class StaticTexture(Item):
    REPR_HIDDEN_KWARGS = ('default_value', )
    REFERENCE_METHOD = dpg.add_static_texture
    VALIDATORS_KWARGS = ()

    def __init__(self,
        width: int,
        height: int,
        default_value: ImageFloatData,
        *,
        parent: Tag | None = None,
        **kwargs: Unpack[ItemKwargs],
    ) -> None:
        """Static texture load class. It's recommended to enter a `tag` when creating a texture.

        Args:
            width (int): Image width.
            height (int): Image height.
            default_value (ImageFloatData): An array of floating point values.
            parent (Tag | None, optional): Parent to add this item to (runtime adding). Defaults to None.
            label (str, optional): Overrides 'name' as label. Defaults to ''.
            user_data (Any | None, optional): User data for callbacks. Defaults to None.
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends #### uuid). Defaults to True.
            tag (Tag | None, optional): Unique id used to programmatically refer to the item. If label is unused this will be the label. Defaults to None.
        """
        super().__init__(
            width=width,
            height=height,
            default_value=default_value,
            parent=field(parent, default=dpg.mvReservedUUID_2, nullable=False),
            **kwargs
        )

    def __dearfy_init__(self) -> None:
        kwargs = get_method_needed(dpg.add_static_texture, **self._config)
        width, height = kwargs.pop('width'), kwargs.pop('height')
        default_value = kwargs.pop('default_value', self._config.get('default_value'))
        with dpg.texture_registry():
            self._config['tag'] = dpg.add_static_texture(width, height, default_value, **kwargs)
        super().__dearfy_init__()

    @classmethod
    def from_file(cls,
        filepath: FilePath,
        *,
        gamma: float = 1.0,
        gamma_scale_factor: float = 1.0,
        parent: Tag | None = None,
        **kwargs: Unpack[ItemKwargs]
    ) -> Self:
        width, height, channels, data = dpg.load_image(  # noqa: RUF059
            str(Path(filepath).resolve()),
            gamma=gamma,
            gamma_scale_factor=gamma_scale_factor
        )
        return cls(width, height, data, parent=parent, **kwargs)

    @classmethod
    def from_image(cls,
        img: Image.Image,
        *,
        parent: Tag | None = None,
        **kwargs: Unpack[ItemKwargs]
    ) -> Self:
        if img.mode != 'RGBA':
            img = img.convert(mode='RGBA')
        width, height = img.size
        if np is not None:
            data = (np.asarray(img, dtype=np.float32) / 255.0).ravel()
        else:
            data = array('f', (b / 255.0 for b in img.tobytes()))
        return cls(width, height, data, parent=parent, **kwargs)