from datetime import datetime
from typing import Any, TypeVar
from typing import List
from typing import Optional, Callable, Union, Set, Mapping

from .utils import Singleton

from .plugin import Plugin

PluginSelector = Union[Plugin, str]

class PluginMetaData:
    def __init__(self, plugin: Plugin, label: str, **kwargs) -> None:
        self.plugin = plugin
        self.label = label
        self.loaded = datetime.now()
        for kwarg in kwargs:
            print("Unknown kwarg: " + str(kwarg))

@Singleton
class PluginManager:

    _plugins = None                     # type: Set[Plugin]
    _plugin_metadata = None             # type: dict

    def __init__(self, metadata_class=PluginMetaData) -> None:
        """
        Initializes the PluginManager

        Takes one argument metadata_class which can be used to extend the metadata format for plugins
        """
        self._metadata_class = metadata_class
        self._plugins = set()
        self._plugin_metadata = dict()

    def register_plugin(self, plugin_class: Plugin, label=None, **kwargs):
        metadata = self._metadata_class(plugin_class) # type: PluginMetaData
        self._plugins.add(plugin_class)
        self._plugin_metadata[plugin_class] = metadata

    @property
    def plugins(self):
        return self._plugins

    def plugin_metadata(self, plugin_selector: PluginSelector):
        """Returns the metadata for a plugin, either by label or plugin reference"""
        for metadata in self._plugin_metadata.values():
            if plugin_selector == metadata.label\
            or plugin_selector == metadata.plugin:
                return metadata
