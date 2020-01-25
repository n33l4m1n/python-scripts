# A network socket is an internal endpoint for sending or receiving data within a node on a computer network.
import socket

# AF_INET is an address family corresponding to Internet Protocol version 4 (IPv4).
# SOCK_STREAM means that this is a Transmission Control Protocol (TCP) socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at localhost port 4242
s.connect((socket.gethostname(), 4242))

#
msg = s.recv(1024)
print(msg.decode("utf-8"))