# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.DeckManagement.DeckController import DeckController
from src.backend.PageManagement.Page import Page
from src.backend.PluginManager.PluginBase import PluginBase

# Import python modules
import os

# Import gtk modules - used for the config rows
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

class SimpleAction(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.use_state_one: bool = True
        
    def on_ready(self) -> None:
        _, render = self.plugin_base.asset_manager.icons.get_asset_values("info")

        if render:
            self.set_media(render)

        self.set_color()
        
    def on_key_down(self) -> None:
        self.set_color()
    
    def on_key_up(self) -> None:
        print("KEY UP")

    def set_color(self):
        if self.use_state_one:
            color = self.plugin_base.asset_manager.colors.get_asset_values("state1")
        else:
            color = self.plugin_base.asset_manager.colors.get_asset_values("state2")
        self.use_state_one = not self.use_state_one

        if color:
            self.set_background_color(color=list(color))