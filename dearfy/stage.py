import dearpygui.dearpygui as dpg

# > Typing
from typing_extensions import Unpack, deprecated

# > Dearfy
from dearfy.base import Item, ItemKwargs
from dearfy.functions import get_method_needed
from dearfy.typing import ExperimentalWarning

# ! Stage Class

@deprecated('[EXPERIMENTAL] There is no certainty regarding the stability of this function.', category=ExperimentalWarning)
class Stage(Item):
    REFERENCE_METHOD = dpg.add_stage

    def __init__(self,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(**kwargs)

    def __dearfy_init__(self):
        kwargs = get_method_needed(dpg.add_stage, **self._config)
        if len(self._node_children) > 0:
            with dpg.stage(**kwargs) as tag:
                super().__dearfy_init__()
        else:
            tag = dpg.add_stage(**kwargs)
        self._config['tag'] = tag