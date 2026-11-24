import inspect
from enum import Enum
from pathlib import Path

import dearpygui.dearpygui as dpg
import loguru
from typing_extensions import Any, Callable, Generator, Iterable, Iterator, TypeAlias  # noqa: UP035

import dearfy.icon
from dearfy.action import Action, Actioner
from dearfy.base import DOMNode, Item
from dearfy.field import field
from dearfy.font import Font
from dearfy.functions import formatting_kwargs, generator_safe, get_method_needed
from dearfy.typing import Color, DearfyObject, FilePath, Tag
from dearfy.widgets import *

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
        icon_path = dearfy.icon.get_icon_path()
        self._gkwagrs = {
            'create_viewport': {
                'title': title,
                'small_icon': field(small_icon, icon_path, nullable=False),
                'large_icon': field(large_icon, icon_path, nullable=False),
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
        self.before_compose()
        self.__dearfy_compose__()
        self.__dearfy_init_action_attributes__()
        self._actioner._app = self
        self._nodes.clear()

    @property
    def title(self) -> str:
        return dpg.get_viewport_title()

    @title.setter
    def title(self, value: str) -> None:
        return dpg.set_viewport_title(value)

    @property
    def width(self) -> int:
        return dpg.get_viewport_width()

    @width.setter
    def width(self, value: int) -> None:
        dpg.set_viewport_width(value)

    @property
    def height(self) -> int:
        return dpg.get_viewport_height()

    @height.setter
    def height(self, value: int) -> None:
        dpg.set_viewport_height(value)

    @property
    def max_width(self) -> int:
        return dpg.get_viewport_max_width()

    @max_width.setter
    def max_width(self, value: int) -> None:
        dpg.set_viewport_max_width(value)

    @property
    def max_height(self) -> int:
        return dpg.get_viewport_max_height()

    @max_height.setter
    def max_height(self, value: int) -> None:
        dpg.set_viewport_max_height(value)

    @property
    def clear_color(self) -> Color:
        return dpg.get_viewport_clear_color()

    @clear_color.setter
    def clear_color(self, value: Color) -> None:
        dpg.set_viewport_clear_color(value)

    @property
    def client_width(self) -> int:
        return dpg.get_viewport_client_width()

    @property
    def client_height(self) -> int:
        return dpg.get_viewport_client_height()

    @property
    def pos(self) -> tuple[float, float]:
        return tuple(dpg.get_viewport_pos())

    @pos.setter
    def pos(self, value: tuple[float, float]) -> None:
        return dpg.set_viewport_pos(value)

    @property
    def vsync(self) -> bool:
        return dpg.is_viewport_vsync_on()

    @vsync.setter
    def vsync(self, value: bool) -> None:
        dpg.set_viewport_vsync(value)

    @property
    def resizable(self) -> bool:
        return dpg.is_viewport_resizable()

    @resizable.setter
    def resizable(self, value: bool) -> None:
        dpg.set_viewport_resizable(value)

    @property
    def always_top(self) -> bool:
        return dpg.is_viewport_always_top()

    @always_top.setter
    def always_top(self, value: bool) -> None:
        dpg.set_viewport_always_top(value)

    @property
    def decorated(self) -> bool:
        return dpg.is_viewport_decorated()

    @decorated.setter
    def decorated(self, value: bool) -> None:
        dpg.set_viewport_decorated(value)
    
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
        for child in generator_safe(self.compose):
            if self._current_node:
                self._current_node._add_child(child)
        self._nodes.clear()
        for child in self._node_children:
            child.__dearfy_compose__()
    
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
        for child in self._node_children:
            if hasattr(child, 'tag'):
                try:
                    return child.get_item(tag)
                except ValueError:
                    pass
        raise ValueError('An object with such an attribute does not exist.')

    def get_items(self, tags: Iterable[Tag], /) -> Iterator[Item]:
        if not isinstance(tags, set):
            tags = set(tags)
        yield from ()
        for child in self._node_children:
            if hasattr(child, 'tag'):
                yield from child.get_items(tags)

    def search_item(self, mask_tag: str) -> Item:
        for child in self._node_children:
            if hasattr(child, 'tag'):
                try:
                    return child.search_item(mask_tag)
                except ValueError:
                    pass
        raise ValueError('An object with such an attribute does not exist.')

    def search_items(self, mask_tag: str) -> Iterator[Item]:
        yield from ()
        for child in self._node_children:
            if hasattr(child, 'tag'):
                yield from child.search_items(mask_tag)

    @staticmethod
    def _dearfy_object_init(app: 'App', obj: DearfyObject) -> None:
        if not bool(obj._state & 0b0001):           obj.__dearfy_preparing__(app)
        if not bool((obj._state & 0b0010) >> 1):    obj.__dearfy_preinit__()
        if not bool((obj._state & 0b0100) >> 2):    obj.__dearfy_init__()
        if not bool((obj._state & 0b1000) >> 3):    obj.__dearfy_postinit__()

    def push_item_to(self, obj: Composable, *, parent: Tag | None = None) -> None:
        loguru.logger.trace(f"[red]Call[/red]: {self!r}.push_item_to({obj!r}, parent={parent!r})")
        parent_item: Item | App = self.get_item(parent) if parent is not None else self
        loguru.logger.trace(f"{self!r}.push_item_to(...).{parent_item=!r}")
        if isinstance(obj, Item):
            loguru.logger.trace("{0}.push_item_to(...).obj is [green]Item[/green]", self)
            if parent is not None:
                obj._config['parent'] = parent
            parent_item._add_child(obj)
            self._dearfy_obejct_init(self, obj)
            return
        elif isinstance(obj, (Iterator, Iterable, Generator)):
            loguru.logger.trace("{0}.push_item_to(...).obj is [green]Iterator[/green] | [green]Iterable[/green] | [green]Generator[/green]", self)
            for item in obj:
                if parent is not None:
                    item._config['parent'] = parent
                parent_item._add_child(item)
                self._dearfy_obejct_init(self, item)
            return
        elif inspect.isgeneratorfunction(obj):
            loguru.logger.trace("{0}.push_item_to(...).obj is [green]GeneratorFunction[/green]", self)
            for item in obj():
                if parent is not None:
                    item._config['parent'] = parent
                parent_item._add_child(item)
                self._dearfy_obejct_init(self, item)
            return
        elif inspect.isgenerator(obj):
            loguru.logger.trace("{0}.push_item_to(...).obj is [green]Generator[/green]", self)
            for item in obj:
                if parent is not None:
                    item._config['parent'] = parent
                parent_item._add_child(item)
                self._dearfy_obejct_init(self, item)
            return
        raise RuntimeWarning(f"Couldn't get Item from the object ({obj}).")

    def push_item(self, obj: Composable) -> None:
        self.push_item_to(obj)

    def set_primary_window(self, window: Tag | Window, value: bool) -> None:
        tag = window.tag if isinstance(window, Window) else window
        dpg.set_primary_window(tag, value)

    def bind_font(self, font: Tag | Font) -> None:
        """Global font setting.

        Args:
            font (Tag | Font): A widget object or its tag.
        """
        tag = font.tag if isinstance(font, Font) else font
        dpg.bind_font(tag)

    def bind_item_font(self, item: Tag | Item, font: Tag | Font) -> None:
        item_tag = item.tag if isinstance(item, Item) else item
        font_tag = font.tag if isinstance(font, Font) else font
        dpg.bind_item_font(item_tag, font_tag)

    def get_active_window(self) -> Window:
        return self.get_item(dpg.get_active_window())

    def set_large_icon(self, src: FilePath) -> None:
        src = str(Path(src).resolve())
        dpg.set_viewport_large_icon(src)
        self._config['large_icon'] = src

    def set_small_icon(self, src: FilePath) -> None:
        src = str(Path(src).resolve())
        dpg.set_viewport_small_icon(src)
        self._config['small_icon'] = src

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

    def show_style_editor(self) -> None:
        """Shows the standard style editor window."""
        dpg.show_style_editor()

    def on_ready(self) -> None:
        """Called after full initialization, before the main loop starts."""

    def before_compose(self) -> None:
        """Called before compose."""

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
        loguru.logger.trace("{tree}", tree=self._to_rich_tree())
        dpg.create_context()
        dpg.create_viewport(**(self._gkwagrs['create_viewport']))
        self._state = AppState.PREINIT
        self.__dearfy_preinit__()
        loguru.logger.trace('[green]▬▬▬▬▬[/green] [yellow]AFTER PREINIT[/yellow] [green]▬▬▬▬▬[/green]')
        loguru.logger.trace("{tree}", tree=self._to_rich_tree())
        self._state = AppState.INIT
        self.__dearfy_init__()
        loguru.logger.trace('[green]▬▬▬▬▬[/green] [yellow]AFTER INIT[/yellow] [green]▬▬▬▬▬[/green]')
        loguru.logger.trace("{tree}", tree=self._to_rich_tree())
        dpg.setup_dearpygui()
        self._state = AppState.POSTINIT
        self.__dearfy_postinit__()
        loguru.logger.trace('[green]▬▬▬▬▬[/green] [yellow]AFTER POSTINIT[/yellow] [green]▬▬▬▬▬[/green]')
        loguru.logger.trace("{tree}", tree=self._to_rich_tree())
        self._state = AppState.RUNNING
        dpg.show_viewport(**(self._gkwagrs['show_viewport']))
        self.on_ready()
        dpg.start_dearpygui()
        dpg.destroy_context()
        self._state = AppState.NONE
        self.__dearfy_destroy__()
        loguru.logger.trace("{tree}", tree=self._to_rich_tree())

    def stop(self) -> None:
        dpg.stop_dearpygui()

action = App._actioner.action