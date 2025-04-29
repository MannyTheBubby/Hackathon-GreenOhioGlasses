import socket
import threading

HEADER = 64
port = 9000
server = socket.gethostbyname(socket.gethostname())
ADDR = (server, port)
FORMAT = "utf-8"
