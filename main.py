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

        # Register plugin
        self.register(
            plugin_name="Template",  # Should be a unique name for your plugin
            # The GitHub repository for your plugin
            github_repo="https://github.com/StreamController/PluginTemplate",
            plugin_version="1.0.0",  # The plugin version, will be used to check updates
            app_version="1.1.1-alpha"  # The support application version
        )
