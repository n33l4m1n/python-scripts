import socket

#AF_INET is an address family corresponding to Internet Protocol version 4 (IPv4).
#SOCK_STREAM means that this is a Transmission Control Protocol (TCP) socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)