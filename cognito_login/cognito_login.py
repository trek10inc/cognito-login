"""cognito-login"""
from cognito_login.lib.parse_args import parse_args
from cognito_login.lib.get_jwt import get_jwt


def cognito_login(*args, **kwargs):
    """Main application logic"""
    args = parse_args(*args, **kwargs)
    result = get_jwt(args)
    return result
