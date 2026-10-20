from __future__ import annotations

import fnmatch

import dearpygui.dearpygui as dpg
import loguru
from typing_extensions import Any, Callable, Iterable, Iterator, NotRequired, ParamSpecKwargs, TypeAlias, TypedDict  # noqa: UP035

from dearfy.base.domnode import DOMNode
from dearfy.exceptions import DearfyAppNoInitedError
from dearfy.field import field
from dearfy.functions import formatting_kwargs, generator_safe, get_method_needed
from dearfy.typing import Tag
from dearfy.validator import ValidatorKwargsBase

# ! Typing

ValidatorKwargsType: TypeAlias = type[ValidatorKwargsBase] | Callable[['Item', ParamSpecKwargs], dict[str, Any]]

class ItemKwargs(TypedDict):
    label: NotRequired[str]
    user_data: NotRequired[Any | None]
    use_internal_label: NotRequired[bool]
    tag: NotRequired[Tag | None]

# ! Base Widget Class

class Item(DOMNode):
    REPR_HIDDEN_KWARGS: tuple[str, ...] = ()
    VALIDATORS_KWARGS: tuple[ValidatorKwargsType, ...] = ()
    REFERENCE_METHOD: Callable[..., Any] | None = None
    
    _node_children: list[Item]

    def __init__(
        self,
        *,
        label: str | None = None,
        user_data: Any | None = None,
        use_internal_label: bool = True,
        tag: Tag | None = None,
        **kwargs: object
    ) -> None:
        """Base class for interface objects.

        Args:
            label (str | None, optional): Used as a name for interface objects. Defaults to None.
            user_data (Any | None, optional): _description_. Defaults to None.
            use_internal_label (bool, optional): _description_. Defaults to True.
            tag (Tag | None, optional): _description_. Defaults to None.
        """
        super().__init__()
        self._app = None
        self._config = {
            'tag': field(tag, 0, nullable=False),
            'label': label,
            'user_data': user_data,
            'use_internal_label': use_internal_label,
            **kwargs
        }
        self._state = 0
    
    def __str__(self) -> str:
        if self.REFERENCE_METHOD is not None:
            kwargs = get_method_needed(self.REFERENCE_METHOD, **self._config)
        else:
            kwargs = self._config
        return f'{self.__class__.__name__}({formatting_kwargs(*self.REPR_HIDDEN_KWARGS, **kwargs)})'
    
    @property
    def tag(self) -> Tag:
        return self._config['tag']
    
    @property
    def app(self) -> object | None:
        return self._app
    
    @property
    def inited(self) -> bool:
        return bool((self._state & 0b0100) >> 2)

    @property
    def label(self) -> str | None:
        if self.tag != 0:
            value = dpg.get_item_label(self.tag)
            self._config['label'] = value
            return value
        return self._config['label']

    @label.setter
    def label(self, v: str) -> None:
        if self.tag != 0:
            dpg.set_item_label(self.tag, v)
        self._config['label'] = v

    @property
    def user_data(self) -> Any:
        if self.tag != 0:
            value = dpg.get_item_user_data(self.tag)
            self._config['user_data'] = value
            return value
        return self._config['user_data']

    @user_data.setter
    def user_data(self, v: Any) -> None:
        if self.tag != 0:
            dpg.set_item_user_data(self.tag, v)
        self._config['user_data'] = v

    def __dearfy_compose__(self) -> None:
        self._nodes.append(self)
        for child in generator_safe(self.compose):
            if self._current_node:
                self._current_node._add_child(child)
        self._nodes.clear()
        for child in self._node_children:
            child.__dearfy_compose__()
    
    def __dearfy_preparing__(self, app: object) -> None:
        loguru.logger.trace(f'[red]Call[/red]: {self!r}.__dearfy_preparing__({app!r})')
        if bool(self._state & 0b0001):
            return
        self._app = app
        for child in self._node_children:
            child.__dearfy_preparing__(app)
        self._state |= 1
    
    def __dearfy_preinit__(self) -> None:
        loguru.logger.trace(f'[red]Call[/red]: {self!r}.__dearfy_preinit__()')
        if bool((self._state & 0b0010) >> 1):
            return
        for vkt in self.VALIDATORS_KWARGS:
            if issubclass(vkt, ValidatorKwargsBase):
                self._config = vkt(item=self, app=self._app).validate(**self._config)
            elif callable(vkt):
                self._config = vkt(self, **self._config)
        for child in self._node_children:
            child.__dearfy_preinit__()
        self._state |= (1 << 1)
    
    def __dearfy_init__(self) -> None:
        loguru.logger.trace(f'[red]Call[/red]: {self!r}.__dearfy_init__()')
        if bool((self._state & 0b0100) >> 2):
            return
        for child in self._node_children:
            child.__dearfy_init__()
        self._state |= (1 << 2)
    
    def __dearfy_postinit__(self) -> None:
        loguru.logger.trace(f'[red]Call[/red]: {self!r}.__dearfy_postinit__()')
        if bool((self._state & 0b1000) >> 3):
            return
        for child in self._node_children:
            child.__dearfy_postinit__()
        self._state |= (1 << 3)
    
    def __dearfy_destroy__(self) -> None:
        self._config['tag'] = 0
        self._state = 0
        for child in self._node_children:
            child.__dearfy_destroy__()

    def get_item(self, tag: Tag) -> Item:
        if self.tag == tag:
            return self
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
        if self.tag in tags:
            tags.remove(self.tag)
            yield self
        for child in self._node_children:
            if hasattr(child, 'tag'):
                yield from child.get_items(tags)

    def search_item(self, mask_tag: str) -> Item:
        if fnmatch.fnmatch(str(self.tag), mask_tag):
            return self
        for child in self._node_children:
            if hasattr(child, 'tag'):
                try:
                    return child.search_item(mask_tag)
                except ValueError:
                    pass
        raise ValueError('An object with such an attribute does not exist.')

    def search_items(self, mask_tag: str) -> Iterator[Item]:
        yield from ()
        if fnmatch.fnmatch(str(self.tag), mask_tag):
            yield self
        for child in self._node_children:
            if hasattr(child, 'tag'):
                yield from child.search_items(mask_tag)

    # NEEDED: Refactoring...
    def push_item(self, item: Item) -> None:
        if self._app is None:
            raise DearfyAppNoInitedError('The application is not initialized.')
        self.app.push_item_to(item, self.tag)

    # NEEDED: Refactoring...
    def push_item_to(self, item: Item, *, parent: Tag | None = None) -> Tag:
        if self._app is None:
            raise DearfyAppNoInitedError('The application is not initialized.')
        self._app.push_item_to(item, parent)

    def _move_item_to(self, parent: Tag) -> None:
        loguru.logger.trace(f'Move {self} to {parent!r}')
        old_parent, new_parent = self._node_parent, self.get_item(parent)
        old_parent._remove_child(self)
        new_parent._add_child(self)
    
    def get_configuration(self) -> dict[str, Any]:
        return dpg.get_item_configuration(self.tag)
    
    def configurate(self, **kwargs: object) -> None:
        if self.inited:
            dpg.configure_item(self.tag, **kwargs)
            self._config.update(**kwargs)
    
    def destroy(self) -> None:
        if self.inited:
            dpg.delete_item(self.tag)
            self._config['tag'] = 0
            self._state = 0
            if self._node_parent is not None:
                self._node_parent._remove_child(self)