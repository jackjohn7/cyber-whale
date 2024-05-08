from sys import argv
from typing import Optional, Literal
import cli_errors

class Args:
    action: Optional[Literal["retrieve", "store"]] = None
    data_mode: Optional[Literal["bit", "byte"]] = None
    offset = 0
    interval = 1

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
                    raise cli_errors.TooManyModesSpecified()
                case ['-', 's'] if self.action is None:
                    self.action = "store"

        self.validate()

