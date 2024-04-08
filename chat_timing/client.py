import socket
import sys

ip = "localhost"
#ip = "138.47.165.71"
port = 1337
#port = 47765

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

data = s.recv(4096)

while data.decode().rstrip("\n") != "EOF":
    sys.stdout.write(data.decode())
    sys.stdout.flush()

    data = s.recv(4096)

s.close()
