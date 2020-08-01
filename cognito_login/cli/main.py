"""Main entrypoint for the CLI"""
import sys

from cognito_login.cognito_login import cognito_login
from cognito_login.lib import exceptions
from cognito_login.lib.logger import logger


def main():
    """Main entrypoint for cli application"""
    try:
        result = cognito_login(*sys.argv[1:])
        if result:
            print(result)
    except exceptions.EarlyExit as early_exit:
        logger.debug('', exc_info=True)
        logger.debug(early_exit)
    except exceptions.CognitoLoginException as err:
        logger.debug('', exc_info=True)
        print('Error: {}'.format(err))
