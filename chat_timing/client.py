from binascii import unhexlify
import socket
from time import time

ip = "localhost"
#ip = "138.47.165.71"
port = 1337
#port = 47765

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

covert_bin = ""

data = s.recv(4096)

while data.decode().rstrip("\n") != "EOF":
    t0 = time()
    data = s.recv(4096)
    t1 = time()
    delta = round(t1 - t0, 3)
    if (delta >= 0.1):
        covert_bin += "1"
    else: 
        covert_bin += "0"


# i = 0
# while (i < len(covert_bin)):
#     b = covert_bin[i:i+8]
#     n = int(b, 2)
#     try:
#         covert += unhexlify(f"{n:02x}")
#     except TypeError:
#         covert += "?"
#     i+=8

hex_string = hex(int(covert_bin, 2))[2:]
if len(hex_string) % 2 != 0:
    hex_string = '0' + hex_string

print(hex_string)
decoded_bytes = unhexlify(hex_string)
print(decoded_bytes)

decoded_message = decoded_bytes.decode('utf-8')

print(decoded_message[:-3])


s.close()
