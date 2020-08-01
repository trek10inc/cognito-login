"""Pluggy hook specifications"""
import configargparse as argparse

import pluggy

hookspec = pluggy.HookspecMarker('cognito-login')


@hookspec
def pre_add_arguments(): # pylint: disable=unused-argument
    """pre add_arguments hook"""

@hookspec
def add_arguments(parser: argparse.ArgumentParser): # pylint: disable=unused-argument
    """add argparse arguments to the parser, should try/except for conflicting arguments"""

@hookspec
def post_add_arguments(parser: argparse.ArgumentParser, arguments: argparse.Namespace): # pylint: disable=unused-argument
    """post add_arguments hook"""


@hookspec
def pre_get_jwt(arguments: argparse.Namespace): # pylint: disable=unused-argument
    """pre get_jwt hook"""

@hookspec
def get_jwt(arguments: argparse.Namespace): # pylint: disable=unused-argument
    """Get JWT"""

@hookspec
def post_get_jwt(arguments: argparse.Namespace, result: int): # pylint: disable=unused-argument
    """post get_jwt hook"""
