from abc import ABC, abstractmethod
import logging

SENTINEL = bytearray(b"\x00\xff\x00\x00\xff\x00")

DEBUG = False
logger = logging.getLogger(__name__)
if not DEBUG:
    logger.disabled = True
else:
    logging.basicConfig(filename='out.log', encoding='utf-8', level=logging.DEBUG)

class Steg(ABC):
    @abstractmethod
    def store(self) -> bytearray:
        """Store one file inside another file"""
        pass
    @abstractmethod
    def retrieve(self) -> bytearray:
        """Retrieve file from inside another file"""
        pass

class StegByte(Steg):
    def __init__(self, wrapper: bytearray, hidden: bytearray, offset: int, interval: int):
        self.wrapper = wrapper
        self.hidden = hidden
        self.offset = offset
        self.interval = interval

    def store(self):
        logger.debug("storing bytes")
        w = self.wrapper
        h = self.hidden
        offset = self.offset
        # write hidden to wrapper
        for i in range(len(h)):
            w[offset] = h[i]
            offset += self.interval

        # write sentinel to wrapper
        for i in range(len(SENTINEL)):
            w[offset] = SENTINEL[i]
            offset += self.interval

        return w

    def retrieve(self):
        logger.debug("retrieving bytes")
        w = self.wrapper
        h = bytearray()
        # read data from hidden file until sentinel
        for offset in range(self.offset, len(w), self.interval):
            b = w[offset]
            if h[-len(SENTINEL):] == SENTINEL:
                logger.debug("encountered sentinel")
                h = h[:-len(SENTINEL)]
                break
            h.append(b)
        return h

class StegBit(Steg):
    def __init__(self, wrapper, hidden, offset, interval):
        self.wrapper = wrapper
        self.hidden = hidden
        self.offset = offset
        self.interval = interval

    def store(self):
        logger.debug("storing bits")
        w = self.wrapper
        h = self.hidden
        offset = self.offset
        # write hidden to wrapper
        for i in range(len(h)):
            for _ in range(8):
                w[offset] &= 0b11111110
                w[offset] |= ((h[i] & 0b10000000) >> 7)
                h[i] = (h[i] << 1) & (2 ** 8 - 1)
                offset += self.interval

        # write sentinel to wrapper
        for i in range(len(SENTINEL)):
            for _ in range(8):
                w[offset] &= 0b11111110
                w[offset] |= ((SENTINEL[i] & 0b10000000) >> 7)
                SENTINEL[i] = (SENTINEL[i] << 1) & (2 ** 8 - 1)
                offset += self.interval
        return w

    def retrieve(self):
        logger.debug("retrieving bits")
        w = self.wrapper
        h = bytearray()
        offset = self.offset

        # read data from hidden file until sentinel or wrapper EOF
        while offset < len(w):
            b = 0
            for j in range(8):
                b <<= 1
                b |= w[offset] & 0b00000001
                if j < 7:
                    offset += self.interval
            if h[-len(SENTINEL):] == SENTINEL:
                logger.debug("encountered sentinel")
                h = h[:-len(SENTINEL)]
                break
            h.append(b)
            offset += self.interval

        return h

if __name__ == "__main__":
    from args import Args
    from sys import argv, stdout
    from traceback import format_exc

    from sys import exit, stderr
    import cli_errors

    args = Args()

    try:
        args.parse(argv[1:])
        hidden = bytearray()
        # if hidden file is provided, read it to hidden
        if args.hidden is not None:
            in_file = open(args.hidden, "rb")
            hidden = bytearray(in_file.read())
            in_file.close()
        if args.wrapper is None:
            exit(1)

        wrapper_file = open(args.wrapper, "rb")
        wrapper = bytearray(wrapper_file.read())
        wrapper_file.close()

        steg: Steg
        if args.data_mode == "byte":
            steg = StegByte(wrapper, hidden, args.offset, args.interval)
        else:
            steg = StegBit(wrapper, hidden, args.offset, args.interval)

        if args.action == "retrieve":
            stdout.buffer.write(steg.retrieve())
        else:
            stdout.buffer.write(steg.store())
        logger.debug("wrote to file")

    except cli_errors.CliError as e:
        print(e, file=stderr)
        print(cli_errors.usage(argv[0]), file=stderr)
        exit(1)
    except Exception as e:
        print("Oops... An unexpected error occurred", file=stderr)
        print(e, file=stderr)
        logger.error(format_exc())
        print(cli_errors.usage(argv[0]), file=stderr)
        exit(1)
