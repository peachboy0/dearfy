import dearpygui.dearpygui as dpg
from typing_extensions import Unpack

from dearfy.base import Enableable, Item, ItemKwargs, Showable
from dearfy.field import field
from dearfy.functions import get_method_needed
from dearfy.typing import Callback, Position, Tag
from dearfy.validator import ValidateKwargsAction

# ! Table Item Class

class Table(Item, Showable):
    REFERENCE_METHOD = dpg.add_table
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        width: int = 0,
        height: int = 0,
        indent: int = -1,
        parent: Tag | None = None,
        before: Tag | None = None,
        source: Tag | None = None,
        callback: Callback | None = None,
        show: bool = True,
        pos: Position | None = None,
        filter_key: str = '',
        header_row: bool = True,
        clipper: bool = False,
        inner_width: int = 0,
        policy: int = 0,
        freeze_rows: int = 0,
        freeze_columns: int = 0,
        sort_multi: bool = False,
        sort_tristate: bool = False,
        resizable: bool = False,
        reorderable: bool = False,
        hideable: bool = False,
        sortable: bool = False,
        context_menu_in_body: bool = False,
        row_background: bool = False,
        borders_innerH: bool = False,
        borders_outerH: bool = False,
        borders_innerV: bool = False,
        borders_outerV: bool = False,
        no_host_extendX: bool = False,
        no_host_extendY: bool = False,
        no_keep_columns_visible: bool = False,
        precise_widths: bool = False,
        no_clip: bool = False,
        pad_outerX: bool = False,
        no_pad_outerX: bool = False,
        no_pad_innerX: bool = False,
        scrollX: bool = False,
        scrollY: bool = False,
        no_saved_settings: bool = False,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            indent=indent,
            parent=field(parent, 0),
            before=field(before, 0),
            source=field(source, 0),
            callback=callback,
            show=show,
            pos=field(pos, default_factory=list),
            filter_key=filter_key,
            header_row=header_row,
            clipper=clipper,
            inner_width=inner_width,
            policy=policy,
            freeze_rows=freeze_rows,
            freeze_columns=freeze_columns,
            sort_multi=sort_multi,
            sort_tristate=sort_tristate,
            resizable=resizable,
            reorderable=reorderable,
            hideable=hideable,
            sortable=sortable,
            context_menu_in_body=context_menu_in_body,
            row_background=row_background,
            borders_innerH=borders_innerH,
            borders_outerH=borders_outerH,
            borders_innerV=borders_innerV,
            borders_outerV=borders_outerV,
            no_host_extendX=no_host_extendX,
            no_host_extendY=no_host_extendY,
            no_keep_columns_visible=no_keep_columns_visible,
            precise_widths=precise_widths,
            no_clip=no_clip,
            pad_outerX=pad_outerX,
            no_pad_outerX=no_pad_outerX,
            no_pad_innerX=no_pad_innerX,
            scrollX=scrollX,
            scrollY=scrollY,
            no_saved_settings=no_saved_settings,
            **kwargs
        )

    def __dearfy_init__(self) -> None:
        kwargs = get_method_needed(dpg.add_table, **self._config)
        if self.containered:
            with dpg.table(**kwargs) as tag:
                super().__dearfy_init__()
        else:
            tag = dpg.add_table(**kwargs)
            super().__dearfy_init__()
        self._config['tag'] = tag

# ! Table Column Item Class

class TableColumn(Item, Showable, Enableable):
    REFERENCE_METHOD = dpg.add_table_column
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        width: int = 0,
        parent: Tag | None = None,
        before: Tag | None = None,
        show: bool = True,
        enabled: bool = True,
        init_width_or_weight: float = 0,
        default_hide: bool = False,
        default_sort: bool = False,
        width_stretch: bool = False,
        width_fixed: bool = False,
        no_resize: bool = False,
        no_reorder: bool = False,
        no_hide: bool = False,
        no_clip: bool = False,
        no_sort: bool = False,
        no_sort_ascending: bool = False,
        no_sort_descending: bool = False,
        no_header_width: bool = False,
        prefer_sort_ascending: bool = True,
        prefer_sort_descending: bool = False,
        indent_enable: bool = False,
        indent_disable: bool = False,
        angled_header: bool = False,
        no_header_label: bool = False,
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            width=width,
            parent=field(parent, 0),
            before=field(before, 0),
            show=show,
            enabled=enabled,
            init_width_or_weight=init_width_or_weight,
            default_hide=default_hide,
            default_sort=default_sort,
            width_stretch=width_stretch,
            width_fixed=width_fixed,
            no_resize=no_resize,
            no_reorder=no_reorder,
            no_hide=no_hide,
            no_clip=no_clip,
            no_sort=no_sort,
            no_sort_ascending=no_sort_ascending,
            no_sort_descending=no_sort_descending,
            no_header_width=no_header_width,
            prefer_sort_ascending=prefer_sort_ascending,
            prefer_sort_descending=prefer_sort_descending,
            indent_enable=indent_enable,
            indent_disable=indent_disable,
            angled_header=angled_header,
            no_header_label=no_header_label
            **kwargs
        )

    def __dearfy_init__(self):
        kwargs = get_method_needed(dpg.add_table_column, **self._config)
        tag = dpg.add_table_column(**kwargs)
        super().__dearfy_init__()
        self._config['tag'] = tag

# ! Table Row Item Class

class TableRow(Item, Showable):
    REFERENCE_METHOD = dpg.add_table_row
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        height: int = 0,
        parent: Tag | None = None,
        before: Tag | None = None,
        show: bool = True,
        filter_key: str = '',
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            height=height,
            parent=field(parent, 0),
            before=field(before, 0),
            show=show,
            filter_key=filter_key,
            **kwargs
        )

    def __dearfy_init__(self):
        kwargs = get_method_needed(dpg.add_table_column, **self._config)
        if self.containered:
            with dpg.table_row(**kwargs) as tag:
                super().__dearfy_init__()
        else:
            tag = dpg.add_table_row(**kwargs)
            super().__dearfy_init__()
        self._config['tag'] = tag

# ! Table Cell

class TableCell(Item, Showable):
    REFERENCE_METHOD = dpg.add_table_cell
    VALIDATORS_KWARGS = (ValidateKwargsAction, )

    def __init__(self,
        height: int = 0,
        parent: Tag | None = None,
        before: Tag | None = None,
        show: bool = True,
        filter_key: str = '',
        **kwargs: Unpack[ItemKwargs]
    ) -> None:
        super().__init__(
            height=height,
            parent=field(parent, 0),
            before=field(before, 0),
            show=show,
            filter_key=filter_key,
            **kwargs
        )

    def __dearfy_init__(self):
        kwargs = get_method_needed(dpg.add_table_column, **self._config)
        if self.containered:
            with dpg.table_cell(**kwargs) as tag:
                super().__dearfy_init__()
        else:
            tag = dpg.add_table_column(**kwargs)
            super().__dearfy_init__()
        self._config['tag'] = tag
