# Base project class exception
class BlockerToolsExceptions(Exception):
    pass


class UtilException(BlockerToolsExceptions):
    pass


class EnvironmentVariableException(UtilException):
    pass


class NullArgumentsNotAllowed(BlockerToolsExceptions):
    pass


class NullArgumentsNotAllowed(BlockerToolsExceptions):
    pass


class EnvironmentVariableUnavaiable(EnvironmentVariableException):
    pass
