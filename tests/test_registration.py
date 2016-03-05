from unittest import TestCase

from pluginmanager2 import PluginManager, RegisterPlugin, PluginException
from pluginmanager2.mock import TestPlugin


class RegistrationTest(TestCase):

    def setUp(self):
        PluginManager.reset_singleton()

    def test_register_with_decorator_call(self):
        pm = PluginManager()

        registered_test_plugin = RegisterPlugin(label="test")(TestPlugin)

        assert registered_test_plugin in pm.plugins
        assert len(pm.plugins) == 1

    def test_register_with_at(self):
        pm = PluginManager()

        @RegisterPlugin()
        class TestPluginWithAtDecorator(TestPlugin):
            pass

        assert TestPluginWithAtDecorator in pm.plugins
        assert len(pm.plugins) == 1

    def test_invalid_decorator(self):
        try:
            @RegisterPlugin
            class TestPlugin:
                pass
        except PluginException:
            return
        else:
            raise Exception("Test failed, decorator was supposed to throw exception")

