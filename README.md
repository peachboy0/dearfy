# dearfy

## Desription

**Dearfy** is a library built on top of [DearPyGUI](https://github.com/hoffstadt/DearPyGui) (which itself is a wrapper for [Dear ImGui](https://github.com/ocornut/imgui)), designed to simplify the creation of complex, highly-structured user interfaces.

The project is fully open-source (MIT License) and was inspired by the object-oriented interface building approach of [Textual](https://github.com/Textualize/textual) (a popular library for creating Terminal User Interfaces).

## Instatting

Direct installation from [PyPi](https://pypi.org/) via `pip`:
```
pip install dearfy
```

Installation from the GitHub repository:
```
pip install git+https://github.com/peachboy0/dearfy.git
```

## Using

```python
import dearpygui.dearpygui as dpg
from dearfy.app import App, action
from dearfy.widgets import *
from dearfy.typing import Tag

from typing_extensions import Any

# ! Menu

class MyApp(App):
    primary_window_tag: Tag | None = None

    def compose(self):
        with Window(tag="FirstWindow"):
            yield Button(label="[P]", callback='SetPrimaryWindow')
            with Group(horizontal=True):
                yield InputText(width=-100)
                yield Button(label="OK", width=50)
        with Window(tag="SecondWindow"):
            yield Button(label="[P]", callback='SetPrimaryWindow')
            with Group(horizontal=True):
                yield Checkbox()
                yield Text("It's okay?")

    @action('SetPrimaryWindow', callmode='one')
    def action_SetPrimaryWindow(self, sender: Tag, app_data: Tag, user_data: Any) -> None:
        button: Button = self.get_item(sender)
        if self.primary_window_tag is not None:
            if self.primary_window_tag == button._node_parent.tag:
                self.set_primary_window(self.primary_window_tag, False)
                self.primary_window_tag = None
            else:
                self.set_primary_window(self.primary_window_tag, False)
                self.set_primary_window(button._node_parent.tag, True)
                self.primary_window_tag = button._node_parent.tag
        else:
            self.set_primary_window(button._node_parent.tag, True)
            self.primary_window_tag = button._node_parent.tag

# ! Run

if __name__ == "__main__":
    app = MyApp()
    app.run()
```