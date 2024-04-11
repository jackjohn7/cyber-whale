
def to_cov_bin(data: list[float], zero: float, one: float) -> str:

    diffs: list[float] = [0.0] * (len(data)-1)
    i, j = 0, 1
    while j < len(data):
        diffs[i] = round(data[j] - data[i], 3)
        i += 1
        j += 1

    #mapper = lambda x : "1" if x >= one else "0" if one > zero else lambda x : "0" if x >= zero else "1"
    return "".join(list(map(translate(zero, one), diffs)))

def analyze(_: list[float]) -> tuple[float, float]:
    """
    Use statistics to figure out likely 0 and 1 delays
    """
    return (0.0,0.0)

def translate(zero: float, one: float):
    """
    Optimized to return the correct function based on which is set to be higher
    """
    def aux(diff: float):
        if diff >= one:
            return "1"
        else:
            return "0"

    def aux2(diff: float):
        if diff >= zero:
            return "0"
        else:
            return "1"

    return aux if one > zero else aux2

def denoise(diffs: list[float]) -> list[float]:
    """
    use statistics to denoise data
    """
    # TODO: Implement
    return diffs

if __name__ == "__main__":
    import socket
    import sys
    import time
    ip = "localhost"
    #ip = "138.47.165.156"
    port = 1337
    #port = 31337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    chat_delays = []

    while (data := s.recv(4096)).decode().rstrip("\n") != "EOF":
        sys.stdout.write(data.decode())
        chat_delays.append(time.time())
        sys.stdout.flush()
    chat_delays.append(time.time()) # Time of EOF message

    s.close()
    sys.stdout.write("\n")

    mapped_binary = to_cov_bin(chat_delays, 0.025, 0.1)
    result = "".join([chr(int(mapped_binary[i:i+8], 2)) for i in range(0, len(mapped_binary), 8)])[0:-3]
    print(result)

    # Also works
    #hex_string = hex(int(mapped_binary, 2))[2:]
    #if len(hex_string) % 2 != 0:
    #    hex_string = '0' + hex_string

    #print(hex_string)
    #decoded_bytes = unhexlify(hex_string)
    #print(decoded_bytes)

    #decoded_message = decoded_bytes.decode('utf-8')

    #print(decoded_message[:-3])

