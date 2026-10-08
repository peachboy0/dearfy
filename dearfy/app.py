import inspect
from enum import Enum

import dearpygui.dearpygui as dpg
import loguru
from typing_extensions import Any, Callable, Generator, Iterable, Iterator, TypeAlias  # noqa: UP035

from dearfy.action import Action, Actioner
from dearfy.base import DOMNode, Item
from dearfy.field import field
from dearfy.functions import formatting_kwargs, get_method_needed
from dearfy.typing import Color, FilePath, Tag, DearfyObject

# ! Types

ComposeResult: TypeAlias = Iterator[Item]
ComposeMethod: TypeAlias = Callable[[], Iterator[Item]]
Composable: TypeAlias = Item | ComposeResult | Generator[Item, Any, Any] | Iterable[Item] | ComposeMethod

# ! States

class AppState(Enum):
    NONE = 0
    PREPARING = 1
    PREINIT = 2
    INIT = 3
    POSTINIT = 4
    RUNNING = 5

# ! App Base Class

class App(DOMNode):
    _node_children: list[Item]
    _actioner: Actioner = Actioner()

    def __init__(
        self,
        title: str = 'Dearfy Viewport',
        small_icon: FilePath | None = None,
        large_icon: FilePath | None = None,
        width: int = 1280,
        height: int = 800,
        x_pos: int = 100,
        y_pos: int = 100,
        min_width: int = 250,
        max_width: int = 10000,
        min_height: int = 250,
        max_height: int = 10000,
        resizable: bool = True,
        vsync: bool = True,
        always_on_top: bool = False,
        decorated: bool = True,
        clear_color: Color = (0, 0, 0, 255),
        disable_close: bool = False,
        minimized: bool = False,
        maximized: bool = False
    ) -> None:
        super().__init__()
        self._state: AppState = AppState.NONE
        self._gkwagrs = {
            'create_viewport': {
                'title': title,
                'small_icon': field(small_icon, '', nullable=False),
                'large_icon': field(large_icon, '', nullable=False),
                'width': width,
                'height': height,
                'x_pos': x_pos,
                'y_pos': y_pos,
                'min_width': min_width,
                'max_width': max_width,
                'min_height': min_height,
                'max_height': max_height,
                'resizable': resizable,
                'vsync': vsync,
                'always_on_top': always_on_top,
                'decorated': decorated,
                'clear_color': clear_color,
                'disable_close': disable_close,
            },
            'show_viewport': {
                'minimized': minimized,
                'maximized': maximized,
            }
        }
        self.__dearfy_compose__()
        self.__dearfy_init_action_attributes__()
        self._actioner._app = self
        self._nodes.clear()
    
    def __str__(self) -> str:
        kwargs = {}
        for item_kwargs in self._gkwagrs.values():
            kwargs.update(item_kwargs)
        kwargs = get_method_needed(self.__init__, **kwargs)
        return f'{self.__class__.__name__}({formatting_kwargs(**kwargs)})'
    
    def __dearfy_init_action_attributes__(self) -> None:
        for attr_name in dir(self):
            if attr_name.startswith('action_'):
                attr = getattr(self, attr_name)
                if isinstance(attr, Action):
                    continue
                elif callable(attr):
                    self._actioner.add_action(attr, attr_name[7:])
    
    def __dearfy_compose__(self) -> None:
        self._nodes.append(self)
        for child in self.compose():
            if self._current_node:
                self._current_node._add_child(child)
        self._nodes.clear()
    
    def __dearfy_preparing__(self) -> None:
        for child in self._node_children:
            child.__dearfy_preparing__(self)
        self.on_preparing()

    def __dearfy_preinit__(self) -> None:
        for child in self._node_children:
            child.__dearfy_preinit__()
        self.before_init()
    
    def __dearfy_init__(self) -> None:
        for child in self._node_children:
            child.__dearfy_init__()
        self.on_init()
    
    def __dearfy_postinit__(self) -> None:
        for child in self._node_children:
            child.__dearfy_postinit__()
        self.after_init()
    
    def __dearfy_destroy__(self) -> None:
        for child in self._node_children:
            child.__dearfy_destroy__()
    
    def get_item(self, tag: Tag) -> Item:
        try:
            return self._node_main_parent._get_node_by_attr('tag', tag)
        except AttributeError:
            pass
        raise RuntimeError(
            "There is no Item with this tag. "
            f"_node_main_parent={self._node_main_parent!r}"
        )

    @staticmethod
    def _dearfy_obejct_init(app: 'App', obj: DearfyObject) -> None:
        if not bool(obj._state & 0b0001):           obj.__dearfy_preparing__(app)
        if not bool((obj._state & 0b0010) >> 1):    obj.__dearfy_preinit__()
        if not bool((obj._state & 0b0100) >> 2):    obj.__dearfy_init__()
        if not bool((obj._state & 0b1000) >> 3):    obj.__dearfy_postinit__()

    def push_item_to(self, obj: Composable, *, parent: Tag | None = None) -> None:
        parent_item: Item | App = self._get_node_by_attr('tag', parent) if parent is not None else self
        if isinstance(obj, Item):
            if parent is not None:
                obj._config['parent'] = parent
            parent_item._add_child(obj)
            self._dearfy_obejct_init(self, obj)
            return
        elif isinstance(obj, (Iterator, Iterable, Generator)):
            for item in obj:
                if parent is not None:
                    item._config['parent'] = parent
                parent_item._add_child(item)
                self._dearfy_obejct_init(self, item)
            return
        elif inspect.isgeneratorfunction(obj):
            for item in obj():
                if parent is not None:
                    item._config['parent'] = parent
                parent_item._add_child(item)
                self._dearfy_obejct_init(self, item)
            return
        elif inspect.isgenerator(obj):
            for item in obj:
                if parent is not None:
                    item._config['parent'] = parent
                parent_item._add_child(item)
                self._dearfy_obejct_init(self, item)
            return
        raise RuntimeWarning(f"Couldn't get Item from the object ({obj}).")

    def push_item(self, obj: Composable) -> None:
        self.push_item_to(obj)

    def set_primary_window(self, window: Tag, value: bool) -> None:
        dpg.set_primary_window(window, value)

    def bind_font(self, font: Tag) -> None:
        dpg.bind_font(font)

    def bind_item_font(self, item: Tag, font: Tag) -> None:
        dpg.bind_item_font(item, font)

    def show_font_manager(self) -> None:
        """Shows a debug tool for the font manager."""
        dpg.show_font_manager()
    
    def show_about(self) -> None:
        """Shows the standard about window."""
        dpg.show_about()

    def show_metrics(self) -> None:
        """Shows the standard metrics window."""
        dpg.show_metrics()

    def show_item_registry(self) -> None:
        """Shows the item hierarchy of your application."""
        dpg.show_item_registry()

    def show_debug(self) -> None:
        """Shows the standard debug window."""
        dpg.show_debug()

    def on_ready(self) -> None:
        """Called after full initialization, before the main loop starts."""

    def on_preparing(self) -> None:
        """Called before initialization, when the context has NOT yet been created."""

    def on_init(self) -> None:
        """Called during initialization."""

    def after_init(self) -> None:
        """Called after initialization (postinit)."""

    def before_init(self) -> None:
        """Called before initialization, but after the context has ALREADY been created."""

    def run(self) -> None:
        self._state = AppState.PREPARING
        self.__dearfy_preparing__()
        loguru.logger.trace('[green]▬▬▬▬▬[/green] [yellow]AFTER PREPARING[/yellow] [green]▬▬▬▬▬[/green]')
        loguru.logger.trace(self._to_rich_tree())
        dpg.create_context()
        dpg.create_viewport(**(self._gkwagrs['create_viewport']))
        self._state = AppState.PREINIT
        self.__dearfy_preinit__()
        loguru.logger.trace('[green]▬▬▬▬▬[/green] [yellow]AFTER PREINIT[/yellow] [green]▬▬▬▬▬[/green]')
        loguru.logger.trace(self._to_rich_tree())
        self._state = AppState.INIT
        self.__dearfy_init__()
        loguru.logger.trace('[green]▬▬▬▬▬[/green] [yellow]AFTER INIT[/yellow] [green]▬▬▬▬▬[/green]')
        loguru.logger.trace(self._to_rich_tree())
        dpg.setup_dearpygui()
        self._state = AppState.POSTINIT
        self.__dearfy_postinit__()
        loguru.logger.trace('[green]▬▬▬▬▬[/green] [yellow]AFTER POSTINIT[/yellow] [green]▬▬▬▬▬[/green]')
        loguru.logger.trace(self._to_rich_tree())
        self._state = AppState.RUNNING
        dpg.show_viewport(**(self._gkwagrs['show_viewport']))
        self.on_ready()
        dpg.start_dearpygui()
        dpg.destroy_context()
        self._state = AppState.NONE
        self.__dearfy_destroy__()
        loguru.logger.trace(self._to_rich_tree())

action = App._actioner.action 