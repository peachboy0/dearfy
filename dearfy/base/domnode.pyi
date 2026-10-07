from collections import deque
from types import TracebackType

from rich.tree import Tree
from typing_extensions import Any, ClassVar, Iterator, Self, TypeVar  # noqa: UP035

# ! Type Vars

T = TypeVar('T')  # noqa: PYI001

# ! DOM Node Class

class DOMNode:
    NODE_CONTAINERABLE: ClassVar[bool]
    """Is the node a container."""
    
    _nodes: ClassVar[deque[DOMNode]]
    _node_parent: DOMNode | None
    _node_children: list[DOMNode]

    def __init__(self) -> None: ...
    
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    
    @property
    def _current_node(self) -> DOMNode | None: ...
    @property
    def _node_main_parent(self) -> DOMNode: ...
    
    def _add_child(self, __child: DOMNode, /) -> None: ...
    def _remove_child(self, __child: DOMNode, /) -> None: ...
    def _pop_child(self, __index: int=-1, /) -> DOMNode: ...
    def _get_node_by_attr(self, __attr_name: str, __attr_value: Any, /) -> DOMNode: ...
    
    def _to_rich_tree(self) -> Tree: ...
    
    def compose(self) -> Iterator[DOMNode]: ...