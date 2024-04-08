import socket
import time

EOF = "EOF"
ZERO = 0.025
ONE = 0.1

"""
NOTE:

bin(ord(some_char))[2:].zfill(8) returns 8-bit binary 
string representation of some_char

length of nonsense msg = length of covert msg + 1

msg,
n = 0
for i in msg:
    c.send(i)
    if (cover_bin[n] == "0"):
        time.sleep(ZERO)
    else:
        time.sleep(ONE)
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1337 #31337 in Timo's server

s.bind(("", port))

s.listen(0)

# respond to every connection synchronously
while True:
    # accept connections
    c, addr = s.accept()

    print(f"Incoming connection from {addr}")
    msg = "Some message here"

    for i in msg:
        # needs to be converted to individual bytes to work
        c.send(i.encode())
        time.sleep(0.1)

    c.send("EOF".encode())

    c.close()
