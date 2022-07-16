from bantools.exceptions import BlockerToolsExceptions


"""

Base Exception

"""


class UtilException(BlockerToolsExceptions):
    pass


class EnvironmentVariableException(UtilException):
    pass


"""

Custom exceptions

"""


class NullArgumentsNotAllowed(BlockerToolsExceptions):
    pass


class EnvironmentVariableUnavaiable(EnvironmentVariableException):
    pass
