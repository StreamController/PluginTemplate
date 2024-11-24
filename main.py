# Import StreamController modules
import os.path

from src.backend.PluginManager.ActionHolder import ActionHolder
from src.backend.PluginManager.ActionInputSupport import ActionInputSupport
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.DeckManagement.InputIdentifier import Input
from src.backend.PluginManager.PluginSettings.Asset import Color, Icon

# Import actions
from .actions.SimpleAction.SimpleAction import SimpleAction

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        ## Register actions
        self.simple_action_holder = ActionHolder(
            plugin_base=self,
            action_base=SimpleAction,
            action_id_suffix="SimpleAction",
            action_name="Simple Action",
            action_support= {
                Input.Key: ActionInputSupport.SUPPORTED,
                Input.Dial: ActionInputSupport.SUPPORTED,
                Input.Touchscreen: ActionInputSupport.SUPPORTED
            }
        )
        self.add_action_holder(self.simple_action_holder)

        self.asset_manager.icons.add_asset("info", Icon(path=os.path.join(self.PATH, "assets", "info.png")))
        self.asset_manager.colors.add_asset("state1", Color(color=(255,0,0,255)))
        self.asset_manager.colors.add_asset("state2", Color(color=(0,255,0,255)))

        # Register plugin
        self.register()