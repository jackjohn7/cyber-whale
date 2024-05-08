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
    data_mode: Optional[Literal["bit", "byte"]]
    offset = 0
    interval = 1
    wrapper: Optional[str]
    hidden: Optional[str]

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
        if self.action is None or self.data_mode is None:
            raise cli_errors.InvalidConfiguration(str(self))

    def parse(self):
        for arg in argv[1:]:
            match [*arg]:
                case ['-', 's'] | ['-', 'r'] if self.action is not None:
                    raise cli_errors.TooManyModesSpecified("action")
                case ['-', 's'] if self.action is None:
                    self.action = "store"
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


        self.validate()

