from abc import ABC, abstractmethod

SENTINEL = [0x0, 0xFF, 0x0, 0x0, 0xFF, 0x0]

class Steg(ABC):
    @abstractmethod
    def store(self) -> list[int]:
        pass
    @abstractmethod
    def retrieve(self) -> list[int]:
        pass

class StegByte(Steg):
    def __init__(self, wrapper: bytearray, hidden: bytearray, offset: int, interval: int):
        self.wrapper = wrapper
        self.hidden = hidden
        self.offset = offset
        self.interval = interval

    def store(self):
        w = self.wrapper
        h = self.hidden
        offset = self.offset
        for i in range(len(h)):
            w[offset] = h[i]
            offset += self.interval

        for i in range(len(SENTINEL)):
            w[offset] = SENTINEL[i]
            offset += self.interval

        return list(w)

    def retrieve(self):
        w = self.wrapper
        h = []
        offset = self.offset
        while offset < len(w):
            b = w[offset]
            h.append(b)
            offset += self.interval
        return list(h)

class StegBit(Steg):
    def __init__(self, wrapper, hidden, offset, interval):
        self.wrapper = wrapper
        self.hidden = hidden
        self.offset = offset
        self.interval = interval

    def store(self):
        w = self.wrapper
        h = self.hidden
        offset = self.offset
        for i in range(len(h)):
            for _ in range(8):
                w[offset] &= 0b11111110
                w[offset] |= ((h[i] & 0b10000000) >> 7)
                #h[i] <<= 1
                h[i] = (h[i] << 1) & (2 ** 8 - 1)
                offset += self.interval

        for i in range(len(SENTINEL)):
            for _ in range(8):
                w[offset] &= 0b11111110
                w[offset] |= ((SENTINEL[i] & 0b10000000) >> 7)
                #SENTINEL[i] <<= 1
                SENTINEL[i] = (SENTINEL[i] << 1) & (2 ** len(SENTINEL) - 1)
        return list(w)

    def retrieve(self):
        w = self.wrapper
        h = bytearray()
        offset = self.offset
        s_count = -1

        while offset < len(w):
            b = 0
            for j in range(8):
                b |= w[offset] & 0b1
                if j < 7:
                    #b <<= 1
                    b = (b << 1) & (2 ** 8 - 1)
                    offset += self.interval

            if SENTINEL[s_count+1] == b:
                print(s_count)
                s_count += 1
            else:
                s_count = -1

            if s_count == len(SENTINEL)-1:
                h.append(b)
                break


            h.append(b)
            offset += self.interval

        return list(h)[0:-len(SENTINEL)]


if __name__ == "__main__":
    from args import Args
    from sys import argv
    from traceback import format_exc

    from sys import exit
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
            print("".join([chr(c) for c in steg.retrieve()]))
        else:
            print("".join([chr(c) for c in steg.store()]))

    except cli_errors.CliError as e:
        print(e)
        print(cli_errors.usage(argv[0]))
        exit(1)
    except Exception as e:
        print("Oops... An unexpected error occurred")
        print(e)
        print(format_exc())
        print(cli_errors.usage(argv[0]))
        exit(1)



