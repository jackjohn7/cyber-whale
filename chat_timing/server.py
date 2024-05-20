import socket
import time
import sys
import signal

def new_int_handler(conn: socket.socket):
    def interrupt_handler(_sig, _frame):
        conn.close()
        print("Connection closed, quitting...")
        sys.exit(0)
    return interrupt_handler


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

signal.signal(signal.SIGINT, new_int_handler(s))

# respond to every connection synchronously
while True:
    try:
        # accept connections
        c, addr = s.accept()

        print(f"Incoming connection from {addr}")
        msg = "When the "
        secret_msg = "I am inside your walls" + "EOF"
        secret_encoded = "".join([bin(ord(c))[2:].zfill(8) for c in secret_msg])
        print(secret_encoded)

        for i, ch in enumerate(secret_encoded):
            # needs to be converted to individual bytes to work
            c.send(msg[i%len(msg)].encode())
            time.sleep(ZERO if ch == "0" else ONE)

        c.send("EOF".encode())

        c.close()
    except KeyboardInterrupt:
        s.close()
        print("Connection closed, quitting...")
        sys.exit(0)

