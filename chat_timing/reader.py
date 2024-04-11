
def to_cov_bin(data: list[float], zero: float, one: float) -> str:

    diffs: list[float] = [0.0] * len(data)
    i, j = 0, 1
    while j < len(data):
        diffs[i] = round(data[j] - data[i], 3)
        i += 1
        j += 1

    return "".join(list(map(translate(zero, one), diffs)))

def analyze(data: list[float]) -> tuple[float, float]:
    """
    Use statistics to figure out likely 0 and 1 delays
    """
    return (0.0,0.0)

# TODO: Look into whether or not zero is required
# Perhaps it's still needed since you could also 
# calculate based on which the difference is closer to
# or you might also need it when denoising
def translate(zero: float, one: float):
    def aux(diff: float):
        if diff >= one:
            return "1"
        else:
            return "0"

    return aux

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
    from binascii import unhexlify
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

    s.close()

    mapped_binary = to_cov_bin(chat_delays, 0.025, 0.1)
    hex_string = hex(int(mapped_binary, 2))[2:]
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string

    print(hex_string)
    decoded_bytes = unhexlify(hex_string)
    print(decoded_bytes)

    decoded_message = decoded_bytes.decode('utf-8')

    print(decoded_message[:-3])

