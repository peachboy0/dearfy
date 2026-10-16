from enum import Enum

import dearpygui.dearpygui as dpg
from typing_extensions import Unpack

from dearfy.base import Item, ItemKwargs, Showable
from dearfy.field import field
from dearfy.functions import get_method_needed
from dearfy.typing import Callback, Position, Tag
from dearfy.validator import ValidateKwargsAction

# ! Types

class TreeNodeLines(Enum):
    NONE = dpg.internal_dpg.mvTreeLines_None
    FULL = dpg.internal_dpg.mvTreeLines_Full
    TO_NODES = dpg.internal_dpg.mvTreeLines_ToNodes

# ! Tree Node Item Class

class TreeNode(Item, Showable):
    REPR_HIDDEN_KWARGS = ('drag_callback', 'drop_callback')
    REFERENCE_METHOD = dpg.add_tree_node
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        indent: int = -1,
        parent: Tag | None = None,
        before: Tag | None = None,
        payload_type: str = '$$DPG_PAYLOAD',
        drag_callback: Callback | None = None,
        drop_callback: Callback | None = None,
        show: bool = True,
        pos: Position | None = None,
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_open: bool = False,
        open_on_double_click: bool = False,
        open_on_arrow: bool = False,
        leaf: bool = False,
        bullet: bool = False,
        selectable: bool = False,
        span_text_width: bool = False,
        span_full_width: bool = False,
        catch_nav_left: bool = False,
        lines: TreeNodeLines | int = TreeNodeLines.NONE,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            indent=indent,
            parent=field(parent, 0),
            before=field(before, 0),
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_open=default_open,
            open_on_double_click=open_on_double_click,
            open_on_arrow=open_on_arrow,
            leaf=leaf,
            bullet=bullet,
            selectable=selectable,
            span_text_width=span_text_width,
            span_full_width=span_full_width,
            catch_nav_left=catch_nav_left,
            lines=lines,
            **kwargs
        )

    def __dearfy_init__(self) -> None:
        kwargs = get_method_needed(dpg.add_tree_node, **self._config)
        if self.containered:
            with dpg.tree_node(**kwargs) as tag:
                super().__dearfy_init__()
        else:
            tag = dpg.add_tree_node(**kwargs)
            super().__dearfy_init__()
        self._config['tag'] = tag
        