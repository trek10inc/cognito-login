"""Plugin hook driver for getting the jwt"""
from cognito_login.lib.plugins import plugin_manager


def get_jwt(arguments: list) -> int:
    """Do the work"""
    plugin_manager.hook.pre_get_jwt( # pylint: disable=no-member
        arguments=arguments,
    )
    result = plugin_manager.hook.get_jwt( # pylint: disable=no-member
        arguments=arguments,
    )
    plugin_manager.hook.post_get_jwt( # pylint: disable=no-member
        arguments=arguments,
        result=result,
    )
    return result
