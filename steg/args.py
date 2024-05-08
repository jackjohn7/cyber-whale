from sys import argv
from typing import Optional, Literal
import cli_errors
import os

class Args:
    """
    Used to parse the arguments in the format that in which
    they are showed in the assignment description document.
    """
    action: Optional[Literal["retrieve", "store"]]
    """Specifies which action the user wants to perform"""
    data_mode: Optional[Literal["bit", "byte"]]
    """Specifies whether the user wants to work with bits or bytes"""
    offset = 0
    """Specifies the offset the user wants to begin writing/retrieving from (distance from beginning)"""
    interval = 1
    """Specifies the distance between each bit/byte"""
    wrapper: Optional[str]
    """Specifies the file that the message will be hidden inside"""
    hidden: Optional[str]
    """Specifies what message will be hidden"""

    def __init__(self):
        self.action = None
        self.data_mode = None
        self.wrapper = None
        self.hidden = None

    def __str__(self) -> str:
        return f"""Config: action    = {self.action}
        data_mode = {self.data_mode}
        offset    = {self.offset}
        interval  = {self.interval}"""

    def validate(self):
        if self.action is None or self.data_mode is None or self.wrapper is None:
            raise cli_errors.InvalidConfiguration(str(self))

    def parse(self, args: list[str]):
        for arg in args:
            match [*arg]:
                case ['-', 's'] | ['-', 'r'] if self.action is not None:
                    raise cli_errors.TooManyModesSpecified("action")
                case ['-', 's'] if self.action is None:
                    self.action = "store"
                case ['-', 'r'] if self.action is None:
                    self.action = "retrieve"
                case ['-', 'b'] | ['-', 'B'] if self.data_mode is not None:
                    raise cli_errors.TooManyModesSpecified("data")
                case ['-', 'b'] if self.data_mode is None:
                    self.data_mode = "bit"
                case ['-', 'B'] if self.data_mode is None:
                    self.data_mode = "byte"
                case ['-', 'o', *rest]:
                    val = "".join(rest)
                    try:
                        offset = int(val)
                        self.offset = offset
                    except:
                        raise cli_errors.InvalidParam(val, "offset")
                case ['-', 'i', *rest]:
                    val = "".join(rest)
                    try:
                        interval = int(val)
                        self.interval = interval
                    except:
                        raise cli_errors.InvalidParam(val, "interval")
                case ['-', 'w', *wrapper]:
                    # validate that file exists
                    self.wrapper = "".join(wrapper)
                    if not os.path.isfile(self.wrapper):
                        raise cli_errors.FileNotFound(self.wrapper, "wrapper")
                case ['-', 'h', *hidden]:
                    # validate that file exists
                    self.hidden = "".join(hidden)
                    if not os.path.isfile(self.hidden):
                        raise cli_errors.FileNotFound(self.wrapper, "hidden")
                case e:
                    arg = "".join(e)
                    raise cli_errors.UnrecognizedArgument(arg)


        self.validate()

