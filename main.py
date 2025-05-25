# Import StreamController modules
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder
from src.backend.DeckManagement.InputIdentifier import Input
from src.backend.PluginManager.ActionInputSupport import ActionInputSupport

# Import actions
from .actions.SimpleAction import SimpleAction


class PluginTemplate(PluginBase):
    def __init__(self):
        # Plugins should set use_legacy_locale to False
        # for future proofing themselves
        super().__init__(use_legacy_locale=False)

        # Register actions
        self.simple_action_holder = ActionHolder(
            plugin_base=self,  # Should always be set to self
            action_base=SimpleAction,  # References the actual created action
            action_id_suffix="SimpleAction",  # A unique name for the action in your plugin
            action_name="Simple Action",  # The display name for the action
            action_support={
                # These should be set based on what inputs have been tested
                Input.Key: ActionInputSupport.SUPPORTED,
                Input.Dial: ActionInputSupport.UNTESTED,
                Input.Touchscreen: ActionInputSupport.UNTESTED,
            }
        )
        # Adds the action to the plugin
        self.add_action_holder(self.simple_action_holder)

        # Register plugin using details from manifest.json
        self.register()
