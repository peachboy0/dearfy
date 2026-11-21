from enum import IntEnum, IntFlag  # noqa: F401

import dearpygui._dearpygui as idpg  # noqa: F401
import dearpygui.dearpygui as dpg

# ! Types

class MouseButton(IntEnum):
    LEFT        = dpg.mvMouseButton_Left
    MIDDLE      = dpg.mvMouseButton_Middle
    RIGHT       = dpg.mvMouseButton_Right
    X1          = dpg.mvMouseButton_X1
    X2          = dpg.mvMouseButton_X2

# ! Tree Node Type

class TreeNodeLines(IntEnum):
    NONE = dpg.mvTreeLines_None
    FULL = dpg.mvTreeLines_Full
    TO_NODES = dpg.mvTreeLines_ToNodes