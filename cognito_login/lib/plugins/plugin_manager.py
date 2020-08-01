"""cognito-login plugin manager"""
import pluggy

from cognito_login import default_plugins
from . import hookspec


plugin_manager = pluggy.PluginManager('cognito-login')
plugin_manager.add_hookspecs(hookspec)
plugin_manager.register(default_plugins)
plugin_manager.load_setuptools_entrypoints('cognito-login')
