from typing_extensions import Any  # noqa: UP035

from dearfy.app import App, action
from dearfy.typing import Tag
from dearfy.widgets import *

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