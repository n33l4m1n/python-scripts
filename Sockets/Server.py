# A network socket is an internal endpoint for sending or receiving data within a node on a computer network.
import socket

# AF_INET is an address family corresponding to Internet Protocol version 4 (IPv4).
# SOCK_STREAM means that this is a Transmission Control Protocol (TCP) socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to tuple of IP and port.
# Using local IP of host and ephemeral port.
s.bind((socket.gethostname(), 4242))

# Prepare to listen and limit connections with a queue of two.
s.listen(5)

# Listen continuously for client socket object.
while True:
    clientsocket, address = s.accept()
    print(f'connection from {address} has been established!')
    clientsocket.send(bytes('Welcome to the server!', 'utf-8'))
    clientsocket.close()