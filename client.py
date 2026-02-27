import socket
import os
import time

HOST = os.getenv("SERVER_HOST", "server") 
PORT = int(os.getenv("SERVER_PORT", "65432"))
MESSAGE = os.getenv("MESSAGE", "hello from client")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(MESSAGE.encode())
    data = s.recv(1024)

print(data.decode(errors="replace"))