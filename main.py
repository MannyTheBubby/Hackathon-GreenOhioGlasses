import socket
import threading

HEADER = 64
port = 9000
server = socket.gethostbyname(socket.gethostname())
ADDR = (server, port)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(format)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(format)
        if msg == "disconnect":
            connected = False

        
        print(f"[{addr}] {msg}")
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {server}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()