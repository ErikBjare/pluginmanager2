from unittest import TestCase

from pluginmanager2 import PluginManager, RegisterPlugin
from pluginmanager2.mock import TestPlugin


class LookupPluginTest(TestCase):
    def setUp(self):
        PluginManager.reset_singleton()
        self.plugin = RegisterPlugin(label="test_plugin")(TestPlugin)

    def test_find_by_label(self):
        assert PluginManager().plugin_metadata("test_plugin")

    def test_find_by_instance(self):
        assert PluginManager().plugin_metadata(self.plugin)
