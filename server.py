import socket
import threading
import os
#HOST = "127.0.0.1"
HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", 65432))

def client_handling(conn, addr):
    print(f"Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg = data.decode("utf-8", errors="replace")
            print(f"Received: {msg}")
            response = f"Client message: {msg}"
            conn.sendall(response.encode("utf-8"))
    print(f"Connection closed by {addr}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server is listening on port {PORT}")
        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=client_handling, args=(conn, addr), daemon=True)
            t.start()

if __name__ == "__main__":
    main()

