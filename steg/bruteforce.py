from sys import stderr, stdin, exit
from threading import Thread
from string import printable
from os import mkdir
from types import SimpleNamespace
from steg import Steg, StegBit, StegByte
from argparse import ArgumentParser, Action
from typing import Literal, Optional
from dataclasses import dataclass, field
import filetype

# DATA
@dataclass
class Matcher:
    header: Optional[bytearray] = None
    middle_bits: list[bytearray] = field(default_factory=list)
    tail: Optional[bytearray] = None
    
    def match_data(self, data: bytearray) -> bool:
        """
        Gives a boolean stating whether or not there is a potential match based on
        certain predefined markers
        """
        potential = False
        if self.header is not None:
            # check for occurrence of header
            potential = self.header == data[0:len(self.header)]

        if self.tail is not None:
            # check for tail
            potential = potential or (self.tail == data[-len(self.tail):])

        for middle in self.middle_bits:
            potential = potential and data.find(middle) != -1

        return potential

headers: dict[str, Matcher] = {}
headers["jfif"] = Matcher(header=bytearray(b"\xFF\xD8"),
                         tail=bytearray(b"\xFF\xD9"),
                         middle_bits=[bytearray(b"\xFF\xDA")])
headers["jpg"] = Matcher(header=bytearray(b"\xFF\xD8"), #SOI
                         tail=bytearray(b"\xFF\xD9"),   #EOI
                         #middle_bits=[
                         #    bytearray(b"\xFF\xC0"),    #SOF0
                         #    bytearray(b"\xFF\xC2"),    #SOF2
                         #    bytearray(b"\xFF\xC4"),    #DHT
                         #    bytearray(b"\xFF\xDB"),    #DQT
                         #    bytearray(b"\xFF\xDD"),    #DRI
                         #    bytearray(b"\xFF\xDA"),    #SOS
                         #]
                         )
headers["jpeg"] = headers["jpg"]
headers["pdf"] = Matcher(header=bytearray(b"\x25\x50\x44\x46\x2D"))
headers["bmp"] = Matcher(header=bytearray(b"\x42\x4D"))

# ACTIONS
ACTIONS = SimpleNamespace()
ACTIONS.LIST_FILETYPES = "list"
ACTIONS.BRUTE_FORCE = "bf"

THREADS: list[Thread] = []

def action_string(x: str):
    return list(map(lambda y: y.split("=")[1].replace("'", ""),
                        x.replace("(", "").replace(")", "")[9:].split(", ")))


# Argument validators
class FileTypeAction(Action):
    def __call__(self, parser, namespace, value, _=None):
        if value not in headers.keys():
            parser.error(f"Unsupported file format: {value}")
        setattr(namespace, self.dest, value)
class BFAction(Action):
    def __call__(self, parser, namespace, value, _=None):
        if value not in action_string(str(ACTIONS)):
            parser.error(f"Invalid action provided: {value}")
        setattr(namespace, self.dest, value)

def get_steg(steg_mode, wrapper, hidden, offset, interval) -> Steg:
    match steg_mode:
        case "bit":
            return StegBit(wrapper, hidden, offset, interval)
        case "byte":
            return StegByte(wrapper, hidden, offset, interval)

def write_file(file_path: str, data: bytearray):
    with open(file_path, "wb") as f:
        f.write(data)

def is_plaintext(data):
    # Check that all chars are printable
    if all(chr(byte) in printable for byte in data):
        return True

    # Check for common encodings
    for encoding in ['utf-8', 'ascii']:
        try:
            data.decode(encoding)
            return True
        except UnicodeDecodeError:
            pass

    return False

def brute_force(steg_mode: Literal["bit", "byte"], data: bytearray, start_offset, start_interval, outdir):
    for offset in range(start_offset, 8096):
        for interval in range(start_interval, start_interval+500):
            s = get_steg(steg_mode, data, bytearray(), offset, interval)
            result = s.retrieve()

            if offset == 1024 and interval == 2:
                print("".join([chr(x) for x in list(result[0:261])]))

            # using filetype
            kind = filetype.guess(result[0:261])
            if kind is not None:
                write_file(f"{outdir}/{offset}_{interval}.{kind.extension}", result)

            # is plaintext
            if is_plaintext(result):
                write_file(f"{outdir}/{offset}_{interval}.txt", result)

            # using my own matcher
            #for file_type, matcher in headers.items():
            #    if matcher.match_data(result):
            #        write_file(f"{outdir}/{offset}_{interval}.{file_type}", result)


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="StegBruteForce",
        description="Checks for combinations of intervals and offsets \
        that produce a file of a given format",
        epilog="Written by Jack Branch"
    )

    parser.add_argument("action", help=str(action_string(str(ACTIONS))), action=BFAction)

    parser.add_argument("-f", "--filetype", action=FileTypeAction,
                        help="Type of file to match against")

    inp = parser.add_mutually_exclusive_group()
    inp.add_argument("-i", "--input", help="Input file path")
    inp.add_argument("-is", "--stdin", help="Treat stdin as input")

    parser.add_argument("-so", "--start-offset", help="in bruteforce, start offset at this value")
    parser.add_argument("-si", "--start-interval", help="in bruteforce, start interval at this value")

    parser.add_argument("-sm", "--steg-mode", help="Set steg mode [bit, byte]")
    parser.add_argument("-o", "--outdir", help="Where should brute forced files be stored?")

    args = parser.parse_args()

    match args.action:
        case ACTIONS.LIST_FILETYPES:
            for e in headers.keys():
                print(e)
            exit(0)
        case "bf":

            if args.outdir is None:
                print("Please provide an outdir, seek --help", file=stderr)
                exit(1)

            # create outdir
            try:
                mkdir(args.outdir)
            except FileExistsError as e:
                pass
            except:
                print(f"Couldn't create directory, {args.outdir}", file=stderr)
                exit(1)

            if args.steg_mode is None:
                print("Please provide a steg-mode", file=stderr)
                exit(1)
            elif args.steg_mode not in ["bit", "byte"]:
                print("Please provide a valid steg-mode, [bit, byte]", file=stderr)
                exit(1)

            try:
                start_offset = 0 if args.start_offset is None else int(args.start_offset)
            except Exception as _:
                print("Invalid offset provided. Please provide a valid positive integer", file=stderr)
                exit(1)
            try:
                start_interval = 1 if args.start_interval is None else int(args.start_interval)
            except Exception as _:
                print("Invalid interval provided. Please provide a valid positive non-zero integer", file=stderr)
                exit(1)

            data = bytearray()

            match [args.input, args.stdin]:
                case [None, None]:
                    print("You must provide some form of input. Seek --help.", file=stderr)
                    exit(1)
                case [provided, None]:
                    # brute force provided file
                    f = open(provided, "rb")
                    data = bytearray(f.read())
                    f.close()
                    pass
                case [None, stdin]:
                    # brute force stdin
                    data = bytearray(stdin.buffer.read())
            brute_force(args.steg_mode, data, start_offset, start_interval, args.outdir)

            #bf_thread = Thread(target=brute_force, args=[args.steg_mode, data, start_offset, start_interval, args.outdir])
            #THREADS.append(bf_thread)
            #bf_thread.start()
            #bf_thread.join()


