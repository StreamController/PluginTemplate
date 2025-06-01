# Import StreamController modules
from gi.repository import Gtk, Adw
from src.backend.PluginManager.ActionCore import ActionCore
from src.backend.DeckManagement.InputIdentifier import InputEvent, Input
from src.backend.PluginManager.EventAssigner import EventAssigner
from src.backend.PluginManager.PluginSettings.Asset import Color, Icon
from GtkHelper.GenerativeUI.EntryRow import EntryRow
from loguru import logger as log

# Import python modules
import os

# Import gtk modules - used for the config rows
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")


class SimpleAction(ActionCore):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_generative_ui()
        self.create_event_assigner()

    # Create events for the different supported functions. This allows users
    # to easily bind different key actions (like long-press) to your action
    def create_event_assigner(self):
        self.event_manager.add_event_assigner(
            EventAssigner(
                id="pressed",  # A unique ID for the event
                ui_label="pressed",  # The locales.csv key for the event name
                default_event=Input.Key.Events.DOWN,  # The default action to trigger this event
                # The function that should get called when this event triggers
                callback=self._on_pressed
            )
        )
        self.event_manager.add_event_assigner(
            EventAssigner(
                id="released",  # A unique ID for the event
                ui_label="released",  # The locales.csv key for the event name
                default_event=Input.Key.Events.UP,  # The default action to trigger this event
                # The function that should get called when this event triggers
                callback=self._on_released
            )
        )

    # This creates the UI. It doesn't have to be done in it's own function,
    # but should be done during __init__ of the plugin
    def create_generative_ui(self):
        self.text_row = EntryRow(
            action_core=self,  # Should reference this action
            var_name="message_text",  # The variable to store the value in
            default_value="Button Pressed",  # Default text
            title="message-text",  # The locales.csv key for the title
            auto_add=True,  # If the UI field should be auto added without needing to manually implement
            # If set to true, will store the variable in a json dict. IE: "key.test = value"
            complex_var_name=False
        )

    # on_ready gets called when the plugin is done initializing and is ready to
    # be interacted with on the deck
    def on_ready(self) -> None:
        icon_path = os.path.join(self.plugin_base.PATH, "assets", "info.png")
        # Sets the icon for the plugin
        self.set_media(media_path=icon_path, size=0.75)

    def _on_pressed(self, _) -> None:
        value = self.text_row.get_value()  # Get the input value from the user
        # Use loguru instead of print() to help with debugging
        log.debug(value)

    def _on_released(self, _) -> None:
        # Use loguru instead of print() to help with debugging
        log.debug("Released")
