import socket
import os
import time

#gets host and port from environment variables
HOST = os.getenv("SERVER_HOST", "server") 
PORT = int(os.getenv("SERVER_PORT", "65432"))
MESSAGE = os.getenv("MESSAGE", "hello from client")

#creates a TCP/IP socket and connects to the server, sends a message, and prints the response
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(MESSAGE.encode())
    data = s.recv(1024)

print(data.decode(errors="replace"))