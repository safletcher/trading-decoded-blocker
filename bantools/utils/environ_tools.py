import os
import typing
from bantools.utils.exceptions import EnvironmentVariableUnavaiable
from bantools.exceptions import NullArgumentsNotAllowed


def getenv_var(variable_name: str, case_insensitive: bool = True) -> str:

    if variable_name is None:
        raise NullArgumentsNotAllowed("A None arguement was passed to variable_name")

    environ_var = os.environ.get(variable_name.lower())

    if environ_var is None:
        environ_var = os.environ.get(variable_name.upper())

    if environ_var is None:
        raise EnvironmentVariableUnavaiable(
            "Environment variable defined on system must be all uppercase or all lowercase"
        )

    return environ_var
