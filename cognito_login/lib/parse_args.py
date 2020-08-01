"""Argument parsing utilities"""
import json
import configargparse as argparse

from cognito_login import __data__
from cognito_login.lib.plugins import plugin_manager
from cognito_login.lib import exceptions


class ArgumentParser(argparse.ArgumentParser):
    """Custom argument parser to raise custom argument exceptions on error"""
    def error(self, message):
        raise exceptions.ArgumentException(message)


def get_cli_argv(*args, **kwargs):
    """Parse python function call into command-line arguments"""
    cli_arguments = [str(arg) for arg in args if arg is not None]

    for key, value in kwargs.items():
        newkey = '--' + key.replace('_', '-')
        cli_arguments.append(str(newkey))

        if isinstance(value, (list, tuple)):
            for element in value:
                cli_arguments.append(str(element))
        elif isinstance(value, bool):
            pass
        elif isinstance(value, dict):
            cli_arguments.append(json.dumps(value, default=str))
        else:
            cli_arguments.append(str(value))

    return cli_arguments


def parse_args(*args: list, **kwargs: dict) -> argparse.Namespace:
    """Parse the incoming python function arguments into parsed argparse arguments"""
    parser = ArgumentParser(
        prog='cognito-login',
        description=__data__.DESCRIPTION + '\n',
        epilog=__data__.MESSAGE,
        formatter_class=lambda prog: (argparse.RawDescriptionHelpFormatter(prog, max_help_position=80, width=80)), # pragma: no cover
        allow_abbrev=False,
        default_config_files=['./.cognito-login.yaml', '~/.cognito-login.yaml'],
    )
    plugin_manager.hook.pre_add_arguments() # pylint: disable=no-member
    plugin_manager.hook.add_arguments( # pylint: disable=no-member
        parser=parser,
    )
    argv = get_cli_argv(*args, **kwargs)

    arguments = parser.parse_args(argv)

    plugin_manager.hook.post_add_arguments( # pylint: disable=no-member
        parser=parser,
        arguments=arguments,
    )
    return arguments
