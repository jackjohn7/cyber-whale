from typing import Literal


def usage(file_name: str) -> str:
    return f"""Usage: python {file_name} -(sr) -(bB) [-i<val>] -w<val> [-h<val>]
       -s      store
       -r      retrieve
       -b      bit mode
       -B      byte mode
       -o<val> set offset to <val> (default is 0)
       -i<val> set interval to <val> (default is 1) -w<val> set wrapper file to <val>
       -h<val> set hidden file to <val>"""

class CliError(Exception):
    def __str__(self) -> str:
        return "ERR: Cli exception occurred"

class InvalidConfiguration(CliError):

    config_str: str

    def __init__(self, config_str: str):
        self.config_str = config_str
    
    def __str__(self) -> str:
        return f"ERR: Invalid configuration given!\n{self.config_str}"

class TooManyModesSpecified(CliError):
    at: Literal["data", "action"]
    def __init__(self, mode):
        self.at = mode

    def __str__(self):
        return f"ERR: Too many modes specified for {self.at}, see usage"

class InvalidParam(CliError):
    given: str
    param_name: Literal["offset", "interval"]
    def __init__(self, given, param_name):
        self.given = given
        self.param_name = param_name
    def __str__(self):
        return f"ERR: Invalid {self.param_name} \"{self.given}\" was given"

class FileNotFound(CliError):
    filename: str
    provided_for: Literal["wrapper", "hidden"]
    def __init__(self, filename, provided_for):
        self.filename = filename
        self.provided_for = provided_for

    def __str__(self):
        return f"ERR: File {self.filename} provided for {self.provided_for} was not found"

class UnrecognizedArgument(CliError):
    argument: str
    def __init__(self, argument: str):
        self.argument = argument

    def __str__(self):
        return f"ERR: Unrecognized argument \"{self.argument}\" provided"
