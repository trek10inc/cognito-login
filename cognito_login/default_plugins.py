"""Default cognito-login plugins"""
import botocore
import configargparse as argparse
import warrant

from cognito_login.lib.plugins.hookimpl import hookimpl
from cognito_login.lib import exceptions
from cognito_login.__data__ import VERSION


@hookimpl(tryfirst=True)
def add_arguments(parser: argparse.ArgumentParser):
    """Add default arguments"""
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=VERSION,
        help='Display the current version of cognito-login',
    )
    parser.add_argument(
        '--user-pool-id',
        dest='user_pool_id',
        env_var='USER_POOL_ID',
        action='store',
        help='UserPool ID',
        type=str,
        required=True,
    )
    parser.add_argument(
        '--app-client-id',
        dest='app_client_id',
        env_var='APP_CLIENT_ID',
        action='store',
        help='App Client ID',
        type=str,
        required=True,
    )
    parser.add_argument(
        '-u', '--username',
        dest='username',
        env_var='COGNITO_USERNAME',
        action='store',
        help='Username',
        type=str,
        required=True,
    )
    parser.add_argument(
        '-p', '--password',
        dest='password',
        env_var='COGNITO_PASSWORD',
        action='store',
        help='Password',
        type=str,
        required=True,
    )


@hookimpl(tryfirst=True)
def get_jwt(arguments: dict) -> dict:
    """Do the work"""
    region = arguments.user_pool_id.split('_')[0]
    user = warrant.Cognito(
        user_pool_id=arguments.user_pool_id,
        client_id=arguments.app_client_id,
        username=arguments.username,
        user_pool_region=region,
    )
    try:
        user.authenticate(password=arguments.password)
    except warrant.exceptions.ForceChangePasswordException as err:
        new_password = input('ForceChangePasswordException raised, please enter a new password\n>')
        user.new_password_challenge(arguments.password, new_password)
    except botocore.exceptions.ClientError as err:
        if err.response.get('Error', {}).get('Code') == 'PasswordResetRequiredException':
            reset_code = input('PasswordResetRequiredException raised, please enter your password reset code\n>')
            new_password = input('Please enter a new password\n>')
            user.confirm_forgot_password(reset_code, new_password)
            user.authenticate(password=new_password)
        if err.response.get('Error', {}).get('Code') == 'UserNotFoundException':
            raise exceptions.UserNotFoundException(arguments.username)
        if err.response.get('Error', {}).get('Code') == 'NotAuthorizedException':
            raise exceptions.NotAuthorizedException(err.response.get('message'))
        raise
    return {
        'id_token': user.id_token,
        'refresh_token': user.refresh_token,
        'access_token': user.access_token,
        'token_type': user.token_type,
    }
