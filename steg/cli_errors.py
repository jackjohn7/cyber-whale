
def usage(file_name: str) -> str:
    return f"""Usage: python {file_name} -(sr) -(bB) [-i<val>] -w<val> [-h<val>]
       -s      store
       -r      retrieve
       -b      bit mode
       -B      byte mode
       -o<val> set offset to <val> (default is 0)
       -i<val> set interval to <val> (default is 1)
       -w<val> set wrapper file to <val>
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
    def __str__(self):
        return "ERR: Too many modes specified, see usage"

