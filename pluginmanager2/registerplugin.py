from .pluginmanager import PluginManager
from .plugin import Plugin
from .exceptions import PluginException

_FORGOT_PARENS="""RegisterPlugin decorator called incorrectly.
Looks like you forgot to put parens after the decorator, make sure the line looks like this: @RegisterPlugin()"""

_POS_ARGS="""RegisterPlugin decorator called incorrectly.
Perhaps you gave it positional arguments which is illegal?"""

class RegisterPlugin:
    """Class that acts as a decorator which registers plugins"""

    def __init__(self, *args, label: str = None, **kwargs) -> None:
        if len(args) > 0:
            if type(args[0]) == type:
                raise PluginException(_FORGOT_PARENS)
            else:
                raise PluginException(_POS_ARGS)
        self.label = label
        self.kwargs = kwargs

    def __call__(self, plugin_class: Plugin):
        pm = PluginManager()
        pm.register_plugin(plugin_class, label=self.label, **self.kwargs)
        return plugin_class
