"""Custom exception classes"""

class CognitoLoginException(Exception):
    """Base exception for this project"""


class ArgumentException(CognitoLoginException):
    """An issue occured during argument handling or parsing"""
    def __init__(self, message):
        super().__init__()
        self.message = message
    def __str__(self):
        return self.message


class EarlyExit(CognitoLoginException):
    """Raise this exception when there is no more work to be done"""
    def __str__(self):
        return 'Early exit exception, nothing left to do'


class ValidationException(CognitoLoginException):
    """A validation exception has occured"""
    def __init__(self, message='no message'):
        super().__init__()
        self.message = message
    def __str__(self):
        return 'Validation Exception - {}'.format(self.message)
